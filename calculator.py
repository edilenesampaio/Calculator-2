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

    num1 = tokens[1]
    num2 = tokens[2]
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

        
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)