
def assignment4_b_1():
    # List( List(order_number, title_and_author, quantity, price_per), List(...
    order_list = [
        [34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3, 32.95],
        [88112, "Einführung im Python3, Bernd Klein", 3, 24.99]
    ]

    def double_tuple(o_list):
        return map(lambda row: (row[0], row[2] * row[3]), o_list)

    for item in double_tuple(order_list):
        print(item)


def assignment4_b_2():
    # List( List(order_number, title_and_author, quantity, price_per), List(...
    order_list = [
        [34587, ("SKU52534", 4, 40.95), ("SKU256126", 10, 12.65)],
        [98762, ("SKU51345", 5, 56.80), ("SKU14515", 3, 32.95)],
        [77226, ("SKU14515", 3, 32.95), ("SKU52534", 4, 40.95)],
        [88112, ("SKU613451", 3, 24.99), ("SKU513461", 6, 26.50)]
    ]

    def order_totaling(o_list):
        result_list = []
        for row in o_list:
            grand_total = 0
            sub_num = len(row)-1

            for i in range(1, sub_num):
                grand_total += row[i][1] * row[i][2]

            result_list.append((row[0], grand_total))

        return result_list

    for item in order_totaling(order_list):
        print(item)


def main():
    print("Welcome to the Assignment 4.b runner created by Sean Horner")
    selection = -1
    print("\n")

    while selection != 0:
        print("")
        print("********************************************")
        print("*  1) Run question 1                       *")
        print("*  2) Run question 2                       *")
        print("*                                          *")
        print("*  0) Exit the program                     *")
        print("********************************************")
        print("")

        # add try/except handling
        selection = int(input("Please enter your choice:   "))

        if selection == 1:
            assignment4_b_1()
        elif selection == 2:
            assignment4_b_2()
        elif selection == 0:
            continue
        else:
            print("That wasn't an acceptable option, please try again.")

        print("\n")
        input("Press enter to continue")

    print("\n\n~~~ Thanks for checking my assignment work :D! ~~~")


if __name__ == "__main__":
    main()
