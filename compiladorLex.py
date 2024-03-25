class Lexico:
    def __init__(indiv):
        indiv.palRes = {"int", "float", "char", "boolean", "void", "if", "else", "for", "while",
                         "scanf", "println", "main", "return"}
        indiv.operadores = {"=", "+", "-", "*", "/", "%", "&&", "||", "!", "&", "|"}
        indiv.comp = {">", ">=", "<", "<=", "!=", "=="}
        indiv.simbolos = {"(", ")", "[", "]", "{", "}", ",", ";"}
        indiv.tokens = []
        indiv.identifi = []

    def verifi(indiv, codigo):
        linhas = codigo.split('\n')

        for linha in linhas:
            indiv.linhaAT(linha)

    def linhaAT(indiv, linha):
        tokenAT = ""
        i = 0

        while i < len(linha):
            if linha[i].isspace():
                i += 1
                continue

            if linha[i] in indiv.simbolos:
                indiv.addToken("Simbolos", linha[i])
                i += 1
            elif linha[i:i+2] in indiv.comp:
                indiv.addToken("Op. comparacao", linha[i:i+2])
                i += 2
            elif linha[i] in indiv.operadores:
                tokenAT += linha[i]
                if linha[i] == '&' or linha[i] == '|' and i + 1 < len(linha) and linha[i] == linha[i + 1]:
                    tokenAT += linha[i + 1]
                    i += 1
                indiv.addToken("Operadores", tokenAT)
                tokenAT = ""
                i += 1
            elif linha[i] == "'":
                tokenAT += linha[i]
                i += 1
                while i < len(linha) and linha[i] != "'":
                    tokenAT += linha[i]
                    i += 1
                tokenAT += linha[i]
                indiv.addToken("Char", tokenAT)
                tokenAT = ""
                i += 1
            elif linha[i] == '"':
                tokenAT += linha[i]
                i += 1
                while i < len(linha) and linha[i] != '"':
                    tokenAT += linha[i]
                    i += 1
                tokenAT += linha[i]
                indiv.addToken("String", tokenAT)
                tokenAT = ""
                i += 1
            else:
                while i < len(linha) and not linha[i].isspace() and linha[i] not in indiv.operadores and linha[i:i+2] not in indiv.comp and linha[i] not in indiv.simbolos:
                    tokenAT += linha[i]
                    i += 1
                if tokenAT:
                    indiv.addIdToken(tokenAT)
                tokenAT = ""

    def addToken(indiv, tipoTok, valor):
        indiv.tokens.append({"tipo": tipoTok, "valor": valor})

    def addIdToken(indiv, identifi):
        if identifi in indiv.palRes:
            indiv.tokens.append({"tipo": "Palavras Reservadas", "valor": identifi})
        elif identifi in indiv.identifi:
            indiv.tokens.append({"tipo": "(id, " + str(indiv.identifi.index(identifi)) + ")", "valor": identifi})
        else:
            indiv.identifi.append(identifi)
            indiv.tokens.append({"tipo": "(id, " + str(len(indiv.identifi) - 1) + ")", "valor": identifi})

codigoF = '''
#include <stdio.h>

int main(){
	int i, j;
	scanf("%d %d", &i, &j);

	if(i % (j + 1) == 0){
		printf("Carlos");
	}
	else{printf("Paula");}

	return 0;
}
'''

Mtoken = Lexico()
Mtoken.verifi(codigoF)

for token in Mtoken.tokens:
    print(token["tipo"], token["valor"])
