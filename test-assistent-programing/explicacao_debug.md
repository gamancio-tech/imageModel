# Explicação do Código em `debug.py`

Este arquivo contém um programa em Python que calcula o total de uma compra com itens, imposto e desconto opcional. Abaixo, uma explicação linha por linha do código atual.

## Entrada de Dados

```python
cliente = input("Qual é seu nome? ")
```
- Solicita o nome do cliente via entrada do usuário e armazena em `cliente`.

```python
qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))  # Corrigido: adicionadas aspas na string do input
```
- Solicita a quantidade do item 1, converte para inteiro e armazena em `qtd1`.
- Solicita o preço do item 1, converte para float e armazena em `item1`. O comentário indica uma correção anterior.

```python
qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))
```
- Similar ao item 1, para o item 2.

```python
qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))
```
- Similar ao item 1, para o item 3.

## Cálculos dos Itens

```python
# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3
```
- Calcula o total para cada item multiplicando quantidade por preço.

```python
subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10
```
- Calcula o subtotal somando os totais dos itens.
- Calcula o imposto como 10% do subtotal.

## Desconto

```python
# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # Corrigido: convertido para float
desconto = subtotal * (desconto_cupom / 100)
```
- Solicita o percentual de desconto, converte para float e armazena em `desconto_cupom`. O comentário indica uma correção.
- Calcula o valor do desconto aplicando o percentual ao subtotal.

## Total Final

```python
# TOTAL FINAL
total = subtotal + imposto - desconto
```
- Calcula o total final somando subtotal e imposto, subtraindo o desconto.

## Exibição

```python
# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31
```
- Cria strings para linhas de separação: `linha` com 31 "=" e `separador` com 31 "-".

```python
print(linha)
print(f" Cliente: {cliente}")
print(linha)
```
- Imprime a linha de separação.
- Imprime o nome do cliente formatado.
- Imprime outra linha de separação.

```python
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")  # Corrigido: adicionado 'f' para f-string
print(f" Item 3:        R$ {total_item3:.2f}")
```
- Imprime o total de cada item formatado com 2 casas decimais. O comentário no item 2 indica uma correção anterior.

```python
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")
```
- Imprime o separador.
- Imprime o subtotal formatado.
- Imprime o imposto formatado.

```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # Corrigido: indentação e conversão para float permite comparação e formatação
```
- Verifica se há desconto (percentual > 0).
- Se sim, imprime o desconto formatado. O comentário indica correções anteriores.

```python
print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```
- Imprime a linha de separação.
- Imprime o total final arredondado para 2 casas decimais.
- Imprime a linha de separação final.

## Erros Encontrados e Resoluções

### 1. Falta de aspas na string do input (Item 1)

**Erro original:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:** A string passada para `input()` estava sem aspas, o que causaria um erro de sintaxe.

**Resolução:** Adicionadas aspas duplas ao redor da string:
```python
item1 = float(input("Preço do item 1? "))
```

### 2. Falta do prefixo 'f' para f-string (Item 2)

**Erro original:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:** Sem o prefixo `f`, a string não seria interpretada como uma f-string, resultando em uma saída literal com as chaves em vez do valor formatado.

**Resolução:** Adicionado o prefixo `f`:
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

### 3. Tipo de dado incorreto para desconto_cupom

**Erro original:**
```python
desconto_cupom = int(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Problema:** Usar `int()` impediria a entrada de valores decimais como 5.5% ou 10.25%. Além disso, a comparação `if desconto_cupom > 0:` seria feita com inteiro, limitando a flexibilidade.

**Resolução:** Convertido para `float`:
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

### 4. Indentação incorreta do print de desconto

**Erro original:**
```python
desconto = subtotal * (desconto_cupom / 100)
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:** O `print()` estava no mesmo nível de indentação que a atribuição de `desconto`, fora do bloco `if`, resultando em exibição do desconto mesmo quando ele era zero.

**Resolução:** Indentado o `print()` para dentro do bloco `if`:
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

Isso garante que o desconto só seja exibido quando o cliente realmente tiver um cupom válido (percentual > 0).