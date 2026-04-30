# Projeto: Assistente de Programação - Testes e Refatoração

Este projeto contém exemplos de código Python demonstrando boas práticas de desenvolvimento, incluindo tratamento de erros, refatoração, e testes. É um material educacional para aprender sobre debugging, otimização e padrões de código.

## 📁 Estrutura do Projeto

```
test-assistent-programing/
├── num_primo.py                    # Programa para verificar números primos
├── debug.py                        # Calculadora de compras com imposto e desconto
├── refatoracao.py                  # Cálculo de estatísticas (versão refatorada)
├── explicacao_num_primo.md         # Documentação do código num_primo.py
├── explicacao_debug.md             # Documentação do código debug.py
├── explicacao_refatoracao.md       # Documentação do código refatoracao.py
└── README.md                       # Este arquivo
```

## 📄 Descrição dos Arquivos

### 1. **num_primo.py** - Verificador de Números Primos

Um programa interativo que verifica se um número é primo ou não.

#### Funcionalidades:
- ✅ Validação de entrada (apenas números inteiros maiores ou iguais a 2)
- ✅ Verificação otimizada usando raiz quadrada
- ✅ Tratamento de erros com mensagens claras
- ✅ Docstrings no padrão Google em português

#### Funções principais:
- `eh_primo(n: int) -> bool`: Verifica se um número é primo
- `obter_numero_inteiro() -> int | None`: Solicita e valida entrada do usuário
- `imprimir_status_primo(numero: int) -> None`: Exibe se o número é primo
- `main() -> None`: Função principal do programa

#### Como usar:
```bash
python num_primo.py
```

**Exemplo de execução:**
```
Digite um número inteiro para verificar se é primo: 17
17: primo
```

#### Algoritmo de otimização:
- Retorna `False` para números menores que 2
- Trata o número 2 como caso especial
- Elimina números pares
- Testa apenas até a raiz quadrada do número (reduz complexidade)
- Testa apenas divisores ímpares

---

### 2. **debug.py** - Calculadora de Compras

Um programa que calcula o total de uma compra com múltiplos itens, incluindo imposto e desconto opcional.

#### Funcionalidades:
- 💰 Cálculo de preço total por item
- 📊 Cálculo automático de imposto (10%)
- 🎟️ Aplicação de desconto via cupom
- 🖨️ Exibição formatada e legível dos valores

#### Lógica:
1. Solicita nome do cliente
2. Captura quantidade e preço de 3 itens
3. Calcula subtotal (soma dos itens)
4. Aplica 10% de imposto
5. Aplica desconto (se houver cupom)
6. Exibe recibo formatado

#### Como usar:
```bash
python debug.py
```

**Exemplo de execução:**
```
Qual é seu nome? João
Quantidade do item 1: 2
Preço do item 1? 50.00
Quantidade do item 2: 1
Preço do item 2? 100.00
Quantidade do item 3: 3
Preço do item 3? 25.00
Você tem um cupom de desconto? (Digite o percentual ou 0): 10
===============================
 Cliente: João
===============================
 Item 1:        R$ 100.00
 Item 2:        R$ 100.00
 Item 3:        R$ 75.00
-------------------------------
 Subtotal:      R$ 275.00
 Imposto (10%): R$ 27.50
 Desconto (10%): -R$ 27.50
===============================
 TOTAL:         R$ 275.00
===============================
```

#### Fórmulas:
- **Total por item**: `quantidade × preço`
- **Subtotal**: Soma de todos os itens
- **Imposto**: `subtotal × 0.10`
- **Desconto**: `subtotal × (percentual / 100)`
- **Total Final**: `subtotal + imposto - desconto`

---

### 3. **refatoracao.py** - Cálculo de Estatísticas

Um programa que calcula estatísticas básicas de uma lista de números (total, média, maior e menor valor).

#### Funcionalidades:
- 📈 Cálculo de total, média, máximo e mínimo
- ✅ Validação contra listas vazias
- 📝 Código refatorado com variáveis nomeadas descritivamente
- 🚀 Uso de built-ins Python (`sum()`, `max()`, `min()`)

#### Função principal:
```python
def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    """Calcula total, média, maior e menor valor de uma lista de números."""
```

#### Como usar:
```bash
python refatoracao.py
```

**Exemplo de execução:**
```
total: 346
média: 34.6
maior: 89
menor: 2
```

#### Melhorias de Refatoração:
| Antes | Depois |
|-------|--------|
| Nomes de função: `c()` | `calcular_estatisticas()` |
| Variáveis: `l`, `t`, `m`, `mx`, `mn` | `numeros`, `total`, `media`, `maior`, `menor` |
| Loop manual: `for i in range(len(l))` | Built-ins: `sum()`, `max()`, `min()` |
| Sem validação | Validação de lista vazia |
| Sem type hints | Type hints completos |

---

## 🎓 Conceitos Aprendidos

### Boas Práticas de Desenvolvimento:

1. **Type Hints**: Uso de anotações de tipo para melhor legibilidade e IDE support
2. **Docstrings**: Documentação no padrão Google em português
3. **Tratamento de Erros**: Validação de entrada e exceções
4. **Refatoração**: Melhoria de legibilidade sem alterar funcionalidade
5. **Nomes Descritivos**: Variáveis e funções com nomes claros
6. **Funções Pequenas**: Divisão de responsabilidades
7. **Comments Inline**: Explicação de lógica de decisão
8. **Main Guard**: Uso de `if __name__ == "__main__":`

### Algoritmos e Otimizações:

- **Verificação de Primos**: Redução de complexidade usando raiz quadrada
- **Eliminação de Pares**: Otimização pulando números pares
- **Built-ins Python**: `sum()`, `max()`, `min()` em vez de loops

---

## 🚀 Como Executar

### Pré-requisitos:
- Python 3.7 ou superior

### Executar um arquivo específico:
```bash
# Verificar se um número é primo
python num_primo.py

# Calcular total de compra
python debug.py

# Calcular estatísticas
python refatoracao.py
```

---

## 📚 Documentação Adicional

Cada arquivo possui um arquivo `.md` correspondente com explicação detalhada:
- `explicacao_num_primo.md` - Análise linha por linha do código
- `explicacao_debug.md` - Detalhes da lógica de cálculo
- `explicacao_refatoracao.md` - Comparação antes/depois da refatoração

---

## 🔧 Melhorias Futuras

- [ ] Adicionar testes unitários com `pytest`
- [ ] Implementar logging para debug
- [ ] Criar versão com interface gráfica (tkinter)
- [ ] Adicionar mais casos de teste
- [ ] Documentação em English

---

## 📝 Autor

Projeto educacional para ensino de boas práticas de programação Python.

---

## 📄 Licença

Este projeto é fornecido como material educacional e pode ser usado livremente para fins de aprendizado.
