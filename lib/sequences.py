#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  
        return
    
    fibonacci_sequence=[0, 1]  
    for n in range(2,length):
        next_value = fibonacci_sequence[n - 1] + fibonacci_sequence[n - 2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence[:length]) 
    pass
