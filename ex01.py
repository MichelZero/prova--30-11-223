

# 1.	Em linguagem Python, Dado um dicionário, 
# faça um programa que encontre 
# a quantidade de cada elementos, faça uso de 
# conjuntos e estrutura de repetição:
d1 = {'a':1,'b':2,'c':3,'d':3,'e':4,'f':4,'g':2,'i':2}



d1 = {'a':1,'b':2,'c':3,'d':3,'e':4,'f':4,'g':2,'i':2}
l1 = d1.values()
l2 = []
for i in l1:
  l2.append(i)
conjunto = set(l2)
print()
# itera o conjunto 
for i in conjunto:
  contador = l2.count(i)
  print(f"{i} -> {contador} elemento(s)")
