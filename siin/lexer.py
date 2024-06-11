from ply import lex

# Lista de tokens
tokens = (
    'ID', 'TYPE', 'INT', 'FLOAT', 'STRING', 'KEYWORD',
    'SEMICOLON', 'DOT', 'COMMA', 'PLUSPLUS', 'MINUSMINUS',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'MODULO', 
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'OROR', 'ANDAND', 'NOT', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'EQUALEQUAL',
    'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'ANDANDEQUAL', 'OROREQUAL',
    'COMMENT', 'MULTICOMMENT', 'STRUCT', 'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'BOOLEAN'
)

keywords = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'scanf': 'SCANF',
    'printf': 'PRINTF',
    'main': 'MAIN',
    'return': 'RETURN'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_OROR = r'\|\|'
t_ANDAND = r'&&'
t_NOT = r'!'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_NOTEQUAL = r'!='
t_EQUALEQUAL = r'=='
t_MODULO = r'%'
t_DOT = r'\.'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_ANDANDEQUAL = r'&&='
t_OROREQUAL = r'\|\|='

# Regular expression rules with some action code
def t_TYPE(t):
    r'int|float|double|char|boolean'
    t.type = keywords.get(t.value, 'TYPE')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_KEYWORD(t):
    r'\b(if|else|for|while|return|main|printf|scanf)\b'
    t.type = keywords.get(t.value, 'KEYWORD')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_MULTICOMMENT(t):
    r'/\*[\s\S]*?\*/'
    pass

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
