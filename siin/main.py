import semantic as sem
from lexer import lexer
from parsert import parser

def compiler():
    data = '''
        float a; 
        a = 2.0;
        int b;
        b = 1;
        boolean validate;
        validate = True;
        int d;
        int s;
        s = validate + b;
        d = (2+2)/2;
    '''

    lexer.input(data)
    for token in lexer:
        print(token)

    result = parser.parse(data)
    print(result)
    
    if sem.analyze(data):
        print("Análise semântica feita com sucesso!")

if __name__ == "__main__":
    compiler()
