# imports
import math

# variables

# reminder for formulas

# Area of circle: A = pi r^2
# Area of parallelogram: A = b * h
# Area of Rectangle & Square: A = l * w
# Area of Triangle: A = b * h / 2
# Circumference of Circle: c = pi * d or c = 2 pi r
# perimeter: Add all sides
# Pythagorean Thereom: a^2 + b^2 = c^2
# Volume of Rextangular Prism: V = L * W * H
# Volume of Cube: V = s^3
# PEMDAS: P(parentheses), E(exponent), M(multiplication), D(divison), A(addition), S(subtraction)
# Multiplying powers with the same base: X^2 * x^b = x^a+b
# Raising a power to a power: (x^a)^b = x^a*b
#power of a product property: (xy)^a = x^a y^a
#x^-a = 1/x^a
# Farenheit to celcius: c = 5/9(f-32)
# Celcius to Farenheit: f = 9/5(35)+32
# i x 2.54cm/ 1inch = xcm
# 1 foot = 12 inches
# Mile x 1.60934 = KM
# Welcome
while True: 
    print(" __________________________________________")
    print("|----Welcome to the calculator program-----|")
    print("|------------------------------------------|")
    # menu
    print("|---------  O--P--T--I--O--N--S  --------- |")
    print("|1. Addition                               |")
    print("|2. Subtraction                            |")
    print("|3. Multiplication                         |")
    print("|4. Division                               |")
    print("|5. Order of Operations                    |")
    print("|6. Geometry                               |")
    print("|7. Algebra                                |")
    print("|8. Convert units                          |")
    print("|9. Other math(Square root, exponents)     |")
    print("|__________________________________________|")

    #
    menu_ans = input('What would you like to do? ')
    # loops for each thing
    if menu_ans == "1" or menu_ans == "addition" or menu_ans == "Addition":
    # addition
        print()
        print("You are in the addition section !")
        print()

        while True: #loop
            add_equation = input("What is your equation? (xample: 2+2+2) ")
            # equation
            try:
                pieces = add_equation.split("+")
                total = 0
                for piece in pieces:
                    total = total + float(piece)
                print("the total is", total)
            except ValueError: 
                print("Please type numbers!")

            print()
            ans_to_menu = input("Would you like to continue or go back menu? ")

            if ans_to_menu == "continue":
                continue
            elif ans_to_menu == "menu":
                break
            else:
                print("error")
                break

# subtraction
# subtraction
# subtraction
    elif menu_ans == "2" or menu_ans == "subtraction":
        print()
        print("You are in the subtraction section!")
        print()
        while True:
            sub_equation = input("What is your equation? (example: 10 - 3 - 2) ")
            try:
                sub_equation = sub_equation.replace(" ", "")
                sub_equation = sub_equation.replace("--", "+")
                sub_equation = sub_equation.replace("-", "+-")
                pieces2 = sub_equation.split("+")

                total = 0
                for piece in pieces2:
                    if piece == "":
                        continue
                    total = total + float(piece)
                if total == int(total):
                    total = int(total)
                print()
                print("Your total is", total)
            except ValueError:
                print("Please type numbers and - signs only!")
            print()
            ans_to_menu = input("Type 'continue' to subtract more or 'menu' to go back: ").lower()
            if ans_to_menu == "continue":
                continue
            elif ans_to_menu == "menu":
                break
            else:
                print("That wasn't 'continue' or 'menu'. Closing the program.")
                exit()
# Multiplication


# division


# Order of Operations


# Geometry


# Algebra


# convert units
