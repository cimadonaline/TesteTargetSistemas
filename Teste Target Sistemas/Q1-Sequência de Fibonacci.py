def fibonacci(n):
    if n <= 0:
        return "O número deve ser positivo"
    elif n == 1:
        return [0]
    else:
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

num = int(input("Digite um número: "))
sequencia = fibonacci(num)
if num in sequencia:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


    #Explicação do código
    #Chamamos a função, no caso a de nome FIBONACCI quando digitamos um número que foi armazenado na SEQUENCIA, verificamos então se este número está dentro das condições passadas, validando assim se ele está ou não dentro da sequência de Fibonacci#