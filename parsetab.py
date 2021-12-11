
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left?:leftLOGORleftLOGANDleft^leftLOGEQLOGNEQleft<>LEQGEQleftLSHIFTRSHIFTleft+-left*/rightLPLUSPLUSLMINUSMINUSLPOSLNEGLNOTleftRPLUSPLUSRMINUSMINUS.RARROWADDEQ BREAK CHAR CHR CLASS CONTINUE DIVEQ DO DOUBLE ELSE FLOAT FOR GEQ ID IF INCLUDE INT LEQ LOGAND LOGEQ LOGNEQ LOGOR LONG LSHIFT MINUSMINUS MODEQ MULTEQ NUMBER PLUSPLUS RARROW RETURN RSHIFT SHORT STR STRUCT SUBEQ VOID WHILE\n        program : include program\n                | external_decl program\n    \n        program : include\n                | external_decl\n    \n        include : INCLUDE\n    \n        external_decl   : decl ';'\n                        | func_def\n    \n        external_decl : ';'\n    \n        decl    : usual_dec\n                | new_type_dec\n    \n        usual_dec : type declarators\n    \n        declarators : declarator_1 ',' declarators\n    \n        declarators : declarator_1\n    \n        declarator_1    : declarator_2\n    \n        declarator_1    : declarator_2 '=' initializer\n    \n        declarator_2    : ID\n    \n        declarator_2    : ID '(' ')'\n    \n        declarator_2    : ID '[' ']'\n    \n        declarator_2    : ID '[' expression ']'\n    \n        initializer : expression\n                    | '{' expressions '}'\n    \n        new_type_dec    : new_type ID '{' new_type_params '}'\n    \n        new_type    : STRUCT\n                    | CLASS\n    \n        new_type_params : new_type_param new_type_params\n    \n        new_type_params : new_type_param\n    \n        new_type_param : type declarators ';'\n    \n        func_def : type ID '(' params ')' '{' statements '}'\n    \n        func_def : type ID '(' ')' '{' statements '}'\n    \n        func_def : type ID '(' params ')' '{' '}'\n    \n        func_def : type ID '(' ')' '{' '}'\n    \n        params : param ',' params\n    \n        params : param\n    \n        param : type declarator_2\n    \n        statements : statement statements\n    \n        statements : statement\n    \n        statement   : expression ';'\n                    | decl ';'\n                    | conditional\n                    | iteration\n                    | jump ';'\n    \n        statement : ';'\n    \n        conditional : IF '(' expression ')' '{' stats_or_null '}'\n    \n        conditional : IF '(' expression ')' '{' stats_or_null '}' ELSE conditional\n    \n        conditional : IF '(' expression ')' '{' stats_or_null '}' ELSE '{' stats_or_null '}'\n    \n        statement : '{' stats_or_null '}'\n    \n        stats_or_null   : statements\n                        | empty\n    \n        iteration : WHILE '(' expression ')' '{' stats_or_null '}'\n    \n        iteration : DO '{' stats_or_null '}' WHILE '(' expression ')' ';'\n    \n        iteration : FOR '(' expr_or_null_or_init ';' expr_or_null ';' expr_or_null ')' '{' stats_or_null '}'\n    \n        expr_or_null    : expression\n                        | empty\n    \n        expr_or_null_or_init    : expr_or_null\n                                | usual_dec\n    \n        assignment_expr : ID assignmenteq_op expression\n    \n        assignmenteq_op     : '='\n                            | MULTEQ\n                            | ADDEQ\n                            | SUBEQ\n                            | MODEQ\n                            | DIVEQ\n    \n        jump    : BREAK\n                | CONTINUE\n                | RETURN\n    \n        jump : RETURN expression\n    \n        expressions : expression ',' expressions\n    \n        expressions : expression\n    \n        expression  : bin_expr\n                    | assignment_expr\n    \n        expression  : bin_expr '?' bin_expr ':' bin_expr\n    \n        bin_expr    : pre_unary_expr bin_op bin_expr\n    \n        bin_expr    : pre_unary_expr\n    \n        bin_op      : '+'\n                    | '-'\n                    | '*'\n                    | '/'\n                    | LOGAND\n                    | LOGOR\n                    | LOGEQ\n                    | LOGNEQ\n                    | LSHIFT\n                    | RSHIFT\n                    | '<'\n                    | '>'\n                    | LEQ\n                    | GEQ\n                    | '^'\t\n    \n        pre_unary_expr  : PLUSPLUS pre_unary_expr %prec LPLUSPLUS\n                        | MINUSMINUS pre_unary_expr %prec LMINUSMINUS\n                        | '+' pre_unary_expr %prec LPOS\n                        | '-' pre_unary_expr %prec LNEG\n                        | '!' pre_unary_expr %prec LNOT\n    \n        pre_unary_expr : post_unary_expr\n    \n        post_unary_expr : post_unary_expr '[' expression ']'\n    \n        post_unary_expr : post_unary_expr '(' ')'\n    \n        post_unary_expr : post_unary_expr '(' expressions ')'\n    \n        post_unary_expr : post_unary_expr PLUSPLUS %prec RPLUSPLUS\n                        | post_unary_expr MINUSMINUS %prec RMINUSMINUS\n    \n        post_unary_expr : post_unary_expr '.' ID\n                        | post_unary_expr RARROW ID\n    \n        post_unary_expr : element\n    \n        element : ID\n    \n        element : NUMBER\n                | CHR\n                | STR\n    \n        type    : VOID\n                | CHAR\n                | SHORT\n                | INT\n                | LONG\n                | FLOAT\n                | DOUBLE\n    \n        empty :\n    "
    
_lr_action_items = {'INCLUDE':([0,2,3,4,6,7,23,113,142,146,160,],[4,4,4,-5,-8,-7,-6,-31,-30,-29,-28,]),';':([0,2,3,4,5,6,7,8,9,23,24,25,26,27,36,38,39,41,42,43,49,50,51,52,53,54,55,56,57,64,73,91,92,93,94,95,96,99,100,106,108,109,111,113,114,115,116,117,118,119,120,125,126,127,129,131,133,135,136,137,138,142,146,148,149,150,153,154,155,157,158,160,161,165,166,167,168,169,170,174,175,176,178,183,184,188,190,191,192,193,196,197,],[6,6,6,-5,23,-8,-7,-9,-10,-6,-16,-11,-13,-14,-17,-103,-18,-69,-70,-73,-94,-102,-104,-105,-106,-12,-16,-15,-20,116,-19,-89,-103,-90,-91,-92,-93,-98,-99,-22,140,116,116,-31,116,148,-42,149,-39,-40,150,-63,-64,-65,-56,-72,-96,-100,-101,-17,-21,-30,-29,-37,-38,-41,116,-114,-66,-95,-97,-28,-46,174,-54,-55,-52,-53,-71,-114,116,116,182,-43,-49,192,116,-44,-50,116,-45,-51,]),'VOID':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[12,12,12,-5,-8,-7,-6,12,12,12,12,12,12,12,-31,12,-42,-39,-40,-27,-30,-29,-37,-38,-41,12,12,-28,-46,12,12,-43,-49,12,-44,-50,12,-45,-51,]),'CHAR':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[13,13,13,-5,-8,-7,-6,13,13,13,13,13,13,13,-31,13,-42,-39,-40,-27,-30,-29,-37,-38,-41,13,13,-28,-46,13,13,-43,-49,13,-44,-50,13,-45,-51,]),'SHORT':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[14,14,14,-5,-8,-7,-6,14,14,14,14,14,14,14,-31,14,-42,-39,-40,-27,-30,-29,-37,-38,-41,14,14,-28,-46,14,14,-43,-49,14,-44,-50,14,-45,-51,]),'INT':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[15,15,15,-5,-8,-7,-6,15,15,15,15,15,15,15,-31,15,-42,-39,-40,-27,-30,-29,-37,-38,-41,15,15,-28,-46,15,15,-43,-49,15,-44,-50,15,-45,-51,]),'LONG':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[16,16,16,-5,-8,-7,-6,16,16,16,16,16,16,16,-31,16,-42,-39,-40,-27,-30,-29,-37,-38,-41,16,16,-28,-46,16,16,-43,-49,16,-44,-50,16,-45,-51,]),'FLOAT':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[17,17,17,-5,-8,-7,-6,17,17,17,17,17,17,17,-31,17,-42,-39,-40,-27,-30,-29,-37,-38,-41,17,17,-28,-46,17,17,-43,-49,17,-44,-50,17,-45,-51,]),'DOUBLE':([0,2,3,4,6,7,23,29,33,60,64,65,109,111,113,114,116,118,119,140,142,146,148,149,150,153,154,160,161,175,176,183,184,190,191,192,193,196,197,],[18,18,18,-5,-8,-7,-6,18,18,18,18,18,18,18,-31,18,-42,-39,-40,-27,-30,-29,-37,-38,-41,18,18,-28,-46,18,18,-43,-49,18,-44,-50,18,-45,-51,]),'STRUCT':([0,2,3,4,6,7,23,64,109,111,113,114,116,118,119,142,146,148,149,150,153,160,161,175,176,183,184,190,191,192,193,196,197,],[19,19,19,-5,-8,-7,-6,19,19,19,-31,19,-42,-39,-40,-30,-29,-37,-38,-41,19,-28,-46,19,19,-43,-49,19,-44,-50,19,-45,-51,]),'CLASS':([0,2,3,4,6,7,23,64,109,111,113,114,116,118,119,142,146,148,149,150,153,160,161,175,176,183,184,190,191,192,193,196,197,],[20,20,20,-5,-8,-7,-6,20,20,20,-31,20,-42,-39,-40,-30,-29,-37,-38,-41,20,-28,-46,20,20,-43,-49,20,-44,-50,20,-45,-51,]),'$end':([1,2,3,4,6,7,21,22,23,113,142,146,160,],[0,-3,-4,-5,-8,-7,-1,-2,-6,-31,-30,-29,-28,]),'ID':([10,11,12,13,14,15,16,17,18,19,20,30,31,32,34,44,45,46,47,48,58,61,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,101,102,109,110,111,114,116,118,119,127,139,148,149,150,151,152,153,154,156,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[24,28,-107,-108,-109,-110,-111,-112,-113,-23,-24,38,55,38,55,92,92,92,92,92,38,55,38,38,-57,-58,-59,-60,-61,-62,92,92,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,38,38,135,136,38,55,38,38,-42,-39,-40,38,38,-37,-38,-41,38,38,38,38,92,-46,38,38,38,38,38,-43,-49,38,-44,-50,38,-45,-51,]),'(':([24,38,49,50,51,52,53,55,92,99,100,121,122,124,133,135,136,157,158,177,],[29,-103,98,-102,-104,-105,-106,103,-103,-98,-99,151,152,154,-96,-100,-101,-95,-97,181,]),'=':([24,27,36,38,39,55,73,137,],[-16,32,-17,67,-18,-16,-19,-17,]),',':([24,26,27,36,37,38,39,41,42,43,49,50,51,52,53,55,56,57,62,73,91,92,93,94,95,96,99,100,105,129,131,133,135,136,137,138,157,158,170,],[-16,31,-14,-17,65,-103,-18,-69,-70,-73,-94,-102,-104,-105,-106,-16,-15,-20,-34,-19,-89,-103,-90,-91,-92,-93,-98,-99,139,-56,-72,-96,-100,-101,-17,-21,-95,-97,-71,]),'[':([24,38,49,50,51,52,53,55,92,99,100,133,135,136,157,158,],[30,-103,97,-102,-104,-105,-106,30,-103,-98,-99,-96,-100,-101,-95,-97,]),'{':([28,32,36,63,64,109,111,114,116,118,119,123,148,149,150,153,161,171,172,175,176,183,184,187,189,190,191,192,193,196,197,],[33,58,64,109,111,111,111,111,-42,-39,-40,153,-37,-38,-41,111,-46,175,176,111,111,-43,-49,190,193,111,-44,-50,111,-45,-51,]),')':([29,35,37,38,39,41,42,43,49,50,51,52,53,55,62,73,91,92,93,94,95,96,98,99,100,103,105,128,129,131,133,134,135,136,137,157,158,159,162,163,168,169,170,182,185,186,],[36,63,-33,-103,-18,-69,-70,-73,-94,-102,-104,-105,-106,-16,-34,-19,-89,-103,-90,-91,-92,-93,133,-98,-99,137,-68,-32,-56,-72,-96,158,-100,-101,-17,-95,-97,-67,171,172,-52,-53,-71,-114,188,189,]),']':([30,38,40,41,42,43,49,50,51,52,53,91,92,93,94,95,96,99,100,129,131,132,133,135,136,157,158,170,],[39,-103,73,-69,-70,-73,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-56,-72,157,-96,-100,-101,-95,-97,-71,]),'PLUSPLUS':([30,32,38,44,45,46,47,48,49,50,51,52,53,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,97,98,99,100,109,111,114,116,118,119,127,133,135,136,139,148,149,150,151,152,153,154,156,157,158,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[44,44,-103,44,44,44,44,44,99,-102,-104,-105,-106,44,44,44,-57,-58,-59,-60,-61,-62,44,44,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-103,44,44,-98,-99,44,44,44,-42,-39,-40,44,-96,-100,-101,44,-37,-38,-41,44,44,44,44,44,-95,-97,-46,44,44,44,44,44,-43,-49,44,-44,-50,44,-45,-51,]),'MINUSMINUS':([30,32,38,44,45,46,47,48,49,50,51,52,53,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,97,98,99,100,109,111,114,116,118,119,127,133,135,136,139,148,149,150,151,152,153,154,156,157,158,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[45,45,-103,45,45,45,45,45,100,-102,-104,-105,-106,45,45,45,-57,-58,-59,-60,-61,-62,45,45,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-103,45,45,-98,-99,45,45,45,-42,-39,-40,45,-96,-100,-101,45,-37,-38,-41,45,45,45,45,45,-95,-97,-46,45,45,45,45,45,-43,-49,45,-44,-50,45,-45,-51,]),'+':([30,32,38,43,44,45,46,47,48,49,50,51,52,53,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,109,111,114,116,118,119,127,133,135,136,139,148,149,150,151,152,153,154,156,157,158,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[46,46,-103,76,46,46,46,46,46,-94,-102,-104,-105,-106,46,46,46,-57,-58,-59,-60,-61,-62,46,46,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-103,-90,-91,-92,-93,46,46,-98,-99,46,46,46,-42,-39,-40,46,-96,-100,-101,46,-37,-38,-41,46,46,46,46,46,-95,-97,-46,46,46,46,46,46,-43,-49,46,-44,-50,46,-45,-51,]),'-':([30,32,38,43,44,45,46,47,48,49,50,51,52,53,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,109,111,114,116,118,119,127,133,135,136,139,148,149,150,151,152,153,154,156,157,158,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[47,47,-103,77,47,47,47,47,47,-94,-102,-104,-105,-106,47,47,47,-57,-58,-59,-60,-61,-62,47,47,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-103,-90,-91,-92,-93,47,47,-98,-99,47,47,47,-42,-39,-40,47,-96,-100,-101,47,-37,-38,-41,47,47,47,47,47,-95,-97,-46,47,47,47,47,47,-43,-49,47,-44,-50,47,-45,-51,]),'!':([30,32,44,45,46,47,48,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,109,111,114,116,118,119,127,139,148,149,150,151,152,153,154,156,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[48,48,48,48,48,48,48,48,48,48,-57,-58,-59,-60,-61,-62,48,48,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,48,48,48,48,48,-42,-39,-40,48,48,-37,-38,-41,48,48,48,48,48,-46,48,48,48,48,48,-43,-49,48,-44,-50,48,-45,-51,]),'NUMBER':([30,32,44,45,46,47,48,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,109,111,114,116,118,119,127,139,148,149,150,151,152,153,154,156,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[51,51,51,51,51,51,51,51,51,51,-57,-58,-59,-60,-61,-62,51,51,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,51,51,51,51,51,-42,-39,-40,51,51,-37,-38,-41,51,51,51,51,51,-46,51,51,51,51,51,-43,-49,51,-44,-50,51,-45,-51,]),'CHR':([30,32,44,45,46,47,48,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,109,111,114,116,118,119,127,139,148,149,150,151,152,153,154,156,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[52,52,52,52,52,52,52,52,52,52,-57,-58,-59,-60,-61,-62,52,52,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,52,52,52,52,52,-42,-39,-40,52,52,-37,-38,-41,52,52,52,52,52,-46,52,52,52,52,52,-43,-49,52,-44,-50,52,-45,-51,]),'STR':([30,32,44,45,46,47,48,58,64,66,67,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,109,111,114,116,118,119,127,139,148,149,150,151,152,153,154,156,161,174,175,176,181,182,183,184,190,191,192,193,196,197,],[53,53,53,53,53,53,53,53,53,53,-57,-58,-59,-60,-61,-62,53,53,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,53,53,53,53,53,-42,-39,-40,53,53,-37,-38,-41,53,53,53,53,53,-46,53,53,53,53,53,-43,-49,53,-44,-50,53,-45,-51,]),'.':([38,49,50,51,52,53,92,99,100,133,135,136,157,158,],[-103,101,-102,-104,-105,-106,-103,-98,-99,-96,-100,-101,-95,-97,]),'RARROW':([38,49,50,51,52,53,92,99,100,133,135,136,157,158,],[-103,102,-102,-104,-105,-106,-103,-98,-99,-96,-100,-101,-95,-97,]),'*':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,78,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'/':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,79,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LOGAND':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,80,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LOGOR':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,81,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LOGEQ':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,82,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LOGNEQ':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,83,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LSHIFT':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,84,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'RSHIFT':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,85,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'<':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,86,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'>':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,87,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'LEQ':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,88,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'GEQ':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,89,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'^':([38,43,49,50,51,52,53,91,92,93,94,95,96,99,100,133,135,136,157,158,],[-103,90,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-96,-100,-101,-95,-97,]),'?':([38,41,43,49,50,51,52,53,91,92,93,94,95,96,99,100,131,133,135,136,157,158,],[-103,74,-73,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,-72,-96,-100,-101,-95,-97,]),'}':([38,41,42,43,49,50,51,52,53,59,60,64,91,92,93,94,95,96,99,100,104,105,107,109,111,112,114,116,118,119,129,131,133,135,136,140,141,143,144,145,147,148,149,150,153,157,158,159,161,164,170,175,176,179,180,183,184,190,191,192,193,194,195,196,197,],[-103,-69,-70,-73,-94,-102,-104,-105,-106,106,-26,113,-89,-103,-90,-91,-92,-93,-98,-99,138,-68,-25,142,-114,146,-36,-42,-39,-40,-56,-72,-96,-100,-101,-27,160,161,-47,-48,-35,-37,-38,-41,-114,-95,-97,-67,-46,173,-71,-114,-114,183,184,-43,-49,-114,-44,-50,-114,196,197,-45,-51,]),'MULTEQ':([38,],[68,]),'ADDEQ':([38,],[69,]),'SUBEQ':([38,],[70,]),'MODEQ':([38,],[71,]),'DIVEQ':([38,],[72,]),':':([43,49,50,51,52,53,91,92,93,94,95,96,99,100,130,131,133,135,136,157,158,],[-73,-94,-102,-104,-105,-106,-89,-103,-90,-91,-92,-93,-98,-99,156,-72,-96,-100,-101,-95,-97,]),'IF':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,187,190,191,192,193,196,197,],[121,121,121,121,-42,-39,-40,-37,-38,-41,121,-46,121,121,-43,-49,121,121,-44,-50,121,-45,-51,]),'WHILE':([64,109,111,114,116,118,119,148,149,150,153,161,173,175,176,183,184,190,191,192,193,196,197,],[122,122,122,122,-42,-39,-40,-37,-38,-41,122,-46,177,122,122,-43,-49,122,-44,-50,122,-45,-51,]),'DO':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,190,191,192,193,196,197,],[123,123,123,123,-42,-39,-40,-37,-38,-41,123,-46,123,123,-43,-49,123,-44,-50,123,-45,-51,]),'FOR':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,190,191,192,193,196,197,],[124,124,124,124,-42,-39,-40,-37,-38,-41,124,-46,124,124,-43,-49,124,-44,-50,124,-45,-51,]),'BREAK':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,190,191,192,193,196,197,],[125,125,125,125,-42,-39,-40,-37,-38,-41,125,-46,125,125,-43,-49,125,-44,-50,125,-45,-51,]),'CONTINUE':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,190,191,192,193,196,197,],[126,126,126,126,-42,-39,-40,-37,-38,-41,126,-46,126,126,-43,-49,126,-44,-50,126,-45,-51,]),'RETURN':([64,109,111,114,116,118,119,148,149,150,153,161,175,176,183,184,190,191,192,193,196,197,],[127,127,127,127,-42,-39,-40,-37,-38,-41,127,-46,127,127,-43,-49,127,-44,-50,127,-45,-51,]),'ELSE':([183,],[187,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,],[1,21,22,]),'include':([0,2,3,],[2,2,2,]),'external_decl':([0,2,3,],[3,3,3,]),'decl':([0,2,3,64,109,111,114,153,175,176,190,193,],[5,5,5,117,117,117,117,117,117,117,117,117,]),'func_def':([0,2,3,],[7,7,7,]),'usual_dec':([0,2,3,64,109,111,114,153,154,175,176,190,193,],[8,8,8,8,8,8,8,8,167,8,8,8,8,]),'new_type_dec':([0,2,3,64,109,111,114,153,175,176,190,193,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'type':([0,2,3,29,33,60,64,65,109,111,114,153,154,175,176,190,193,],[10,10,10,34,61,61,110,34,110,110,110,110,110,110,110,110,110,]),'new_type':([0,2,3,64,109,111,114,153,175,176,190,193,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'declarators':([10,31,61,110,],[25,54,108,25,]),'declarator_1':([10,31,61,110,],[26,26,26,26,]),'declarator_2':([10,31,34,61,110,],[27,27,62,27,27,]),'params':([29,65,],[35,128,]),'param':([29,65,],[37,37,]),'expression':([30,32,58,64,66,97,98,109,111,114,127,139,151,152,153,154,174,175,176,181,182,190,193,],[40,57,105,115,129,132,105,115,115,115,155,105,162,163,115,168,168,115,115,185,168,115,115,]),'bin_expr':([30,32,58,64,66,74,75,97,98,109,111,114,127,139,151,152,153,154,156,174,175,176,181,182,190,193,],[41,41,41,41,41,130,131,41,41,41,41,41,41,41,41,41,41,41,170,41,41,41,41,41,41,41,]),'assignment_expr':([30,32,58,64,66,97,98,109,111,114,127,139,151,152,153,154,174,175,176,181,182,190,193,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'pre_unary_expr':([30,32,44,45,46,47,48,58,64,66,74,75,97,98,109,111,114,127,139,151,152,153,154,156,174,175,176,181,182,190,193,],[43,43,91,93,94,95,96,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'post_unary_expr':([30,32,44,45,46,47,48,58,64,66,74,75,97,98,109,111,114,127,139,151,152,153,154,156,174,175,176,181,182,190,193,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'element':([30,32,44,45,46,47,48,58,64,66,74,75,97,98,109,111,114,127,139,151,152,153,154,156,174,175,176,181,182,190,193,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'initializer':([32,],[56,]),'new_type_params':([33,60,],[59,107,]),'new_type_param':([33,60,],[60,60,]),'assignmenteq_op':([38,],[66,]),'bin_op':([43,],[75,]),'expressions':([58,98,139,],[104,134,159,]),'statements':([64,109,111,114,153,175,176,190,193,],[112,141,144,147,144,144,144,144,144,]),'statement':([64,109,111,114,153,175,176,190,193,],[114,114,114,114,114,114,114,114,114,]),'conditional':([64,109,111,114,153,175,176,187,190,193,],[118,118,118,118,118,118,118,191,118,118,]),'iteration':([64,109,111,114,153,175,176,190,193,],[119,119,119,119,119,119,119,119,119,]),'jump':([64,109,111,114,153,175,176,190,193,],[120,120,120,120,120,120,120,120,120,]),'stats_or_null':([111,153,175,176,190,193,],[143,164,179,180,194,195,]),'empty':([111,153,154,174,175,176,182,190,193,],[145,145,169,169,145,145,169,145,145,]),'expr_or_null_or_init':([154,],[165,]),'expr_or_null':([154,174,182,],[166,178,186,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> include program','program',2,'p_program','parser.py',38),
  ('program -> external_decl program','program',2,'p_program','parser.py',39),
  ('program -> include','program',1,'p_program_end','parser.py',46),
  ('program -> external_decl','program',1,'p_program_end','parser.py',47),
  ('include -> INCLUDE','include',1,'p_include','parser.py',58),
  ('external_decl -> decl ;','external_decl',2,'p_external_declaration','parser.py',67),
  ('external_decl -> func_def','external_decl',1,'p_external_declaration','parser.py',68),
  ('external_decl -> ;','external_decl',1,'p_external_declaration_extra_semicolon','parser.py',75),
  ('decl -> usual_dec','decl',1,'p_decl','parser.py',82),
  ('decl -> new_type_dec','decl',1,'p_decl','parser.py',83),
  ('usual_dec -> type declarators','usual_dec',2,'p_usual_decl','parser.py',90),
  ('declarators -> declarator_1 , declarators','declarators',3,'p_declarators','parser.py',99),
  ('declarators -> declarator_1','declarators',1,'p_declarator_end','parser.py',106),
  ('declarator_1 -> declarator_2','declarator_1',1,'p_declarator_1','parser.py',113),
  ('declarator_1 -> declarator_2 = initializer','declarator_1',3,'p_declarator_1_winit','parser.py',120),
  ('declarator_2 -> ID','declarator_2',1,'p_declarator_2_single','parser.py',127),
  ('declarator_2 -> ID ( )','declarator_2',3,'p_declarator_2_func','parser.py',134),
  ('declarator_2 -> ID [ ]','declarator_2',3,'p_declarator_2_array','parser.py',141),
  ('declarator_2 -> ID [ expression ]','declarator_2',4,'p_declarator_2_arrray','parser.py',148),
  ('initializer -> expression','initializer',1,'p_initializer','parser.py',155),
  ('initializer -> { expressions }','initializer',3,'p_initializer','parser.py',156),
  ('new_type_dec -> new_type ID { new_type_params }','new_type_dec',5,'p_new_type_dec','parser.py',171),
  ('new_type -> STRUCT','new_type',1,'p_new_type','parser.py',178),
  ('new_type -> CLASS','new_type',1,'p_new_type','parser.py',179),
  ('new_type_params -> new_type_param new_type_params','new_type_params',2,'p_new_type_params','parser.py',186),
  ('new_type_params -> new_type_param','new_type_params',1,'p_new_type_params_end','parser.py',193),
  ('new_type_param -> type declarators ;','new_type_param',3,'p_new_type_param','parser.py',200),
  ('func_def -> type ID ( params ) { statements }','func_def',8,'p_function_definition','parser.py',209),
  ('func_def -> type ID ( ) { statements }','func_def',7,'p_function_defintion_noparam','parser.py',216),
  ('func_def -> type ID ( params ) { }','func_def',7,'p_function_defintion_nostatement','parser.py',223),
  ('func_def -> type ID ( ) { }','func_def',6,'p_function_definition_nothing','parser.py',230),
  ('params -> param , params','params',3,'p_params','parser.py',237),
  ('params -> param','params',1,'p_params_end','parser.py',244),
  ('param -> type declarator_2','param',2,'p_param','parser.py',251),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',260),
  ('statements -> statement','statements',1,'p_statements_end','parser.py',270),
  ('statement -> expression ;','statement',2,'p_statement','parser.py',277),
  ('statement -> decl ;','statement',2,'p_statement','parser.py',278),
  ('statement -> conditional','statement',1,'p_statement','parser.py',279),
  ('statement -> iteration','statement',1,'p_statement','parser.py',280),
  ('statement -> jump ;','statement',2,'p_statement','parser.py',281),
  ('statement -> ;','statement',1,'p_statement_extra_semicolon','parser.py',288),
  ('conditional -> IF ( expression ) { stats_or_null }','conditional',7,'p_conditional','parser.py',297),
  ('conditional -> IF ( expression ) { stats_or_null } ELSE conditional','conditional',9,'p_conditional_elseif','parser.py',304),
  ('conditional -> IF ( expression ) { stats_or_null } ELSE { stats_or_null }','conditional',11,'p_conditional_else','parser.py',311),
  ('statement -> { stats_or_null }','statement',3,'p_block','parser.py',320),
  ('stats_or_null -> statements','stats_or_null',1,'p_statement_or_null','parser.py',327),
  ('stats_or_null -> empty','stats_or_null',1,'p_statement_or_null','parser.py',328),
  ('iteration -> WHILE ( expression ) { stats_or_null }','iteration',7,'p_iteration','parser.py',338),
  ('iteration -> DO { stats_or_null } WHILE ( expression ) ;','iteration',9,'p_iteration_do_while','parser.py',345),
  ('iteration -> FOR ( expr_or_null_or_init ; expr_or_null ; expr_or_null ) { stats_or_null }','iteration',11,'p_iteration_for','parser.py',352),
  ('expr_or_null -> expression','expr_or_null',1,'p_expr_or_null','parser.py',359),
  ('expr_or_null -> empty','expr_or_null',1,'p_expr_or_null','parser.py',360),
  ('expr_or_null_or_init -> expr_or_null','expr_or_null_or_init',1,'p_expr_or_null_or_init','parser.py',367),
  ('expr_or_null_or_init -> usual_dec','expr_or_null_or_init',1,'p_expr_or_null_or_init','parser.py',368),
  ('assignment_expr -> ID assignmenteq_op expression','assignment_expr',3,'p_assignment_expr','parser.py',375),
  ('assignmenteq_op -> =','assignmenteq_op',1,'p_assignment_op','parser.py',383),
  ('assignmenteq_op -> MULTEQ','assignmenteq_op',1,'p_assignment_op','parser.py',384),
  ('assignmenteq_op -> ADDEQ','assignmenteq_op',1,'p_assignment_op','parser.py',385),
  ('assignmenteq_op -> SUBEQ','assignmenteq_op',1,'p_assignment_op','parser.py',386),
  ('assignmenteq_op -> MODEQ','assignmenteq_op',1,'p_assignment_op','parser.py',387),
  ('assignmenteq_op -> DIVEQ','assignmenteq_op',1,'p_assignment_op','parser.py',388),
  ('jump -> BREAK','jump',1,'p_jump','parser.py',395),
  ('jump -> CONTINUE','jump',1,'p_jump','parser.py',396),
  ('jump -> RETURN','jump',1,'p_jump','parser.py',397),
  ('jump -> RETURN expression','jump',2,'p_jump_wvalue','parser.py',404),
  ('expressions -> expression , expressions','expressions',3,'p_expressions','parser.py',415),
  ('expressions -> expression','expressions',1,'p_expressions_end','parser.py',422),
  ('expression -> bin_expr','expression',1,'p_expression','parser.py',429),
  ('expression -> assignment_expr','expression',1,'p_expression','parser.py',430),
  ('expression -> bin_expr ? bin_expr : bin_expr','expression',5,'p_expression_wternary','parser.py',437),
  ('bin_expr -> pre_unary_expr bin_op bin_expr','bin_expr',3,'p_binary_expr','parser.py',444),
  ('bin_expr -> pre_unary_expr','bin_expr',1,'p_binary_to_unary','parser.py',451),
  ('bin_op -> +','bin_op',1,'p_binary_operator','parser.py',458),
  ('bin_op -> -','bin_op',1,'p_binary_operator','parser.py',459),
  ('bin_op -> *','bin_op',1,'p_binary_operator','parser.py',460),
  ('bin_op -> /','bin_op',1,'p_binary_operator','parser.py',461),
  ('bin_op -> LOGAND','bin_op',1,'p_binary_operator','parser.py',462),
  ('bin_op -> LOGOR','bin_op',1,'p_binary_operator','parser.py',463),
  ('bin_op -> LOGEQ','bin_op',1,'p_binary_operator','parser.py',464),
  ('bin_op -> LOGNEQ','bin_op',1,'p_binary_operator','parser.py',465),
  ('bin_op -> LSHIFT','bin_op',1,'p_binary_operator','parser.py',466),
  ('bin_op -> RSHIFT','bin_op',1,'p_binary_operator','parser.py',467),
  ('bin_op -> <','bin_op',1,'p_binary_operator','parser.py',468),
  ('bin_op -> >','bin_op',1,'p_binary_operator','parser.py',469),
  ('bin_op -> LEQ','bin_op',1,'p_binary_operator','parser.py',470),
  ('bin_op -> GEQ','bin_op',1,'p_binary_operator','parser.py',471),
  ('bin_op -> ^','bin_op',1,'p_binary_operator','parser.py',472),
  ('pre_unary_expr -> PLUSPLUS pre_unary_expr','pre_unary_expr',2,'p_pre_unary_expr','parser.py',479),
  ('pre_unary_expr -> MINUSMINUS pre_unary_expr','pre_unary_expr',2,'p_pre_unary_expr','parser.py',480),
  ('pre_unary_expr -> + pre_unary_expr','pre_unary_expr',2,'p_pre_unary_expr','parser.py',481),
  ('pre_unary_expr -> - pre_unary_expr','pre_unary_expr',2,'p_pre_unary_expr','parser.py',482),
  ('pre_unary_expr -> ! pre_unary_expr','pre_unary_expr',2,'p_pre_unary_expr','parser.py',483),
  ('pre_unary_expr -> post_unary_expr','pre_unary_expr',1,'p_pre_unary_to_post','parser.py',490),
  ('post_unary_expr -> post_unary_expr [ expression ]','post_unary_expr',4,'p_post_unary_expr_array','parser.py',497),
  ('post_unary_expr -> post_unary_expr ( )','post_unary_expr',3,'p_post_unary_fncall_empty','parser.py',504),
  ('post_unary_expr -> post_unary_expr ( expressions )','post_unary_expr',4,'p_post_unary_fncall','parser.py',511),
  ('post_unary_expr -> post_unary_expr PLUSPLUS','post_unary_expr',2,'p_post_unary_ppmm','parser.py',518),
  ('post_unary_expr -> post_unary_expr MINUSMINUS','post_unary_expr',2,'p_post_unary_ppmm','parser.py',519),
  ('post_unary_expr -> post_unary_expr . ID','post_unary_expr',3,'p_post_unary_access_member','parser.py',526),
  ('post_unary_expr -> post_unary_expr RARROW ID','post_unary_expr',3,'p_post_unary_access_member','parser.py',527),
  ('post_unary_expr -> element','post_unary_expr',1,'p_post_unary_to_element','parser.py',534),
  ('element -> ID','element',1,'p_element','parser.py',541),
  ('element -> NUMBER','element',1,'p_element_const','parser.py',548),
  ('element -> CHR','element',1,'p_element_const','parser.py',549),
  ('element -> STR','element',1,'p_element_const','parser.py',550),
  ('type -> VOID','type',1,'p_type','parser.py',559),
  ('type -> CHAR','type',1,'p_type','parser.py',560),
  ('type -> SHORT','type',1,'p_type','parser.py',561),
  ('type -> INT','type',1,'p_type','parser.py',562),
  ('type -> LONG','type',1,'p_type','parser.py',563),
  ('type -> FLOAT','type',1,'p_type','parser.py',564),
  ('type -> DOUBLE','type',1,'p_type','parser.py',565),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',572),
]
