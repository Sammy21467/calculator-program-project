# imports
import math

# Formula reminders
# Area of circle: A = pi r^2
# Area of parallelogram: A = b * h
# Area of Rectangle & Square: A = l * w
# Area of Triangle: A = b * h / 2
# Circumference of Circle: c = 2 pi r
# Perimeter: add all sides
# Pythagorean Theorem: a^2 + b^2 = c^2
# Volume of Rectangular Prism: V = L * W * H
# Volume of Cube: V = s^3
# Fahrenheit to Celsius: c = 5/9 (f - 32)
# Celsius to Fahrenheit: f = 9/5 * c + 32
# inches * 2.54 = cm
# 1 foot = 12 inches
# miles * 1.60934 = km

while True:
    print(" __________________________________________")
    print("|----Welcome to the calculator program-----|")
    print("|------------------------------------------|")
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
    print("|0. Quit                                   |")
    print("|__________________________________________|")

    menu_ans = input("What would you like to do? ").lower()

    # quit
    if menu_ans == "0" or menu_ans == "quit":
        print("Goodbye!")
        break

    # addition
    elif menu_ans == "1" or menu_ans == "addition":
        print()
        print("You are in the addition section!")
        print()
        while True:
            add_equation = input("What is your equation? (example: 2+2+2) ")
            try:
                pieces = add_equation.split("+")
                total = 0
                for piece in pieces:
                    total = total + float(piece)
                if total == int(total):
                    total = int(total)
                print("Your total is", total)
            except ValueError:
                print("Please type numbers and + signs only!")
            print()
            ans_to_menu = input("Type 'continue' to add more or 'menu' to go back: ").lower()
            if ans_to_menu == "menu":
                break

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
                pieces = sub_equation.split("+")
                total = 0
                for piece in pieces:
                    if piece == "":
                        continue
                    total = total + float(piece)
                if total == int(total):
                    total = int(total)
                print("Your total is", total)
            except ValueError:
                print("Please type numbers and - signs only!")
            print()
            ans_to_menu = input("Type 'continue' to subtract more or 'menu' to go back: ").lower()
            if ans_to_menu == "menu":
                break

    # multiplication
    elif menu_ans == "3" or menu_ans == "multiplication":
        print()
        print("You are in the multiplication section!")
        print()
        while True:
            mult_equation = input("What is your equation? (example: 2*3*4) ")
            try:
                mult_equation = mult_equation.replace(" ", "")
                mult_equation = mult_equation.replace("x", "*")
                pieces = mult_equation.split("*")
                total = 1
                for piece in pieces:
                    total = total * float(piece)
                if total == int(total):
                    total = int(total)
                print("Your total is", total)
            except ValueError:
                print("Please type numbers and * signs only!")
            print()
            ans_to_menu = input("Type 'continue' to multiply more or 'menu' to go back: ").lower()
            if ans_to_menu == "menu":
                break

    # division
    elif menu_ans == "4" or menu_ans == "division":
        print()
        print("You are in the division section!")
        print()
        while True:
            div_equation = input("What is your equation? (example: 10/2/5) ")
            try:
                div_equation = div_equation.replace(" ", "")
                pieces = div_equation.split("/")
                total = float(pieces[0])
                for piece in pieces[1:]:
                    total = total / float(piece)
                if total == int(total):
                    total = int(total)
                print("Your total is", total)
            except ValueError:
                print("Please type numbers and / signs only!")
            except ZeroDivisionError:
                print("You can't divide by zero!")
            print()
            ans_to_menu = input("Type 'continue' to divide more or 'menu' to go back: ").lower()
            if ans_to_menu == "menu":
                break

    # order of operations
    elif menu_ans == "5" or menu_ans == "order of operations":
        print()
        print("You are in the order of operations section!")
        print("(You can use + - * / ^ and parentheses)")
        print()
        while True:
            order_equation = input("What is your equation? (example: 2+3*4) ")
            allowed = "0123456789+-*/^(). "
            good = True
            for letter in order_equation:
                if letter not in allowed:
                    good = False
            if good == False or order_equation == "":
                print("Please use only numbers and + - * / ^ ( )")
            else:
                try:
                    order_equation = order_equation.replace("^", "**")
                    total = eval(order_equation)
                    if total == int(total):
                        total = int(total)
                    print("Your total is", total)
                except ZeroDivisionError:
                    print("You can't divide by zero!")
                except:
                    print("That equation doesn't look right. Try again.")
            print()
            ans_to_menu = input("Type 'continue' to do more or 'menu' to go back: ").lower()
            if ans_to_menu == "menu":
                break

    # geometry
    elif menu_ans == "6" or menu_ans == "geometry":
        print()
        print("You are in the geometry section!")
        print()
        while True:
            print("What would you like to calculate?")
            print("1. Area of Circle")
            print("2. Area of Parallelogram")
            print("3. Area of Rectangle & Square")
            print("4. Area of Triangle")
            print("5. Circumference of Circle")
            print("6. Perimeter")
            print("7. Pythagorean Theorem")
            print("8. Volume of Rectangular Prism")
            print("9. Volume of Cube")
            geom_ans = input("Type your answer: ")
            # try:
            #     if geom_ans == "1":
            #         radius = float(input("What is the radius? "))
            #         area = math.pi * radius ** 2
            #         print("The area of the circle is", round(area, 2))