
# Three is a Crowd
def assignment2_c_1():

    def crowd_test(p_list):
        if len(p_list) > 3:
            print("Wow, this room is crowded!")

    people_list = ["Jim", "Carey", "Bonnie", "Hunter"]

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")

    print("Removing 2 people from the list...")
    people_list.pop()
    people_list.remove("Bonnie")

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")


# Three is a Crowd, pt. 2
def assignment2_c_2():
    def crowd_test(p_list):
        if len(p_list) > 3:
            print("Wow, this room is crowded!")
        else:
            print("This room isn't very crowded.")

    people_list = ["Jim", "Carey", "Bonnie", "Hunter"]

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")

    print("Removing 2 people from the list...")
    people_list.pop()
    people_list.remove("Bonnie")

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")


# Six is a Mob
def assignment2_c_3():
    def crowd_test(p_list):
        if len(p_list) > 5:
            print("There's a whole mob in this room!!")
        elif len(p_list) > 3:
            print("Wow, this room is crowded!")
        elif len(p_list) > 0:
            print("This room isn't very crowded.")
        else:
            print("This room is totally empty.")

    people_list = ["Jim", "Carey", "Bonnie", "Hunter", "Korvo", "Terry"]

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")

    print("Removing 2 people from the list...")
    people_list.pop()
    people_list.remove("Bonnie")

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")

    print("Removing 2 people from the list...")
    people_list.pop()
    people_list.remove("Carey")

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")

    print("Removing 2 people from the list...")
    people_list.pop()
    people_list.remove("Jim")

    print(f"Testing with people_list = {people_list}")
    print("result:")
    crowd_test(people_list)
    print("")


def main():
    print("\n")
    print("Running first iteration: Three is a Crowd")
    assignment2_c_1()
    print("")
    print("--------------------------------------------------")
    print("")

    print("Running second iteration: Three is a Crowd, part 2")
    assignment2_c_2()
    print("")
    print("--------------------------------------------------")
    print("")

    print("Running third iteration: Six is a Mob")
    assignment2_c_3()
    print("")


if __name__ == "__main__":
    main()