# ====================================================
# Programando para web com Python, HTML e CSS
#=====================================================


#SINTAXE PYTHON
# => A sintaxe Python pode ser executada escrevendo diretamente na linha de comando:
print("Hello, Rodrigo")

#RECUO PYTHON
# => O recuo refere-se aos espaços no início de uma linha de código.
if 5 > 2:
  print("Five is greater than two!")


#COMENTÁRIOS 
#This is a comment. => Os comentários começam com um # e o Python renderizará o resto da linha como um comentário:
print("Hello, World!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")


#VARIÁVEIS PYTHON 
# => No Python, as variáveis ​​são criadas quando você atribui um valor a ela:
x = 5
y = "Boa noite!"
print(x)
print(y)

#As variáveis ​​não precisam ser declaradas com nenhum tipo específico e podem até mesmo mudar de tipo depois de configuradas.
x = 4       # x è do tipo int
x = "Sally" # x é do tipo str
print(x)

#CASTING 
# => Especifica o tipo de dados de uma variável, isso pode ser feito com o casting.
x = str(10)    # x will be '10'
y = int(10)    # y will be 10
z = float(10)  # z will be 10.0

print(x)
print(y)
print(z)

#OBTENHA O TIPO 
# => Você pode obter o tipo de dados de uma variável com a type()função.
x = 10
y = "RODRIGO"

print(type(x))
print(type(y))

#CITAÇÕES SIMPLES OU DUPLAS
x = "John"
print(x)
#as aspas duplas são iguais às aspas simples:
x = 'John'
print(x)

#MAIÚSCULAS E MINUSCÚLAS 
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#NOMES DE VARIÁVEIS 
# => Uma variável pode ter um nome curto ou um nome mais descritivo. Regras para variáveis ​​Python:
# O nome de uma variável deve começar com uma letra ou o caractere sublinhado
# O nome de uma variável não pode começar com um número
# Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _)
# Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, idade e IDADE são três variáveis ​​diferentes)

myvar = "RODRIGO"
my_var = "RODRIGO"
_my_var = "RODRIGO"
myVar = "RODRIGO"
MYVAR = "RODRIGO"
myvar2 = "RODRIGO"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Nomes de variáveis ​​com mais de uma palavra podem ser difíceis de ler.
#Existem várias técnicas que você pode usar para torná-los mais legíveis:

#CASO CAMEL
myVariableName = "Abacaxi"
print(myVariableName)

#CASO PASCAL
MyVariableName = "Rodrigo"
print(MyVariableName)

#ESTOJO DE COBRA
my_variable_name = "Orange"
print(my_variable_name)

#MUITOS VALORES PARA VARIÁVEIS MULTIPLAS
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#UM VALOR PARA MÚLTIPLAS VARIÁVEIS 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#DESCOMPACTAR UMA LISTA, TUPLA, ETC. 
# => Python permite que você extraia os valores em variáveis. Isso é chamado de descompactar .
fruits = ["Uva", "Maçã", "Morango"]
x, y, z = fruits
print(x)
print(y)
print(z)

