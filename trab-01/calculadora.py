def soma(a,b):
    '''
    Recebe dois numeros e retona a soma deles

    Input: a e b, dois numeros inteiros
    Output: a+b
    '''
    return a + b
def subtracao(a,b):
    ''' Recebe dois numeros e retorna a subtração deles
        Input: a e b, dois numeros inteiros
        Output: a-b
    '''
    return a - b
def multiplicacao(a,b):
    ''' Recebe dois numeros e retorna a multiplicação deles
        Input: a e b, dois numeros inteiros
        Output: a*b
    '''
    return a * b

def divisao(a,b):
    ''' Recebe dois numeros inteiros
        e retorna a divisão inteira deles
        Input a e b, dois numeros inteiro
        Output: a%b
    '''
    return a % b
def operacoes():
    ''' Retorna Um dicionario com todas as operações
        Output: Um dicionario com todas as operações
        
    '''
    return dict([('soma',soma), ('subtracao', subtracao),
        ('multiplicacao', multiplicacao),('divisao', divisao)])