
def assignment2_a_1():
    print([c for c in "Hello World" if c == 'r'])
    print('Hello World'[-3])
    print("Hello World"[8])


def assignment2_a_2():
    word = "thinker"
    print(word[2:6])

    print("Technically, h[1] would give an error.")
    print("But S[1] would return 'e'.")


def assignment2_a_3():
    print("The output of s[2:] would be starting at the second character in the")
    print("string and going until the end. This would equate to 'mmy'.")


def assignment2_a_4():
    def is_palindrome(word: str) -> str:
        scrubbed_word = [c for c in word.lower() if c.isalpha()]
        for i in range(0, int(len(scrubbed_word)/2)):
            if scrubbed_word[i] != scrubbed_word[-(i+1)]:
                return 'N'

        return 'Y'

    result = ""
    num_of_trials = int(input("Please input the number of words to test: "))
    for i in range(0, num_of_trials):
        test_word = input("Please enter the word or phrase to test: ")
        result += is_palindrome(test_word) + " "

    print("")
    print("answer:")
    print(result[:-1])


def main():
    print("Now running sub-assignment 1")
    assignment2_a_1()

    print("Now running sub-assignment 2")
    assignment2_a_2()

    print("Now running sub-assignment 3")
    assignment2_a_3()

    print("Now running sub-assignment 4")
    assignment2_a_4()


if __name__ == '__main__':
    main()
