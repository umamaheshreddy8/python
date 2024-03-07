#Write a program to find all prime numbers between 1 to 100.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for x in range(1, 101):
    if is_prime(x):
        print(x)


        
            
        
            

    
    
