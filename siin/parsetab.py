
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ANDAND ANDANDEQUAL BOOLEAN COMMA COMMENT DIVEQUAL DIVIDE DOT ELSE EQUALEQUAL EQUALS FLOAT FOR GREATER GREATEREQUAL ID IF INT KEYWORD LBRACE LBRACKET LESS LESSEQUAL LPAREN MINUS MINUSEQUAL MINUSMINUS MODEQUAL MODULO MULTICOMMENT NOT NOTEQUAL OROR OROREQUAL PLUS PLUSEQUAL PLUSPLUS RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING STRUCT TIMES TIMESEQUAL TYPE WHILEprogram : declaration_list\n    declaration_list : declaration_list declaration\n                     | declaration\n    \n    declaration : var_declaration\n                | fun_declaration\n                | struct_declaration\n                | control_structure\n                | comment\n    \n    var_declaration : TYPE ID SEMICOLON\n                    | TYPE ID EQUALS expression SEMICOLON\n    \n    fun_declaration : TYPE ID LPAREN params RPAREN block\n    \n    params : param_list\n           | empty\n    \n    param_list : param_list COMMA param\n               | param\n    param : TYPE IDblock : LBRACE declaration_list RBRACE\n    comment : COMMENT\n            | MULTICOMMENT\n    \n    expression : assignment_expression\n               | simple_expression\n    \n    assignment_expression : ID EQUALS expression\n                          | ID PLUSEQUAL expression\n                          | ID MINUSEQUAL expression\n                          | ID TIMESEQUAL expression\n                          | ID DIVEQUAL expression\n                          | ID MODEQUAL expression\n    \n    simple_expression : additive_expression\n    \n    additive_expression : additive_expression PLUS term\n                        | additive_expression MINUS term\n                        | term\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n         | factor\n    \n    factor : LPAREN expression RPAREN\n           | ID\n           | INT\n           | FLOAT\n           | STRING\n    \n    control_structure : IF LPAREN expression RPAREN block\n                      | IF LPAREN expression RPAREN block ELSE block\n                      | WHILE LPAREN expression RPAREN block\n                      | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN block\n                      | RETURN expression SEMICOLON\n    struct_declaration : STRUCT ID LBRACE var_declaration_list RBRACE\n    var_declaration_list : var_declaration_list var_declaration\n                         | var_declaration\n    empty :'
    
_lr_action_items = {'TYPE':([0,2,3,4,5,6,7,8,15,16,17,34,36,37,41,59,60,77,80,81,82,84,85,86,88,91,93,94,97,],[9,9,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,54,61,-44,61,-47,-10,54,-45,-46,-40,9,-42,-11,9,-41,-17,-43,]),'STRUCT':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[10,10,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,10,-42,-11,10,-41,-17,-43,]),'IF':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[11,11,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,11,-42,-11,11,-41,-17,-43,]),'WHILE':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[12,12,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,12,-42,-11,12,-41,-17,-43,]),'FOR':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[13,13,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,13,-42,-11,13,-41,-17,-43,]),'RETURN':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[14,14,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,14,-42,-11,14,-41,-17,-43,]),'COMMENT':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[15,15,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,15,-42,-11,15,-41,-17,-43,]),'MULTICOMMENT':([0,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,85,86,88,91,93,94,97,],[16,16,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,16,-42,-11,16,-41,-17,-43,]),'$end':([1,2,3,4,5,6,7,8,15,16,17,34,41,77,81,84,86,88,93,94,97,],[0,-1,-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,-10,-45,-40,-42,-11,-41,-17,-43,]),'RBRACE':([3,4,5,6,7,8,15,16,17,34,41,59,60,77,81,82,84,86,88,91,93,94,97,],[-3,-4,-5,-6,-7,-8,-18,-19,-2,-9,-44,81,-47,-10,-45,-46,-40,-42,-11,94,-41,-17,-43,]),'ID':([9,10,14,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,54,61,64,92,],[18,19,26,26,26,26,26,26,26,26,26,26,26,26,72,72,72,72,78,83,26,26,]),'LPAREN':([11,12,13,14,18,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,64,92,],[20,21,22,30,36,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'INT':([14,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,64,92,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FLOAT':([14,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,64,92,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'STRING':([14,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,64,92,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'SEMICOLON':([18,23,24,25,26,27,28,29,31,32,33,40,53,65,66,67,68,69,70,71,72,73,74,75,76,83,87,],[34,41,-20,-21,-36,-28,-31,-34,-37,-38,-39,64,77,-22,-23,-24,-25,-26,-27,-29,-36,-30,-32,-33,-35,34,92,]),'EQUALS':([18,26,83,],[35,42,35,]),'LBRACE':([19,62,63,79,90,96,],[37,85,85,85,85,85,]),'RPAREN':([24,25,26,27,28,29,31,32,33,36,38,39,52,55,56,57,58,65,66,67,68,69,70,71,72,73,74,75,76,78,89,95,],[-20,-21,-36,-28,-31,-34,-37,-38,-39,-48,62,63,76,79,-12,-13,-15,-22,-23,-24,-25,-26,-27,-29,-36,-30,-32,-33,-35,-16,-14,96,]),'PLUSEQUAL':([26,],[43,]),'MINUSEQUAL':([26,],[44,]),'TIMESEQUAL':([26,],[45,]),'DIVEQUAL':([26,],[46,]),'MODEQUAL':([26,],[47,]),'TIMES':([26,28,29,31,32,33,71,72,73,74,75,76,],[-36,50,-34,-37,-38,-39,50,-36,50,-32,-33,-35,]),'DIVIDE':([26,28,29,31,32,33,71,72,73,74,75,76,],[-36,51,-34,-37,-38,-39,51,-36,51,-32,-33,-35,]),'PLUS':([26,27,28,29,31,32,33,71,72,73,74,75,76,],[-36,48,-31,-34,-37,-38,-39,-29,-36,-30,-32,-33,-35,]),'MINUS':([26,27,28,29,31,32,33,71,72,73,74,75,76,],[-36,49,-31,-34,-37,-38,-39,-29,-36,-30,-32,-33,-35,]),'COMMA':([56,58,78,89,],[80,-15,-16,-14,]),'ELSE':([84,94,],[90,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,85,],[2,91,]),'declaration':([0,2,85,91,],[3,17,3,17,]),'var_declaration':([0,2,37,59,85,91,],[4,4,60,82,4,4,]),'fun_declaration':([0,2,85,91,],[5,5,5,5,]),'struct_declaration':([0,2,85,91,],[6,6,6,6,]),'control_structure':([0,2,85,91,],[7,7,7,7,]),'comment':([0,2,85,91,],[8,8,8,8,]),'expression':([14,20,21,22,30,35,42,43,44,45,46,47,64,92,],[23,38,39,40,52,53,65,66,67,68,69,70,87,95,]),'assignment_expression':([14,20,21,22,30,35,42,43,44,45,46,47,64,92,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'simple_expression':([14,20,21,22,30,35,42,43,44,45,46,47,64,92,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'additive_expression':([14,20,21,22,30,35,42,43,44,45,46,47,64,92,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'term':([14,20,21,22,30,35,42,43,44,45,46,47,48,49,64,92,],[28,28,28,28,28,28,28,28,28,28,28,28,71,73,28,28,]),'factor':([14,20,21,22,30,35,42,43,44,45,46,47,48,49,50,51,64,92,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,74,75,29,29,]),'params':([36,],[55,]),'param_list':([36,],[56,]),'empty':([36,],[57,]),'param':([36,80,],[58,89,]),'var_declaration_list':([37,],[59,]),'block':([62,63,79,90,96,],[84,86,88,93,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','parsert.py',5),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parsert.py',9),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parsert.py',10),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parsert.py',15),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','parsert.py',16),
  ('declaration -> struct_declaration','declaration',1,'p_declaration','parsert.py',17),
  ('declaration -> control_structure','declaration',1,'p_declaration','parsert.py',18),
  ('declaration -> comment','declaration',1,'p_declaration','parsert.py',19),
  ('var_declaration -> TYPE ID SEMICOLON','var_declaration',3,'p_var_declaration','parsert.py',24),
  ('var_declaration -> TYPE ID EQUALS expression SEMICOLON','var_declaration',5,'p_var_declaration','parsert.py',25),
  ('fun_declaration -> TYPE ID LPAREN params RPAREN block','fun_declaration',6,'p_fun_declaration','parsert.py',30),
  ('params -> param_list','params',1,'p_params','parsert.py',35),
  ('params -> empty','params',1,'p_params','parsert.py',36),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parsert.py',41),
  ('param_list -> param','param_list',1,'p_param_list','parsert.py',42),
  ('param -> TYPE ID','param',2,'p_param','parsert.py',46),
  ('block -> LBRACE declaration_list RBRACE','block',3,'p_block','parsert.py',49),
  ('comment -> COMMENT','comment',1,'p_comment','parsert.py',53),
  ('comment -> MULTICOMMENT','comment',1,'p_comment','parsert.py',54),
  ('expression -> assignment_expression','expression',1,'p_expression','parsert.py',59),
  ('expression -> simple_expression','expression',1,'p_expression','parsert.py',60),
  ('assignment_expression -> ID EQUALS expression','assignment_expression',3,'p_assignment_expression','parsert.py',65),
  ('assignment_expression -> ID PLUSEQUAL expression','assignment_expression',3,'p_assignment_expression','parsert.py',66),
  ('assignment_expression -> ID MINUSEQUAL expression','assignment_expression',3,'p_assignment_expression','parsert.py',67),
  ('assignment_expression -> ID TIMESEQUAL expression','assignment_expression',3,'p_assignment_expression','parsert.py',68),
  ('assignment_expression -> ID DIVEQUAL expression','assignment_expression',3,'p_assignment_expression','parsert.py',69),
  ('assignment_expression -> ID MODEQUAL expression','assignment_expression',3,'p_assignment_expression','parsert.py',70),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression','parsert.py',75),
  ('additive_expression -> additive_expression PLUS term','additive_expression',3,'p_additive_expression','parsert.py',80),
  ('additive_expression -> additive_expression MINUS term','additive_expression',3,'p_additive_expression','parsert.py',81),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression','parsert.py',82),
  ('term -> term TIMES factor','term',3,'p_term','parsert.py',87),
  ('term -> term DIVIDE factor','term',3,'p_term','parsert.py',88),
  ('term -> factor','term',1,'p_term','parsert.py',89),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parsert.py',94),
  ('factor -> ID','factor',1,'p_factor','parsert.py',95),
  ('factor -> INT','factor',1,'p_factor','parsert.py',96),
  ('factor -> FLOAT','factor',1,'p_factor','parsert.py',97),
  ('factor -> STRING','factor',1,'p_factor','parsert.py',98),
  ('control_structure -> IF LPAREN expression RPAREN block','control_structure',5,'p_control_structure','parsert.py',103),
  ('control_structure -> IF LPAREN expression RPAREN block ELSE block','control_structure',7,'p_control_structure','parsert.py',104),
  ('control_structure -> WHILE LPAREN expression RPAREN block','control_structure',5,'p_control_structure','parsert.py',105),
  ('control_structure -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN block','control_structure',9,'p_control_structure','parsert.py',106),
  ('control_structure -> RETURN expression SEMICOLON','control_structure',3,'p_control_structure','parsert.py',107),
  ('struct_declaration -> STRUCT ID LBRACE var_declaration_list RBRACE','struct_declaration',5,'p_struct_declaration','parsert.py',111),
  ('var_declaration_list -> var_declaration_list var_declaration','var_declaration_list',2,'p_var_declaration_list','parsert.py',115),
  ('var_declaration_list -> var_declaration','var_declaration_list',1,'p_var_declaration_list','parsert.py',116),
  ('empty -> <empty>','empty',0,'p_empty','parsert.py',120),
]
