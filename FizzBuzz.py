number = 0
while(number < 100):
    number+=1
    if number%3==0:
        print(number,"Fizz")
    if number%5==0:
        print(number,"Buzz")
    if number %5==0 and number%3==0:
        print(number,"FizzBuzz")
    else:
        print(number)