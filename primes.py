# Van Huynh
# asks user for a number and displays all the primes between 2 and the number entered


def validate_int():    # fct makes sure prime is a digit and greater than 1
    my_prime = input('Please enter an integer >= 2: ')
    if my_prime.isdigit(): 
        my_prime = int(my_prime)
        if my_prime >= 2:
            return my_prime
    else:
        return None

my_prime = None

while my_prime == None:      # if prime doesn't meet the condition, prime won't overwrite "None"
    my_prime = validate_int()

           
for primes in range(1, my_prime+1):  # evaluates every number from 1 to prime
    num_temp = []
    for num in range(2,my_prime+1):  # using each prime to see if it's divisible by any other number
        if primes % num == 0:
            num_temp.append(primes)
            if len(num_temp) >= 2:   # if there are more than 2 number evenly divisible, then it's not a prime
                break
    if len(num_temp) == 1:
        print(num_temp[0])
            

    
        
        
        



