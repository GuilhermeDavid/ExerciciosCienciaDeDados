def converterUnidades(valor, primeiraUnidade, unidadeFinal):
    if primeiraUnidade == "pé" and unidadeFinal == "metro":
        return valor * 0.3048
    elif primeiraUnidade == "metro" and unidadeFinal == "pé":
        return valor * 3.281
    elif primeiraUnidade == "jarda" and unidadeFinal == "metro":
        return valor * 0.9144
    elif primeiraUnidade == "jarda" and unidadeFinal == "pé":
        return valor * 3
    else:
        return "Conversão não suportada"

primeiraUnidade = input("Digite a unidade de origem (pé, metro, jarda): ")
valor = float(input("Digite o valor a ser convertido: "))
unidadeFinal = input("Digite a unidade de destino (pé, metro, jarda): ")

resultado = converterUnidades(valor, primeiraUnidade, unidadeFinal)
print(f"Resultado: {resultado}")