number = 0
while(number < 100):
    number+=1
    if number%3==0 and number%5==0:
        print(number,"FizzBuzz")
    elif number%3==0:
        print(number,"Fizz")
    elif number %5==0:
        print(number,"Buzz")
    else:
        print(number)
