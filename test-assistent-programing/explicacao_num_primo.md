# Explicação do código em `num_primo.py`

1. `def eh_primo(n: int) -> bool:`
   - Define a função `eh_primo`.
   - Recebe `n` e retorna um valor booleano.

2. `    """Retorna True se n for um número primo, caso contrário False."""`
   - Docstring que descreve o comportamento da função.
   - Ajuda IDEs e documentação.

3. `    if not isinstance(n, int) or n < 2:`
   - Verifica se `n` não é inteiro ou se é menor que 2.
   - Números não inteiros e valores abaixo de 2 não são primos.

4. `        return False`
   - Retorna `False` imediatamente nesses casos.

5. `    if n == 2:`
   - Verifica o caso especial do número 2.

6. `        return True`
   - Retorna `True` para 2, o menor primo.

7. `    if n % 2 == 0:`
   - Verifica se `n` é par.

8. `        return False`
   - Retorna `False` para pares maiores que 2.

9. `    limite = int(n ** 0.5) + 1`
   - Calcula um limite de verificação baseado na raiz quadrada de `n`.
   - Não é preciso testar divisores maiores que a raiz quadrada.

10. `    for divisor in range(3, limite, 2):`
    - Loop sobre divisores ímpares a partir de 3.
    - O passo `2` evita testar números pares novamente.

11. `        if n % divisor == 0:`
    - Verifica se `n` é divisível por `divisor`.

12. `            return False`
    - Retorna `False` se encontrar um divisor.

13. `    return True`
    - Retorna `True` se nenhum divisor for encontrado.

14. `def executar_testes() -> None:`
    - Define uma função de teste para separar lógica de execução.

15. `    numeros_para_testar = [0, 6, 90, 75, 807, 7]`
    - Lista de números usados nos testes.

16. `    for numero in numeros_para_testar:`
    - Itera sobre cada número de teste.

17. `        rotulo = "primo" if eh_primo(numero) else "não primo"`
    - Chama `eh_primo(numero)` e escolhe a string correta.

18. `        print(f"{numero}: {rotulo}")`
    - Imprime o resultado formatado.

19. `if __name__ == "__main__":`
    - Bloco executado apenas quando o arquivo é rodado diretamente.

20. `    executar_testes()`
    - Chama a função de testes no modo principal.

Resumo:
- A função principal `eh_primo` usa validações claras e retorna cedo em casos simples.
- O loop de verificação testa somente divisores ímpares até a raiz quadrada.
- A função `executar_testes` separa a lógica de teste do bloco principal.