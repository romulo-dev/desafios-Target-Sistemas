import json

with open("dados.json") as file: 
    data = json.load(file)


def menor():
    menor = data[0]["valor"]
    dia = data[0]["dia"]
    for p in data:
        if p["valor"] < menor and p["valor"] != 0.0:
            menor = p["valor"]
            dia = p["dia"]
    return menor

def maior():
    maior = data[0]["valor"]
    dia = data[0]["dia"]
    for p in data:
        if p["valor"] > maior:
            maior = p["valor"]
            dia = p["dia"]
    return maior

def media():
    media = 0.0
    soma = 0.0
    diasNoMes = 30
    for p in data:
        if p["valor"] != 0.0:
            soma = soma + p["valor"]
        else:
            diasNoMes = diasNoMes -1
    media = soma / diasNoMes
    return media


media = media()

def nDiasSuperiorMedia():
    n = 0
    for p in data:
        if p["valor"] > media:
            n = n + 1
    return n


    
print("A menor fatura ocorrida é: ", menor())
print("A maior fatura ocorrida é: ", maior())
print("O número de dias que tiveram a fatura diária maior que a média é : ", nDiasSuperiorMedia())