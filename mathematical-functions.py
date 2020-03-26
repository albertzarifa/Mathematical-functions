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
