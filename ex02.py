# prova 2
# data: 30/11/2023
# autores: Cristiano e Michel


# 2.	Em linguagem Python, faça um programa que lê uma 
# frase e substitui todas as ocorrências de espaço por "#"

oracao1 = input("entre com uma oração: ")
oracao2 = ''
for i in oracao1:
  oracao2 = oracao2 + (i if i != ' ' else '#' )

print(oracao2)
