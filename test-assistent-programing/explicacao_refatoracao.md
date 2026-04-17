# Explicação do código em `refatoracao.py`

O código original faz o seguinte:

- Define uma função `c(l)` que recebe uma lista de números.
- Inicializa `t = 0` para acumular o total dos valores.
- Usa um `for i in range(len(l))` para percorrer cada índice da lista e somar `l[i]` em `t`.
- Calcula a média com `m = t / len(l)`.
- Inicializa `mx = l[0]` e `mn = l[0]` para o maior e o menor valor da lista.
- Percorre a lista novamente e, para cada elemento:
  - atualiza `mx` se o elemento for maior que o valor atual de `mx`
  - atualiza `mn` se o elemento for menor que o valor atual de `mn`
- Retorna uma tupla com `(t, m, mx, mn)`.

Em seguida:

- Cria a lista `x = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`
- Chama `a, b, c2, d = c(x)` para receber total, média, maior e menor
- Imprime os resultados:
  - `total: a`
  - `media: b`
  - `maior: c2`
  - `menor: d`

No arquivo `refatoracao.py`, a mesma lógica foi mantida, mas com melhorias de legibilidade:

- A função foi renomeada para `calcular_estatisticas`.
- O parâmetro `l` foi renomeado para `numeros`.
- As variáveis internas foram renomeadas para `total`, `media`, `maior` e `menor`.
- Foi adicionada uma verificação para garantir que a lista não esteja vazia.
- Foram usados os built-ins `sum()`, `max()` e `min()` para simplificar os cálculos.
- O retorno permanece uma tupla com total, média, maior e menor.
- A lista de valores foi atribuída à variável `valores`.
- Os resultados são impressos com labels mais claros.

Assim, `refatoracao.py` preserva a mesma funcionalidade do código original, mas torna o fluxo e as intenções mais fáceis de entender.