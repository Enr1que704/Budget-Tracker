

def main():
    print('Welcome to the Budget Tracker! Please choose an option below to begin.')
    result = ""
    go = True
    while go:
        print('(1) Create a new budget\n')
        print('(2) View a current budget\n')
        print('(3) View a past budget\n')
        print('(4) Edit a current budget\n')
        result = input('Enter your choice (1-4): ')
        
        if result.isdigit() and 1 <= int(result) <= 4:
            go = False
        else:
            print('Invalid input. Please enter a number between 1 and 4.')

    if result == 1:
        print(1)
    elif result == 2:
        print(2)
    elif result == 3:
        print(3)
    elif result == 4:
        print(4)


main()

