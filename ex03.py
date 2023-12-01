# prova 2
# data: 30/11/2023
# autores: Cristiano e Michel

# 3.	Crie um dicionário para armazenar o nome 
# de 3 alunos e cada aluno com 2 notas, fazendo 
# a leitura dos valores por meio de uma estrutura 
# de repetição. Depois, crie uma nova estrutura de 
# repetição para somar todas as notas e retornar a média.

# criando a turma (dicionário)
turma = {}

# lendo os alunos (nome e notas)
for i in range(3):
  nome = input(f"Digite o nome do aluno[{i+1}]: ")
  notas = list() # criando uma lista vazia para as notas
  for j in range(2):
    nota = float(input(f"Digite a nota {j+1}: "))
    notas.append(nota) # adicionando a nota na lista de notas
  turma[nome] = notas # adicionando a lista de notas no dicionário turma
  
# listando a turma
for nome in turma:
  print(f"{nome} -> {turma[nome]}")
  
# calculando a média de cada aluno
for nome in turma:
  media = sum(turma[nome]) / len(turma[nome])
  print(f"Média de {nome}: {media:.2f}")
  
# calculando a média da turma
soma = 0
for nome in turma:
  soma += sum(turma[nome])
media = soma / len(turma)
print(f"Média da turma: {media:.2f}") 

