
num = int(input("Informe um número: "))


fibonacci = [0, 1]

while fibonacci[-1] < num:
    next_fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fib)

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")