MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar CNH.")

elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, não as práticas>")

else:
    print("Ainda não pode tirar CNH")    