# * 	Creator:	Sean Horner
# * 	Date:		10/05/2021
# *     Updated:	10/06/2021
# * 	Purpose:	The first assigned homework of the Python Core coursework
# * 	Requires:	None
import math


def assignment1_2_1() -> bool:
    print((50+50) + (100-10))
    return True


def assignment1_2_2() -> bool:
    print(30 + 6)
    print(6**6)
    print(6^6)
    print(6+6+6+6+6+6)
    return True


def assignment1_2_3() -> bool:
    print("Hello World")
    print("Hello World : 10")
    return True


def assignment1_2_4(input_str: str) -> int:
    parameters = input_str.split()
    principle = int(parameters[0])
    rate = int(parameters[1])
    months = int(parameters[2])
    # start guesses at the minimum number it could be: principle/months
    payment = principle/months

    found = False

    while not found:
        month_count = 0
        loop_principle = principle

        while loop_principle > payment and month_count <= months:
            month_count += 1
            principle -= payment
            principle *= (1 + (rate/100))

        if loop_principle == 0 and month_count == months:
            found = True
        elif loop_principle > 0:
            payment += loop_principle/months

    print(payment)
    return int(math.ceil(payment))


def main():
    input("Waiting for input: ")
    print("Running assignment 1: add 50+50 and 100-10")
    assignment1_2_1()

    print("Running assignment 2: print many 36's")
    assignment1_2_2()

    print("Running assignment 3: Hello World and Formatting")
    assignment1_2_3()

    assignment1_2_4("800000 6 103")


if __name__ == '__main()__':
    main()

