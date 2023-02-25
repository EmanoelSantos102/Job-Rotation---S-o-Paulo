#Escreva um programa que inverta os caracteres de um string.
palavra=("hire me")
palavra_rev=""
n=0
for i in range(len(palavra)):
    n+=1
    palavra_rev+=palavra[len(palavra)-n]
print(palavra_rev)
