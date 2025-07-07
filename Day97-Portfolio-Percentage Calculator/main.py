import time

def clear_screen():
    # Clears the terminal by printing many newlines to simulate a "clear screen"
    clear = "\n" * 100
    print(clear)

def percent_of_num():
    # Calculate "What is x% of y?"
    print("You chose option #1 - What is x % of y?\n")
    x = float(input("What is the value of x?: "))  # Percentage value
    y = float(input("What is the value of y?: "))  # Base number
    # Compute (x% of y) = (x * y) / 100
    answer = f"\n{x} is {(x * y) / 100}% of {y}\n"
    print(answer)
    another_calc()

def num_percent_of_num():
    # Calculate "x is what % of y?"
    print("You chose option #2 - x is what % of y?\n")
    x = float(input("What is the value of x?: "))  # Part value
    y = float(input("What is the value of y?: "))  # Whole value
    # Compute (x/y)*100 to get the percentage
    answer = f"\n{x} is {(x * 100) / y}% of {y}\n"
    print(answer)
    another_calc()

def percent_num_to_num():
    # Calculate "% increase or decrease from x to y"
    print("You chose option #3 - What is the % increase/decrease from x to y?\n")
    x = float(input("What is the value of x?: "))  # Original number
    y = float(input("What is the value of y?: "))  # New number
    # Determine increase or decrease and calculate percentage change
    if x > y:
        diff_percent = -((x - y) / x) * 100
        answer = f"\nThere is a {diff_percent:.2f}% decrease from {x} to {y}\n"
    else:
        diff_percent = ((y - x) / x) * 100
        answer = f"\nThere is a {diff_percent:.2f}% increase from {x} to {y}\n"
    print(answer)
    another_calc()

def another_calc():
    # Prompt user to perform another calculation or exit
    response = input("\nWould you like to perform another calculation? (Y/N): ")
    if response.lower() == "y":
        clear_screen()
        main()
    elif response.lower() == "n":
        clear_screen()
        print("Thanks for using the Percentage Calculator!")
    else:
        clear_screen()
        print("Choose a valid answer!\n")
        time.sleep(2)
        clear_screen()
        another_calc()

def main():
    # Main menu - presents calculation options to the user
    print("Types of calculations:\n")
    print("1. What is x % of y?\n"
          "2. x is what % of y?\n"
          "3. What is the % increase/decrease from x to y?\n")

    choice = input("Select a calculation from 1-3: ")
    if choice == "1":
        clear_screen()
        percent_of_num()
    elif choice == "2":
        clear_screen()
        num_percent_of_num()
    elif choice == "3":
        clear_screen()
        percent_num_to_num()
    else:
        clear_screen()
        print("Choose a valid answer!\n")
        time.sleep(2)
        clear_screen()
        main()

print("Welcome to the Percentage Calculator!\n")
main()
