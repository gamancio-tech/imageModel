from typing import List, Tuple

def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    if not numeros:
        raise ValueError("A lista de números não pode ser vazia.")

    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return total, media, maior, menor

valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior_valor, menor_valor = calcular_estatisticas(valores)

print("total:", total)
print("média:", media)
print("maior:", maior_valor)
print("menor:", menor_valor)