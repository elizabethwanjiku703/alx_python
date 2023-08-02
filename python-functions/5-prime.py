# 5. Prime Number Function 
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True
