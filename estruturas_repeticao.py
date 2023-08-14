texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

else:
     print() #adicona uma qebra de linha, para adicionar as VOGAIS
     print("Executa no final do laço, isso é referente ao else inserido")        


for numero in range (0, 51, 5):
    print(numero, end=" ")