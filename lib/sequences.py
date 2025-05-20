def print_fibonacci(length):
    if length <= 0:
        print([])  
        return

    
    fib_sequence = [0]

    if length > 1:
        fib_sequence.append(1)

    
    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    print(fib_sequence)
