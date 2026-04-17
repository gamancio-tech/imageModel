import math


def eh_primo(n: int) -> bool:
    """Retorna True se n for um número primo, caso contrário False."""
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
    situacao = "primo" if eh_primo(numero) else "não primo"
    print(f"{numero}: {situacao}")


def main() -> None:
    numero = obter_numero_inteiro()
    if numero is None:
        return
    imprimir_status_primo(numero)


if __name__ == "__main__":
    main()
