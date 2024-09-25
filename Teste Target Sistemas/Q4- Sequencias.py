def next_elements():
    # a) Sequência de números ímpares
    seq_a = [1, 3, 5, 7]
    next_a = seq_a[-1] + 2

    # b) Sequência de potências de 2
    seq_b = [2, 4, 8, 16, 32, 64]
    next_b = seq_b[-1] * 2

    # c) Sequência de quadrados perfeitos
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    next_c = (len(seq_c)) ** 2  # len(seq_c) é 7, então 7^2

    # d) Sequência de quadrados de números pares
    seq_d = [4, 16, 36, 64]
    next_d = ((len(seq_d) + 1) * 2) ** 2  # próximo par (10) ao quadrado

    # e) Sequência de Fibonacci
    seq_e = [1, 1, 2, 3, 5, 8]
    next_e = seq_e[-1] + seq_e[-2]

    # f) Sequência com padrão específico
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    next_f = seq_f[-1] + 1  # seguindo o padrão

    print(f"Próximo elemento da sequência a: {next_a}")
    print(f"Próximo elemento da sequência b: {next_b}")
    print(f"Próximo elemento da sequência c: {next_c}")
    print(f"Próximo elemento da sequência d: {next_d}")
    print(f"Próximo elemento da sequência e: {next_e}")
    print(f"Próximo elemento da sequência f: {next_f}")

next_elements()


#Explicação

#Para cada sequencia se calcula o proximo elemento utilizando-se da lógica que identificamos