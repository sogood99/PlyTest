# Subset C's CFG (BNF)

## Syntax rules for subset of C we are working with.

```c
program : include program
        | external_decl program
        | include
        | external_decl

include : #include < ID . ID >

/* External Declarations (函数外声明) */
exernal_decl    : decl ; // int a = 10; etc.
                | func_def // void f(){ ... }

/* decl */

decl    : usual_dec // int a, b=2, d, g();
        | new_type_dec // new class or struct

type    : VOID | CHAR | SHORT | INT | LONG | FLOAT | DOUBLE

/* struct class begin: */
// self defined data structures (struct, class)

new_type_dec    : new_type ID { new_type_params }
                | new_type ID { new_type_params } declarators
                | new_type ID declarators

new_type : CLASS | STRUCT

// only support the simple params
new_type_params : new_type_param; new_type_params
                | new_type_param; // inside struct {... int a; ...} where int a; is the param

new_type_param  : type ID ;

/* struct class end */

usual_dec : type declarators ;

// can can many declarator (eg. int a,b,c,d,e )
declarators : declarator_1
            | declarator_1 , declarators

// level 1 of declaration, assign or not
declarator_1    : declarator_2 = initializer // pointers
                | declarator_2

// level 2 of declaration, pointer or not
declarator_2    : * declarator_3
                | declarator_3

// level 3 of declaration, parenthasis/function declaration etc. may have to go up a level: eg. char (*(*x())[])() function returning pointer to array[] of pointer to function returning char
declaration_3   : ID
                | ( declarator_2 )
                | declarator_2 [ expression ]
                | declarator_2 [  ]
                | declarator_2 ( params )
                | declarator_2 (  )

// params eg. int a, int, float * etc.
params  : param , params
        | param

param   : type declarator_2

// initializer used in declarator_1

initializer : expression
            | { expressions }

expressions : expression , expressions
            | expression

/* function definition */

func_def        : type ID ( params ) { statements }
                | type ID ( ) { statements }
                | VOID ID ( params ) { }
                | VOID ID (  ) { }

// c statements

statements  : statement statements
            | statement

statement       : expression ; // a+1*10
                | decl ; // int a = 10;
                | block
                | conditional // if () {} else {}
                | iteration // while () {}
                | jump ;
                | ; // many ;'s

block           : { stats_or_null } // block statements

conditional     : if ( expression ) statement
                | if ( expression ) statement else conditional // higher precedence
                | if ( expression ) statement else statement // lower precedence

iteration       : while ( expression ) statement
                | do statement while ( expression ) ;
                | for ( expr_or_null_or_init ; expr_or_null ; expr_or_null ) statement

stats_or_null : statements // statements or empty
                | empty

expr_or_null    : expression
                | empty

expr_or_null_or_init    : expr_or_null
                        | usual_dec

jump            : break
                | continue
                | return
                | return expression

/* expressions in the order of operation */
expression      : or_expr assignment_op expression

assignment_op   : = | *= | /= | %= | += | -= | <<=
                | >>= | $= | ^= | |=

or_expr         : and_expr || and_expr
                | and_expr

and_expr        : xor_expr && xor_expr
                | xor_expr

xor_expr        : eq_expr ^ eq_expr
                | eq_expr

eq_expr         : rel_expr
                | eq_expr == rel_expr
                | eq_expr != rel_expr

rel_expr        : shift_expr
                | rel_expr < shift_expr
                | rel_expr > shift_expr
                | rel_expr <= shift_expr
                | rel_expr >= shift_expr

shift_expr      : add_expr
                | shift_expr << add_expr
                | shift_expr >> add_expr

add_expr        : mult_expr
                | add_expr + mult_expr
                | add_expr - mult_expr

mult_expr       : pre_unary_expr
                | mult_expr * pre_unary_expr
                | mult_expr / pre_unary_expr

pre_unary_expr  : post_unary_expr
                | ++ pre_unary_expr
                | -- pre_unary_expr
                | +  pre_unary_expr
                | -  pre_unary_expr
                | !  pre_unary_expr
                | &  pre_unary_expr

post_unary_expr : element
                | post_unary_expr [ expression ]
                | post_unary_expr ( expressions )
                | post_unary_expr ( )
                | post_unary_expr ++
                | post_unary_expr --
                | post_unary_expr . ID
                | post_unary_expr -> ID

element : ID
        | NUMBER // 11212.12121
        | CHR // character 'a'
        | STR // string "abd"
        | ( expression )
```

## Currently not supprted styles (that i know of):

```c
#define
typedef
class ;// with public private
int * bar(); // functions that return complex types
struct ... {... } *i_1, i_2[10], *i_3[20]; // struct with complex initializations (eg. *i_1 )
int foo(int, float, int) // function definition with type but no var name
int foo(float a, ...) // stdarg style three dots ...
a | b // bitwise operations
switch () // switch statements
goto // will not plan on adding
```

## Comments

The production:

```c
statement       : ....
                | conditional
                | block // { ....;....; }
conditional     : if ( expression ) statement
                | if ( expression ) statement else statement
```

generated 1 parse reduce warning:

```
$ python3 parser.py test.c
WARNING: no p_error() function is defined
Generating LALR tables
WARNING: 1 shift/reduce conflict
```

this is because when the parser encounters an `else`, it doesn't know whether to reduce the last `if` and leave the `else` for the last last `if`:

```c
        if ------------- combined
->      if --- reduce
        else ----------- combined
```

or reduce the last `if` with the `else`.

```c
        if ---- waiting
->      if ------------- combined
        else ----------- combined
```

By default it will do the correct thing (combine with current if) since by default it favors shifting, so it will shift to the end and then pop everything out, which is equivalent to stack operation (popping). We can get rid of the conflict by specifying reduce precedence:

```python
precedence = (
        ...,
        ('left', "THEN"),
        ('left', 'ELSE'),
)

...

def p_conditional(p):
    """
        conditional : IF '(' expression ')' statement %prec THEN
    """
    p[0] = n("conditional", [p[3], p[5]])


def p_conditional_else(p):
    """
        conditional : IF '(' expression ')' statement ELSE statement
    """
    p[0] = n("conditional", [p[3], p[5], p[7]], "else")
```
