 
{% include navigation.html %}


**_Code Snippets From Challenges_**

**Lists/Loops**

```
Family = []
Family.append({
               "Mom": "Kalpana",  
               "Dad": "Ravi",  
               "Children": ["Saumya","Shreya"],
               "Residence": "San Diego" , 
               "Population":"4" 
              })


def print_data(n):
    print(Family[n]["Mom"], Family[n]["Dad"]) 
    print(Family[n]["Children"])
    print(Family[n]["Residence"])
    print(Family[n]["Population"])
    # print(Family[n]["Pets"])  
    # print(Family[n]["Near_Parks"])
    # print(Family[n]["DOBs"])
    # print(Family[n]["Cousins"])
    # print(Family[n]["Emails"])
    print()

 
def for_loop():
  for data in Family:
    print(data)
  return

def while_loop(n):
  while n < len(Family):
        print_data(n)
        n += 1
  return

def recursive_loop(n):
  if n < len(Family):
        print_data(n)
        recursive_loop(n + 1)
  return


def driver():
  for_loop()
  while_loop(0)
  recursive_loop(0)



```

  
  
  
  
**Fibonacci**

```
def driver():

  terms = int(input("How many terms? "))

  n1, n2 = 0, 1
  count = 0

  if terms <= 0:
     print("Please enter a positive integer")
  elif terms == 1:
      print("Fibonacci sequence upto",nterms,":")
      print(n1)

  else:
     print("Fibonacci sequence:")
     while count < terms:
         print(n1)
         nth = n1 + n2
       
         n1 = n2
         n2 = nth
         count += 1
 ```
  

**Menu/Submenu**
  
```
from src.week0 import ship
from src.week0 import icecream
from src.week0 import catanim
from src.week0 import christmastree
from src.week0 import keypad
from src.week0 import swap
from src.week1 import fibonacci
from src.week2 import mathfunction
from src.week1 import familyloops



main_menu = [
    ["Swap", swap.driver],
    ["Keypad", keypad.matrix],
    ["Family", familyloops.driver],
    ["Fibonacci", fibonacci.driver],
    ["Factorial", "src/week2/factorial.py"],
    ["Math Function", mathfunction.driver],
]



sub_menu = [
    ["Cat", catanim.ship],
    ["Icecream", icecream.ship],
    ["Christmas Tree", christmastree.driver],
    ["Ship", ship.ship],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()
 ```
  
 **One Animation (Ice Cream):**
  ```
  import time
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
def ocean_print():
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)

def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp+ " (----)")
    print(sp + " (    )")
    print(SHIP_COLOR, end="")
    print(sp + "  \__/ ")
    print(sp + "   \/ ")
    print(RESET_COLOR)

def ship():
    ocean_print()
    start = 0  
    distance = 60 
    step = 2  
    for position in range(start, distance, step):
        ship_print(position)  
        time.sleep(.1)
        
if __name__ == "__main__":
    ship()


  ```
  
**Christmas Tree**
  ```
  #christmastree
def christmastree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end='*')
        print(' ')


def trunk(n):
  for i in range(n):
    for j in range(n-1):
      print(' ', end =' ')
    print('* * *')
  # Input and Function Call


def driver():
  row = int(input('Enter number of rows: '))
  christmastree(row)
  trunk (row)

  ```
  
  **Math Function (Prime Numbers)**
  
  ```
  min = 2
max = 200

class primeNumbers:
    def __init__(self):
        pass
    def __call__(self, min, max):
      print("Here are OOP results:")
      for Number in range(min, max + 1):
              count = 0
              for i in range(2, (Number // 2 + 1)):
                  if (Number % i == 0):
                      count = count + 1
                      break
              if (count == 0 and Number != 1):
                  print(" %d" % Number, end='  ')

def driver():
  primes_of = primeNumbers() # object instantiation and run __init__ method
  print(primes_of(min, max)) # object running __call__ method
  
  ```
  
  **Swap**
  ```
  
# # # Write a python program to print a 3x3 formatted matrix as shown below, using lists and nested loops.
# # # Make note of 2d array, loop/iteration and zero based counting.
# # # matrix = [ [1,2,3],[4,5,6],[7,8,9] ] #write a function to output the formatted matrix :
# # # 1 2 3
# # # 4 5 6
# # # 7 8 9

# # matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

# # print each sublist in new row
# # for row in matrix:
# #   print (row, sep=',')
# # a = matrix[0
# # print(a)

# a = matrix[0][0], matrix[0][1], matrix[0][2]
# b = matrix[1][0], matrix[1][1], matrix[1][2]
# c = matrix[2][0], matrix[2][1], matrix[2][2]
# print(*a, sep=" ")
# print(*b, sep=" ")
# print(*c, sep=" ")



# swaps numbers regardless of value
def swap1(age1,age2):
  temp = age1
  age1 = age2
  age2 = temp
  print("Swap 1 Result:")
  return age1,age2
  
#returns numbers lowest to highest  
def swap2(a, b):
  if a > b:
    b, a = a, b
  print("Swap 2 Result:")
  return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
  if age1 > age2:
    print ("Swap 3 Result:")
    return(age2, age1)
  else:
    print ("Swap 3 Result:")
    return(age1, age2)

# tests
def driver():
  print(16,20)
  print(9.134,4)
  print(swap1(16, 20))
  print(swap1(9.134, 4))
  print(swap2(16,20))
  print(swap2(9.134, 4))
  print(swap3(16,20))
  print(swap3(9.134, 4))
  ```
  
  **Keypad**
  ```
  
# # # Write a python program to print a 3x3 formatted matrix as shown below, using lists and nested loops.
# # # Make note of 2d array, loop/iteration and zero based counting.
# # # matrix = [ [1,2,3],[4,5,6],[7,8,9] ] #write a function to output the formatted matrix :
# # # 1 2 3
# # # 4 5 6
# # # 7 8 9

# # matrix = [ [1,2,3],[4,5,6],[7,8,9] ]

# # print each sublist in new row
# # for row in matrix:
# #   print (row, sep=',')
# # a = matrix[0
# # print(a)

# a = matrix[0][0], matrix[0][1], matrix[0][2]
# b = matrix[1][0], matrix[1][1], matrix[1][2]
# c = matrix[2][0], matrix[2][1], matrix[2][2]
# print(*a, sep=" ")
# print(*b, sep=" ")
# print(*c, sep=" ")



# swaps numbers regardless of value
def swap1(age1,age2):
  temp = age1
  age1 = age2
  age2 = temp
  print("Swap 1 Result:")
  return age1,age2
  
#returns numbers lowest to highest  
def swap2(a, b):
  if a > b:
    b, a = a, b
  print("Swap 2 Result:")
  return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
  if age1 > age2:
    print ("Swap 3 Result:")
    return(age2, age1)
  else:
    print ("Swap 3 Result:")
    return(age1, age2)

# tests
def driver():
  print(16,20)
  print(9.134,4)
  print(swap1(16, 20))
  print(swap1(9.134, 4))
  print(swap2(16,20))
  print(swap2(9.134, 4))
  print(swap3(16,20))
  print(swap3(9.134, 4))
  ```
  
