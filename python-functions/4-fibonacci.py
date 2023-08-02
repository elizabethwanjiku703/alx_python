# Fibonacci Sequence Fucntion
def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0] * n
    sequence[0] = 0

    if n > 1:
        sequence[1] = 1

    for i in range(2, n):
        sequence[i] = sequence[i-2] + sequence[i-1]

    return sequence
