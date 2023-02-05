def fizz_buzz(n):
 
 n =int (n)
 

 if(n / 3 == 0):
    print("Fizz")
 if(n % 5 ==0):
    print("Buzz")
 else:
    print("FizzBuzz")
 return n % 3 or n % 5

    
print(fizz_buzz(input("Введите число: ")))
