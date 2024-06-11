from ply import yacc
from lexer import tokens

def p_program(p):
    "program : declaration_list"

def p_declaration_list(p):
    """
    declaration_list : declaration_list declaration
                     | declaration
    """

def p_declaration(p):
    """
    declaration : var_declaration
                | fun_declaration
                | struct_declaration
                | control_structure
                | comment
    """

def p_var_declaration(p):
    """
    var_declaration : TYPE ID SEMICOLON
                    | TYPE ID EQUALS expression SEMICOLON
    """

def p_fun_declaration(p):
    """
    fun_declaration : TYPE ID LPAREN params RPAREN block
    """

def p_params(p):
    """
    params : param_list
           | empty
    """

def p_param_list(p):
    """
    param_list : param_list COMMA param
               | param
    """

def p_param(p):
    "param : TYPE ID"

def p_block(p):
    "block : LBRACE declaration_list RBRACE"

def p_comment(p):
    """
    comment : COMMENT
            | MULTICOMMENT
    """

def p_expression(p):
    """
    expression : assignment_expression
               | simple_expression
    """

def p_assignment_expression(p):
    """
    assignment_expression : ID EQUALS expression
                          | ID PLUSEQUAL expression
                          | ID MINUSEQUAL expression
                          | ID TIMESEQUAL expression
                          | ID DIVEQUAL expression
                          | ID MODEQUAL expression
    """

def p_simple_expression(p):
    """
    simple_expression : additive_expression
    """

def p_additive_expression(p):
    """
    additive_expression : additive_expression PLUS term
                        | additive_expression MINUS term
                        | term
    """

def p_term(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    """

def p_factor(p):
    """
    factor : LPAREN expression RPAREN
           | ID
           | INT
           | FLOAT
           | STRING
    """

def p_control_structure(p):
    """
    control_structure : IF LPAREN expression RPAREN block
                      | IF LPAREN expression RPAREN block ELSE block
                      | WHILE LPAREN expression RPAREN block
                      | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN block
                      | RETURN expression SEMICOLON
    """

def p_struct_declaration(p):
    "struct_declaration : STRUCT ID LBRACE var_declaration_list RBRACE"

def p_var_declaration_list(p):
    """
    var_declaration_list : var_declaration_list var_declaration
                         | var_declaration
    """

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Erro de sintaxe na linha {p.lineno}")

parser = yacc.yacc()
