
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BOOLEAN CHAR COMMA DIVIDE ELSE EQ FLOAT FOR GE GT ID IF INT LBRACE LBRACKET LE LPAREN LT MAIN MINUS MOD NE NUMBER PLUS PRINTF RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOID WHILEprogram : declaration_listdeclaration_list : declaration_list declaration\n                        | declarationdeclaration : var_declaration\n                   | fun_declarationvar_declaration : type_specifier ID SEMICOLON\n                       | type_specifier ID ASSIGN expression SEMICOLONtype_specifier : INT\n                      | FLOAT\n                      | CHAR\n                      | BOOLEAN\n                      | VOIDfun_declaration : type_specifier ID LPAREN params RPAREN compound_stmtparams : param_list\n              | VOIDparam_list : param_list COMMA param\n                  | paramparam : type_specifier IDcompound_stmt : LBRACE local_declarations statement_list RBRACElocal_declarations : local_declarations var_declaration\n                          | emptystatement_list : statement_list statement\n                      | emptystatement : expression_stmt\n                 | compound_stmt\n                 | selection_stmt\n                 | iteration_stmt\n                 | return_stmt\n                 | print_stmtexpression_stmt : expression SEMICOLON\n                       | SEMICOLONselection_stmt : IF LPAREN expression RPAREN statement ELSE statement\n                      | IF LPAREN expression RPAREN statementiteration_stmt : WHILE LPAREN expression RPAREN statement\n                      | FOR LPAREN expression_stmt expression_stmt expression RPAREN statementreturn_stmt : RETURN SEMICOLON\n                   | RETURN expression SEMICOLONprint_stmt : PRINTF LPAREN STRING RPAREN SEMICOLON\n                  | PRINTF LPAREN expression RPAREN SEMICOLONexpression : var ASSIGN expression\n                  | simple_expressionvar : ID\n           | ID LBRACKET expression RBRACKETsimple_expression : additive_expression relop additive_expression\n                         | additive_expressionrelop : LE\n             | LT\n             | GE\n             | GT\n             | EQ\n             | NEadditive_expression : additive_expression addop term\n                           | termaddop : PLUS\n             | MINUSterm : term mulop factor\n            | factormulop : TIMES\n             | DIVIDE\n             | MODfactor : LPAREN expression RPAREN\n              | var\n              | call\n              | NUMBER\n              | FLOAT\n              | CHAR\n              | STRINGcall : ID LPAREN args RPARENargs : arg_list\n            | emptyarg_list : arg_list COMMA expression\n                | expressionempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,12,14,16,37,56,68,69,74,75,78,81,],[7,7,-3,-4,-5,-2,-6,7,-7,7,-13,-73,7,-21,-20,-19,]),'FLOAT':([0,2,3,4,5,12,14,15,16,24,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,68,69,73,74,75,77,78,79,81,82,83,84,85,86,87,88,90,94,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[8,8,-3,-4,-5,-2,-6,27,8,27,27,27,-7,27,27,27,-46,-47,-48,-49,-50,-51,-54,-55,27,-58,-59,-60,8,-13,-73,27,8,-21,27,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,27,-30,27,27,27,-36,27,27,-37,27,27,27,-33,-34,-38,-39,27,27,-32,-35,]),'CHAR':([0,2,3,4,5,12,14,15,16,24,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,68,69,73,74,75,77,78,79,81,82,83,84,85,86,87,88,90,94,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[9,9,-3,-4,-5,-2,-6,28,9,28,28,28,-7,28,28,28,-46,-47,-48,-49,-50,-51,-54,-55,28,-58,-59,-60,9,-13,-73,28,9,-21,28,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,28,-30,28,28,28,-36,28,28,-37,28,28,28,-33,-34,-38,-39,28,28,-32,-35,]),'BOOLEAN':([0,2,3,4,5,12,14,16,37,56,68,69,74,75,78,81,],[10,10,-3,-4,-5,-2,-6,10,-7,10,-13,-73,10,-21,-20,-19,]),'VOID':([0,2,3,4,5,12,14,16,37,56,68,69,74,75,78,81,],[11,11,-3,-4,-5,-2,-6,33,-7,11,-13,-73,11,-21,-20,-19,]),'$end':([1,2,3,4,5,12,14,37,68,81,],[0,-1,-3,-4,-5,-2,-6,-7,-13,-19,]),'ID':([6,7,8,9,10,11,14,15,24,30,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,69,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,90,94,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[13,-8,-9,-10,-11,-12,-6,17,17,54,-12,17,17,-7,17,17,17,-46,-47,-48,-49,-50,-51,-54,-55,17,-58,-59,-60,-73,17,-73,-21,17,-20,-23,96,-19,-22,-24,-25,-26,-27,-28,-29,-31,17,-30,17,17,17,-36,17,17,-37,17,17,17,-33,-34,-38,-39,17,17,-32,-35,]),'SEMICOLON':([13,14,17,18,19,20,21,22,23,25,26,27,28,29,37,62,63,64,65,66,67,69,71,72,74,75,77,78,79,81,82,83,84,85,86,87,88,89,90,94,96,97,100,101,102,106,107,110,111,113,114,115,116,118,119,120,121,122,123,],[14,-6,-42,37,-62,-41,-45,-53,-57,-63,-64,-65,-66,-67,-7,-40,-44,-62,-52,-56,-61,-73,-43,-68,-73,-21,90,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,97,-31,101,14,-30,90,-36,107,90,-37,90,90,118,119,-33,-34,-38,-39,90,90,-32,-35,]),'ASSIGN':([13,17,19,71,96,],[15,-42,38,-43,15,]),'LPAREN':([13,14,15,17,24,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,69,73,74,75,77,78,79,81,82,83,84,85,86,87,88,90,91,92,93,94,95,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[16,-6,24,36,24,24,24,-7,24,24,24,-46,-47,-48,-49,-50,-51,-54,-55,24,-58,-59,-60,-73,24,-73,-21,24,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,98,99,100,24,103,-30,24,24,24,-36,24,24,-37,24,24,24,-33,-34,-38,-39,24,24,-32,-35,]),'RBRACE':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,115,116,118,119,122,123,],[-6,-7,-73,-73,-21,81,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,-33,-34,-38,-39,-32,-35,]),'LBRACE':([14,37,55,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,69,-73,-73,-21,69,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,69,69,-33,-34,-38,-39,69,69,-32,-35,]),'IF':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,-73,-73,-21,91,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,91,91,-33,-34,-38,-39,91,91,-32,-35,]),'WHILE':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,-73,-73,-21,92,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,92,92,-33,-34,-38,-39,92,92,-32,-35,]),'FOR':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,-73,-73,-21,93,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,93,93,-33,-34,-38,-39,93,93,-32,-35,]),'RETURN':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,-73,-73,-21,94,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,94,94,-33,-34,-38,-39,94,94,-32,-35,]),'PRINTF':([14,37,69,74,75,77,78,79,81,82,83,84,85,86,87,88,90,97,101,107,110,111,115,116,118,119,120,121,122,123,],[-6,-7,-73,-73,-21,95,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,95,95,-33,-34,-38,-39,95,95,-32,-35,]),'NUMBER':([14,15,24,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,69,73,74,75,77,78,79,81,82,83,84,85,86,87,88,90,94,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[-6,26,26,26,26,-7,26,26,26,-46,-47,-48,-49,-50,-51,-54,-55,26,-58,-59,-60,-73,26,-73,-21,26,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,26,-30,26,26,26,-36,26,26,-37,26,26,26,-33,-34,-38,-39,26,26,-32,-35,]),'STRING':([14,15,24,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,69,73,74,75,77,78,79,81,82,83,84,85,86,87,88,90,94,97,98,99,100,101,103,106,107,110,111,112,115,116,118,119,120,121,122,123,],[-6,29,29,29,29,-7,29,29,29,-46,-47,-48,-49,-50,-51,-54,-55,29,-58,-59,-60,-73,29,-73,-21,29,-20,-23,-19,-22,-24,-25,-26,-27,-28,-29,-31,29,-30,29,29,29,-36,108,29,-37,29,29,29,-33,-34,-38,-39,29,29,-32,-35,]),'TIMES':([17,19,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,50,-57,-63,-64,-65,-66,-67,-62,50,-56,-61,-43,-68,-67,]),'DIVIDE':([17,19,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,51,-57,-63,-64,-65,-66,-67,-62,51,-56,-61,-43,-68,-67,]),'MOD':([17,19,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,52,-57,-63,-64,-65,-66,-67,-62,52,-56,-61,-43,-68,-67,]),'LE':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,41,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'LT':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,42,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'GE':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,43,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'GT':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,44,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'EQ':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,45,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'NE':([17,19,21,22,23,25,26,27,28,29,64,65,66,67,71,72,108,],[-42,-62,46,-53,-57,-63,-64,-65,-66,-67,-62,-52,-56,-61,-43,-68,-67,]),'PLUS':([17,19,21,22,23,25,26,27,28,29,63,64,65,66,67,71,72,108,],[-42,-62,47,-53,-57,-63,-64,-65,-66,-67,47,-62,-52,-56,-61,-43,-68,-67,]),'MINUS':([17,19,21,22,23,25,26,27,28,29,63,64,65,66,67,71,72,108,],[-42,-62,48,-53,-57,-63,-64,-65,-66,-67,48,-62,-52,-56,-61,-43,-68,-67,]),'RPAREN':([17,19,20,21,22,23,25,26,27,28,29,31,32,33,34,36,53,54,58,59,60,61,62,63,64,65,66,67,70,71,72,76,104,105,108,109,117,],[-42,-62,-41,-45,-53,-57,-63,-64,-65,-66,-67,55,-14,-15,-17,-73,67,-18,72,-69,-70,-72,-40,-44,-62,-52,-56,-61,-16,-43,-68,-71,110,111,113,114,121,]),'RBRACKET':([17,19,20,21,22,23,25,26,27,28,29,57,62,63,64,65,66,67,71,72,],[-42,-62,-41,-45,-53,-57,-63,-64,-65,-66,-67,71,-40,-44,-62,-52,-56,-61,-43,-68,]),'COMMA':([17,19,20,21,22,23,25,26,27,28,29,32,34,54,59,61,62,63,64,65,66,67,70,71,72,76,],[-42,-62,-41,-45,-53,-57,-63,-64,-65,-66,-67,56,-17,-18,73,-72,-40,-44,-62,-52,-56,-61,-16,-43,-68,-71,]),'LBRACKET':([17,],[35,]),'ELSE':([81,83,84,85,86,87,88,90,97,101,107,115,116,118,119,122,123,],[-19,-24,-25,-26,-27,-28,-29,-31,-30,-36,-37,120,-34,-38,-39,-32,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,12,]),'var_declaration':([0,2,74,],[4,4,78,]),'fun_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,16,56,74,],[6,6,30,30,80,]),'expression':([15,24,35,36,38,73,77,94,98,99,100,103,106,110,111,112,120,121,],[18,53,57,61,62,76,89,102,104,105,89,109,89,89,89,117,89,89,]),'var':([15,24,35,36,38,39,40,49,73,77,94,98,99,100,103,106,110,111,112,120,121,],[19,19,19,19,19,64,64,64,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'simple_expression':([15,24,35,36,38,73,77,94,98,99,100,103,106,110,111,112,120,121,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'additive_expression':([15,24,35,36,38,39,73,77,94,98,99,100,103,106,110,111,112,120,121,],[21,21,21,21,21,63,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'term':([15,24,35,36,38,39,40,73,77,94,98,99,100,103,106,110,111,112,120,121,],[22,22,22,22,22,22,65,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'factor':([15,24,35,36,38,39,40,49,73,77,94,98,99,100,103,106,110,111,112,120,121,],[23,23,23,23,23,23,23,66,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'call':([15,24,35,36,38,39,40,49,73,77,94,98,99,100,103,106,110,111,112,120,121,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'params':([16,],[31,]),'param_list':([16,],[32,]),'param':([16,56,],[34,70,]),'relop':([21,],[39,]),'addop':([21,63,],[40,40,]),'mulop':([22,65,],[49,49,]),'args':([36,],[58,]),'arg_list':([36,],[59,]),'empty':([36,69,74,],[60,75,79,]),'compound_stmt':([55,77,110,111,120,121,],[68,84,84,84,84,84,]),'local_declarations':([69,],[74,]),'statement_list':([74,],[77,]),'statement':([77,110,111,120,121,],[82,115,116,122,123,]),'expression_stmt':([77,100,106,110,111,120,121,],[83,106,112,83,83,83,83,]),'selection_stmt':([77,110,111,120,121,],[85,85,85,85,85,]),'iteration_stmt':([77,110,111,120,121,],[86,86,86,86,86,]),'return_stmt':([77,110,111,120,121,],[87,87,87,87,87,]),'print_stmt':([77,110,111,120,121,],[88,88,88,88,88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','parser.py',7),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',11),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parser.py',12),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',16),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','parser.py',17),
  ('var_declaration -> type_specifier ID SEMICOLON','var_declaration',3,'p_var_declaration','parser.py',21),
  ('var_declaration -> type_specifier ID ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration','parser.py',22),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',26),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','parser.py',27),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier','parser.py',28),
  ('type_specifier -> BOOLEAN','type_specifier',1,'p_type_specifier','parser.py',29),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','parser.py',30),
  ('fun_declaration -> type_specifier ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','parser.py',34),
  ('params -> param_list','params',1,'p_params','parser.py',38),
  ('params -> VOID','params',1,'p_params','parser.py',39),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',43),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',44),
  ('param -> type_specifier ID','param',2,'p_param','parser.py',48),
  ('compound_stmt -> LBRACE local_declarations statement_list RBRACE','compound_stmt',4,'p_compound_stmt','parser.py',52),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations','parser.py',56),
  ('local_declarations -> empty','local_declarations',1,'p_local_declarations','parser.py',57),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',61),
  ('statement_list -> empty','statement_list',1,'p_statement_list','parser.py',62),
  ('statement -> expression_stmt','statement',1,'p_statement','parser.py',66),
  ('statement -> compound_stmt','statement',1,'p_statement','parser.py',67),
  ('statement -> selection_stmt','statement',1,'p_statement','parser.py',68),
  ('statement -> iteration_stmt','statement',1,'p_statement','parser.py',69),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',70),
  ('statement -> print_stmt','statement',1,'p_statement','parser.py',71),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt','parser.py',75),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt','parser.py',76),
  ('selection_stmt -> IF LPAREN expression RPAREN statement ELSE statement','selection_stmt',7,'p_selection_stmt','parser.py',80),
  ('selection_stmt -> IF LPAREN expression RPAREN statement','selection_stmt',5,'p_selection_stmt','parser.py',81),
  ('iteration_stmt -> WHILE LPAREN expression RPAREN statement','iteration_stmt',5,'p_iteration_stmt','parser.py',85),
  ('iteration_stmt -> FOR LPAREN expression_stmt expression_stmt expression RPAREN statement','iteration_stmt',7,'p_iteration_stmt','parser.py',86),
  ('return_stmt -> RETURN SEMICOLON','return_stmt',2,'p_return_stmt','parser.py',90),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt','parser.py',91),
  ('print_stmt -> PRINTF LPAREN STRING RPAREN SEMICOLON','print_stmt',5,'p_print_stmt','parser.py',95),
  ('print_stmt -> PRINTF LPAREN expression RPAREN SEMICOLON','print_stmt',5,'p_print_stmt','parser.py',96),
  ('expression -> var ASSIGN expression','expression',3,'p_expression','parser.py',100),
  ('expression -> simple_expression','expression',1,'p_expression','parser.py',101),
  ('var -> ID','var',1,'p_var','parser.py',105),
  ('var -> ID LBRACKET expression RBRACKET','var',4,'p_var','parser.py',106),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression','parser.py',110),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression','parser.py',111),
  ('relop -> LE','relop',1,'p_relop','parser.py',115),
  ('relop -> LT','relop',1,'p_relop','parser.py',116),
  ('relop -> GE','relop',1,'p_relop','parser.py',117),
  ('relop -> GT','relop',1,'p_relop','parser.py',118),
  ('relop -> EQ','relop',1,'p_relop','parser.py',119),
  ('relop -> NE','relop',1,'p_relop','parser.py',120),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression','parser.py',124),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression','parser.py',125),
  ('addop -> PLUS','addop',1,'p_addop','parser.py',129),
  ('addop -> MINUS','addop',1,'p_addop','parser.py',130),
  ('term -> term mulop factor','term',3,'p_term','parser.py',134),
  ('term -> factor','term',1,'p_term','parser.py',135),
  ('mulop -> TIMES','mulop',1,'p_mulop','parser.py',139),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','parser.py',140),
  ('mulop -> MOD','mulop',1,'p_mulop','parser.py',141),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',145),
  ('factor -> var','factor',1,'p_factor','parser.py',146),
  ('factor -> call','factor',1,'p_factor','parser.py',147),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',148),
  ('factor -> FLOAT','factor',1,'p_factor','parser.py',149),
  ('factor -> CHAR','factor',1,'p_factor','parser.py',150),
  ('factor -> STRING','factor',1,'p_factor','parser.py',151),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','parser.py',155),
  ('args -> arg_list','args',1,'p_args','parser.py',159),
  ('args -> empty','args',1,'p_args','parser.py',160),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','parser.py',164),
  ('arg_list -> expression','arg_list',1,'p_arg_list','parser.py',165),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',169),
]
