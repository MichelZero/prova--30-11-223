


# 4.	Em linguagem Python, faça um programa que decida 
# se duas strings lidas do teclado são palíndromas mútuas, 
# ou seja, se uma é igual à outra quando lida de traz 
# para frente. Exemplo: amor e roma.

s1 = "amor"
s2 = s1[::-1]

palindrome = ''
for i in range(len(s1) - 1, -1, -1):
  palindrome += s1[i]
#print(palindrome)

if palindrome == s2:
  print("são palíndromas")
  print(f"{s1} - {s2}") 
else:
  print("não são palíndromas")
