
def assignment2_b_1():
    multi_type_list = [100, "potato", 2.65]
    print(multi_type_list)


def assignment2_b_2():
    nested_list = [1, 1, [1, 2]]
    print("Ro get the 2 out of the nested array, the inner-array's position in the outer-array,")
    print("then the index of the 2 in the inner-array, like so:")
    print(f"nested_list[2][1] = {nested_list[2][1]}")


def assignment2_b_3():
    print("lst = ['a', 'b', 'c', 'd'] --> lst[1:] = ['b', 'c', 'd']")


def assignment2_b_4():
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    for value in weekdays.items():
        print(value)


def assignment2_b_5():
    print("The output would be the second element of the array at dictionary key 'k1', i.e. 2")
    dictionary = {'k1': [1, 2, 3]}
    print(f"dictionary['k1'][1] = {dictionary['k1'][1]}")


def assignment2_b_6():
    print("Yes, tuples can contain ints and even lists. In fact, lists inside tuples can be mutated,")
    print("even though they exist inside an immutable object. This is because the tuple itself has no")
    print("way of knowing if its elements are mutable, it just maintains pointers to memory locations.")


def assignment2_b_7():
    state = "Mississippi"
    char_set = set(state)
    print(char_set)


def assignment2_b_8():
    print("Yes you can, since 'x' isn't already in the set.")


def assignment2_b_9():
    print("Output of set([1, 1, 2, 3]) = {1, 2, 3}")
    print(f"set([1, 1, 2, 3]) = {set([1, 1, 2, 3])}")


def main():
    print("Running assignment 1")
    assignment2_b_1()
    print("")

    print("Running assignment 2")
    assignment2_b_2()
    print("")

    print("Running assignment 3")
    assignment2_b_3()
    print("")

    print("Running assignment 4")
    assignment2_b_4()
    print("")

    print("Running assignment 5")
    assignment2_b_5()
    print("")

    print("Running assignment 6")
    assignment2_b_6()
    print("")

    print("Running assignment 7")
    assignment2_b_7()
    print("")

    print("Running assignment 8")
    assignment2_b_8()
    print("")

    print("Running assignment 9")
    assignment2_b_9()
    print("")


if __name__ == '__main__':
    main()