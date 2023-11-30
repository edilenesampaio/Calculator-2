"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# repeat forever:
while True:
    #     read input
    user_input = input("> ")
#     tokenize input
    tokens = user_input.split(" ")


    if len(tokens) >= 3:
        num1 = tokens[1] 
        num2 = tokens[2]
    else:
        num1 = tokens[1]
        num2 = "0"

#         if the first token is "q":
    if "q" in tokens:
        print("Quitting game")
        break

    elif "+" in tokens:
        print(add(float(num1),float(num2)))

    elif "-" in tokens:
        print(subtract(float(num1),float(num2)))
        
    elif "*" in tokens:
        print(multiply(float(num1),float(num2)))

    elif "/" in tokens:
        print(divide(float(num1),float(num2)))

    elif "square" in tokens:
        print(square(float(num1)))
    
    elif "cube" in tokens:
        print(cube(float(num1)))

    elif "power" in tokens:
        print(power(float(num1),float(num2)))

        

