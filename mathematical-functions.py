def euclidean_algorithm(): 
    """
    This is the euclidean algorithm. Given two number,
    it will return the gcd (Greatest common divisor)
    >>> euclidean_algorithm(2,5)
    The gcd is: 1
     >>> euclidean_algorithm(9,27)
    The gcd is: 9
    """
    
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    r = a%b
    
    while r:
        a = b
        b = r
        r = a%b
    print("The gcd is: ", b)


def is_prime(n):
    """
    This function return whether a given number is prime or not.
    >>> is_prime(3)
    True
    >>> is_prime(2)
    True
    >>> is_prime(7)
    False
    """

    num_check = 1
    num_of_divisors = 0

    if n <= 1:                   # This will automatically return False if the given number
        return False             # is less than or eqaual to 1, and prime numbers start at 2.

    while (num_check < n+1):     # To check all the numbers to and including n.
        if n % num_check == 0:
            num_of_divisors += 1 # Add one to the number of divisors so we can check the number we get later.
        num_check += 1           # This is to go to the next number to check

    return (num_of_divisors == 2)# This will only return True if the number of divisors is 2,
                                 # where the 2 are only 1 and n. 