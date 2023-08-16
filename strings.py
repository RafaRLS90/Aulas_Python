nome = "Rafael"
idade = 33
profissao = "programador"
linguagem = "Python"

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}"  .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {0} Idade: {1} Profissao: {2}" .format(nome, idade, profissao))
print("Agora da melhor forma, nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))

dados = {"name": "Professor", "anos": 28}
print("Nome: {name} Idade: {anos}" .format(**dados)) #o asterístico duplo, trás as variáveis disponíveis

print(f"Aqui, apenas colocando o f, fica assim: Nome: {nome} Idade: {idade}")

print(
    '''
     **********Menu**********

     1-Depositor
     2-Sacar
     3-Sair

'''
)