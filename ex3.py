import json
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
menor=dados[0]["valor"]
maior=dados[0]["valor"]
soma=qtd=qtdsup=0
for i in range(30):
    if dados[i]["valor"]>0 and dados[i]["valor"]<menor:
        menor=dados[i]["valor"]
        imenor=i
    if dados[i]["valor"]>maior:
        maior=dados[i]["valor"]
        imaior=i
    if dados[i]["valor"]>0:
        soma+=dados[i]["valor"]
        qtd+=1
    media=soma/qtd
for i in range(30):
    if dados[i]["valor"]>media:
        qtdsup+=1
print("O menor valor de faturamento foi de ",menor,"ocorrido no dia",dados[imenor]["dia"])    
print("O maior valor de faturamento foi de ",maior,"ocorrido no dia",dados[imaior]["dia"])     
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal ",qtdsup)