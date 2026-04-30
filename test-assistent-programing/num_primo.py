import math


def eh_primo(n: int) -> bool:
    """Verifica se um número é primo.

    Args:
        n: Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if not isinstance(n, int) or n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite_raiz = math.isqrt(n)
    for divisor in range(3, limite_raiz + 1, 2):
        if n % divisor == 0:
            return False
    return True


def obter_numero_inteiro() -> int | None:
    """Solicita e valida a entrada de um número inteiro do usuário.

    Returns:
        int | None: O número inteiro fornecido pelo usuário, ou None se a entrada
            for inválida ou vazia.
    """
    entrada = input("Digite um número inteiro para verificar se é primo: ").strip()
    if not entrada:
        print("Nenhum valor informado.")
        return None

    try:
        return int(entrada)
    except ValueError:
        print("Valor inválido. Informe apenas um número inteiro.")
        return None


def imprimir_status_primo(numero: int) -> None:
    """Imprime se um número é primo ou não.

    Args:
        numero: Número inteiro a ser verificado e exibido.
    """
    situacao = "primo" if eh_primo(numero) else "não primo"
    print(f"{numero}: {situacao}")


def main() -> None:
    """Função principal que executa o programa de verificação de números primos.

    Solicita um número inteiro ao usuário e exibe se é primo ou não.
    """
    numero = obter_numero_inteiro()
    if numero is None:
        return
    imprimir_status_primo(numero)


if __name__ == "__main__":
    main()
