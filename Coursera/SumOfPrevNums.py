def sum_postivite_numbers(n):

    if n < 1: #Base case ; where condition breaks out
        return 0;
    
    return n + sum_postivite_numbers(n - 1)

print(sum_postivite_numbers(3))    
print(sum_postivite_numbers(5))  
print(sum_postivite_numbers(6))    
