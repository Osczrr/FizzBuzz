number = 0
while(number < 100):
    number+=1
    if number%3==0:
        print(number,"Fizz")
    if number%5==0:
        print(number,"Buzz")
    else:
        print(number)