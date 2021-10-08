
def bmi_calculator(weight: int, height: float) -> float:
    return weight/(height * height)


def bmi_assessor(bmi: float) -> str:
    if bmi >= 30.0:
        return "obese"
    elif bmi >= 25.0:
        return "over"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "under"


def main():
    results = ""
    runs = int(input("Enter the number of people in the assessment: "))
    for i in range(0, runs):
        line = input("Enter the person's weight (in kg) and height (in m), space-separated: ")
        weight = int(line.split()[0])
        height = float(line.split()[1])

        results += f"{bmi_assessor(bmi_calculator(weight, height))} "

    print("")
    print("answer:")
    print(results)


if __name__ == "__main__":
    main()