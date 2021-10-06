import random
import time


def assignment3_a_1():
    out_list = [x for x in range(1500, 2701) if x % 5 == 0 and x % 7 == 0]
    for num in out_list:
        print(num)


def assignment3_a_2():
    def converter(temp: int, current_scale: str) -> int:
        if current_scale == "F" or current_scale == 'f':
            return int(((temp-32)/9)*5)
        else:
            return int(((temp / 5) * 9) + 32)

    temp_to_convert = int(input("Enter the temperature to convert: "))
    scale = input("Enter the temperature's *current* scale (F/C): ")

    print(f"The converted temperature is: {converter(temp_to_convert, scale)}")


def assignment3_a_3():
    magic_num = random.randint(1, 9)
    player_guess = 0

    while player_guess != magic_num:
        player_guess = int(input("Enter your guess between 1 and 9: "))

        if player_guess != magic_num:
            print("Uh oh, looks like the wrong number, guess again.")
        else:
            print("Well guessed! You got the right number!")


def assignment3_a_4():
    def pop(s: str) -> str:
        return s[:-1]
    magic_string = "*"
    while len(magic_string) < 6:
        print(magic_string)
        magic_string += '*'
    while len(magic_string) > 0:
        print(magic_string)
        magic_string = pop(magic_string)


def assignment3_a_6():
    word = input("Enter a word to reverse: ")
    print(word[::-1])


def assignment3_a_7():
    def list_parser(list_of_nums):
        odd_count = 0
        even_count = 0
        for num in list_of_nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print(f"Number of even numbers: {even_count}")
        print(f"Number of odd numbers: {odd_count}")

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Testing with list of numbers: {num_list}")
    list_parser(num_list)


def assignment3_a_8():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    for item in datalist:
        print(item)
        print(type(item))
        print("-------------------------------------")


def assignment3_a_9():
    num_list = range(0, 7)
    result = ""
    print(f"Initial number list = {num_list}")
    for num in num_list:
        if num == 3 or num == 6:
            continue
        else:
            result += f"{num} "
    print("Resulting list after filtering is: ")
    print(result)


def main():
    print("\n")
    print("Running assignment 1...")
    assignment3_a_1()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 2...")
    assignment3_a_2()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 3...")
    assignment3_a_3()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 4...")
    assignment3_a_4()
    print("")
    print("--------------------------------------------")
    print("")

    print("\n\nNumbering error: no assignment 5\n\n")

    print("Running assignment 6...")
    assignment3_a_6()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 7...")
    assignment3_a_7()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 8...")
    assignment3_a_8()
    print("")
    print("--------------------------------------------")
    print("")

    print("Running assignment 9...")
    assignment3_a_9()
    print("")


if __name__ == "__main__":
    main()
