for FizzBuzz in range(100):

    if FizzBuzz % 3 == 0:
        print("Fizz", "The Fizz number is:", FizzBuzz)

    elif FizzBuzz % 5 == 0:
        print("Buzz", "The Buzz number is:", FizzBuzz)

    elif FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print("FizzBuzz" "The FizzBuzz number is:", FizzBuzz)

    else:
        print('None of above', FizzBuzz)