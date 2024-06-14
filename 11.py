def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence
n = int(input("Enter the value of n: "))
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are:")
for num in fibonacci_numbers:
    print(num, end=" ")
