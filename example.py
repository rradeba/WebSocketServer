given_temp = int(input("What is the temperature: "))

if  0 <= given_temp <= 32:
    print('Wear quilted pants!')
elif 32 < given_temp <= 60:
    print('Wear pants!')
elif given_temp > 60:
    print('Wear shorts!')
else: print("incorrect input")

