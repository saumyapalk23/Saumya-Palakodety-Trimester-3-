from week0 import catanim, christmastree, icecream, keypad, ship, swap
from week1 import familyloops, fibonacci
from week2 import factorial, mathfunction


main_menu = [
    # ["Week O", "week0/week0_menu.py"],
    # ["Week 1", "week1/week1_menu.py"],
      ["Week 2", "week2/week2_menu.py"],

  
]

sub_menu = [
    # ["Week O", "week0/week0_menu.py"],
    # ["Week 1", "week1/week1_menu.py"],
      ["Week 2", "week2/week2_menu.py"],

  
]

# math_menu = [
#     ["Factors", mathfunction.factors],
#     ["GCD", mathfunction.gcd],
#     ["LCM", mathfunction.lcm],
#     ["Primes", mathfunction.primes],
# ]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
