
def assignment4_a_1():
    def func():
        print("Hello World")

    func()


def assignment4_a_2():
    def func1(name):
        print(f"Hi, my name is {name}")

    username = input("Please enter your name: ")

    func1(username)


def assignment4_a_3():
    def func3(x, y, z: bool):
        if z:
            return x
        else:
            return y

    func3("hello", "goodbye", True)


def assignment4_a_4():
    def func4(x, y):
        return x * y

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    print(func4(num1, num2))


def assignment4_a_5():
    def is_even(num: int) -> bool:
        return num % 2 != 1

    num = int(input("Please enter the number you'd like to test the evenness of:  "))

    print(f"is_even({num}) = {is_even(num)}")


def assignment4_a_6():
    def greater_than(num1: int, num2: int):
        return num1 > num2

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    print(f"greater_than({num1}, {num2}) = {greater_than(num1, num2)}")


def assignment4_a_7():
    def conglom(*nums):
        return sum(nums)

    num_list = [1, 6, 7, 2, 45, 234, 34, 26]
    print(f"Orig list: {num_list}")
    print(f"Summed: {conglom(num_list)}")


def assignment4_a_8():
    def filter_evens(*nums):
        return [n for n in nums if n % 2 == 0]

    num_list = [1, 6, 7, 2, 45, 234, 34, 26]
    print(f"Orig list: {num_list}")
    print(f"Filtered: {filter_evens(num_list)}")


def assignment4_a_9():
    def camel_catastrophe(text: str):
        result = ""
        for i in range(0,len(text)):
            if (i+1) % 2 == 1:
                result += text.upper()[i]
            else:
                result += text.lower()[i]

        return result

    line = input("Please enter the string you'd like to morph:  ")
    print(camel_catastrophe(line))


def assignment4_a_10():
    def complex_comparison(num1: int, num2: int) -> int:
        if num1 % 2 == 0 and num2 % 2 ==0:
            if num1 < num2:
                return num1
            else:
                return num2
        else:
            if num1 > num2:
                return num1
            else:
                return num2

    num1 = int(input("Please enter the first number you'd like to test: "))
    num2 = int(input("Please enter the second number you'd like to test: "))

    print(f"The result of our complex comparison is: {complex_comparison(num1, num2)}")


def assignment4_a_11():
    def start_the_same(text1: str, text2: str) -> bool:
        return text1.lower()[0] == text2.lower()[0]

    word1 = input("Please enter the first word you'd like to compare: ")
    word2 = input("Please enter the second word you'd like to compare: ")

    if start_the_same(word1, word2):
        print("The two words start the same!")
    else:
        print("These words start differently.")


def assignment4_a_12():
    def twice_the_other_side_of_seven(num: int) -> int:
        diff = num - 7
        return 7 + 2 * diff

    number = int(input("Please enter the number you'd like to calculate from: "))
    print(f"The number twice this side of seven is: {twice_the_other_side_of_seven(number)}")


def assignment4_a_13():
    def pre_determined_cameling(word: str) -> str:
        result = ""
        for i in range(0, len(word)):
            if i == 0 or i == 3:
                result += word.upper()[i]
            else:
                result += word[i]

        return result

    line = input("Please enter the word you'd like to disfigure:  ")
    print(pre_determined_cameling(line))


def main():
    print("Welcome to the Assignment 4.a runner created by Sean Horner")
    selection = -1
    print("\n")

    while selection != 0:
        print("")
        print("********************************************")
        print("*  1) Run question 1                       *")
        print("*  2) Run question 2                       *")
        print("*  3) Run question 3                       *")
        print("*  4) Run question 4                       *")
        print("*  5) Run question 5                       *")
        print("*  6) Run question 6                       *")
        print("*  7) Run question 7                       *")
        print("*  8) Run question 8                       *")
        print("*  9) Run question 9                       *")
        print("* 10) Run question 10                      *")
        print("* 11) Run question 11                      *")
        print("* 12) Run question 12                      *")
        print("* 13) Run question 13                      *")
        print("*                                          *")
        print("*  0) Exit the program                     *")
        print("********************************************")
        print("")

        # add try/except handling
        selection = int(input("Please enter your choice:   "))

        if selection == 1:
            assignment4_a_1()
        elif selection == 2:
            assignment4_a_2()
        elif selection == 3:
            assignment4_a_3()
        elif selection == 4:
            assignment4_a_4()
        elif selection == 5:
            assignment4_a_5()
        elif selection == 6:
            assignment4_a_6()
        elif selection == 7:
            assignment4_a_7()
        elif selection == 8:
            assignment4_a_8()
        elif selection == 9:
            assignment4_a_9()
        elif selection == 10:
            assignment4_a_10()
        elif selection == 11:
            assignment4_a_11()
        elif selection == 12:
            assignment4_a_12()
        elif selection == 13:
            assignment4_a_13()
        elif selection == 0:
            continue
        else:
            print("That wasn't an acceptable option, please try again.")

        print("\n")
        input("Press enter to continue")

    print("\n\n~~~ Thanks for checking my assignment work :D! ~~~")


if __name__ == "__main__":
    main()
