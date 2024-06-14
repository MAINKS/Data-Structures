def print_powers_of_two(exponent):
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    if exponent == 0:
        print(1)
        return 1
    else:
        previous_power = print_powers_of_two(exponent - 1)
        current_power = previous_power * 2
        print(current_power)
        return current_power
    
print_powers_of_two(10)

#Time complexity for above program :O(LOGN) , Because the interval is variable without fix intervals. 

def poweroftwo(n):
    if n == 0:
        return n
    elif n == 1:
        return 2
    else:
        return 2*poweroftwo(n-1)
print(poweroftwo(4))