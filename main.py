# from subprocess import call

# call(["python", "src/week0/week0_menu.py"])

# call(["python", "src/week1/week1_menu.py"])

# call(["python", "src/week2/week2_menu.py"])


# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from src.week0 import ship
from src.week0 import icecream
from src.week0 import catanim
from src.week0 import christmastree
from src.week0 import keypad
from src.week0 import swap
from src.week1 import fibonacci
from src.week2 import factorial
from src.week2 import mathfunction


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()


main_menu = [
    ["Swap", swap.driver],
    ["Keypad", keypad.matrix],
    ["Family", None],
    ["Fibonacci", fibonacci.driver],
    ["Factorial", factorial.driver],
    ["Math Function", mathfunction.driver],
]


# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Cat", catanim.ship],
    ["Icecream", icecream.ship],
    ["Christmas Tree", christmastree.driver],
    ["Ship", ship.ship],
]



# for_loop(a,b)
# while_loop(a,b)
# recursive_loop(0,a,b)


# sub_menu[0][2] = call(["python", "catanim.py"])
# try:
#   choice = int(choice)
# #   if choice == 4:
# call(["python", "ship.py"])
# #   return
# # call(["python", "icecream.py"])
# call(["python", "catanim.py"])


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)


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