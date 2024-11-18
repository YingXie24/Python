def fibonacci(n):

    if n == 0:
        fibonacci_list = []

    elif n == 1: 
        fibonacci_list = [0]

    elif n > 1:        
        fibonacci_list = [0,1]

        #  want to stop appending when the length of the list is n
        for num_to_interate in range (n - len(fibonacci_list)):
                #  the logic of the fibonacci list is to add the last two numbers together to generate
                # the new number
            fibonacci_list.append(fibonacci_list[-2]+fibonacci_list[-1])

    return fibonacci_list    

cube = lambda x: pow(x,3)
n=5
print(list(map(cube, fibonacci(n))))