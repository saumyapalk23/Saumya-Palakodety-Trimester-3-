  
{% include navigation.html %}

**_Challenges_**
  
| Links to Runtime (Github and Repl)
 --------------------------------- | 
| <a href="https://replit.com/join/afjdfnnhak-saumyapalak" target="_blank">Repl.it &</a>   <a href="https://github.com/sarayu-pr11/saas/commit/9e1e93a73865b5de75014f07e9dc212a8dd49151" target="_blank">Github Commits</a> |

 <div>
 
<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@saumyapalak/CSChallenges?lite=true#src/main.py"></iframe>



  
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
Family.append({
              "Pets": "None",  
              "Near_Parks": "Trent",  
              "DOBs": ["August 26", "September 28", "April 5", "November 21"]  ,
              "Cousins": ["Siva","Harini", "Pranav", "Nithya"],  
              "Emails":["saumyp3@gmail.com", "ravips1@gmail.com", "k_palakodety@yahoo.com","shreya.palakodety@gmail.com"]  
              })

a = input("Type key: " )
b = input("Type value: " )


def for_loop(key, value):
  for data in Family:
    if(data[key]) == value:
      print(data[key])
      return
for_loop(a,b)

def while_loop(key, value):
  i = 0
  while i < len(Family):
    if (Family[i][key] == value):
      print(Family[i][key])
      return
   i +=1
while_loop(a,b)

def recursive_loop(i, key, value):
  if (i < len(Family)):
    if (Family[i][key] == value):
      print(Family[i][key])
      return
    i += 1
    recursive_loop(i, key, value)
  return
recursive_loop(0,a,b)

```

**Fibonacci**

```
nterms = int(input("Display term #: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   raise Exception ("Try again with a positive number.")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
 ```


**Menu/Submenu**
  
```
  main_menu = [
    ["Swap", "swap.py"],
    ["Keypad", "keypad.py"],
]
# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Cat", "catanim.py"],
    ["Icecream", "icecream.py"],
    ["Christmas", "christmastree.py"]
] 
 ```
  
 **One Animation (Ice Cream):**
  ```
  #icecream animation
#prefuncy.py
import time
import os

Color34 = "\u001b[34m"
Color37 = "\u001b[37m"


# As you can see, its not very optimal 
def icecream1():
    print(" (----)")
    print(" (    )")
    print("  \__/ ")
    print("   \/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream2():
    print("    (----)")
    print("    (    )")
    print("     \__/ ")
    print("      \/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream3():
    print("      (----)")
    print("      (    )")
    print("       \__/ ")
    print("        \/ ")
  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream4():
    print("     (----)")
    print("     (    )")
    print("      \__/ ")
    print("       \/ ")
  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream5():
    print("       (----)")
    print("       (    )")
    print("        \__/ ")
    print("         \/ ")
  
print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream6():
    print("             (----)")
    print("             (    )")
    print("              \__/ ")
    print("               \/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream7():
    print("     (----)")
    print("     (    )")
    print("      \__/ ")
    print("       \/ ")
  

print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ic8cream8():
    print("           (----)")
    print("           (    )")
    print("            \__/ ")
    print("             \/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream9():
    print("               (----)")
    print("               (    )")
    print("                \__/ ")
    print("                 \/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream10():
    print("         (----)")
    print("         (    )")
    print("          \__/ ")
    print("           \/ ")
  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream11():
    print("            (----)")
    print("         (    )")
    print("             \__/ ")
    print("           \/ ")
  
print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream12():
    print("             (----)")
    print("        (    )")
    print("            \__/ ")
    print("         \/ ")
  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream13():
    print("                (----)")
    print("       (    )")
    print("                  \__/ ")
    print("         \/ ")  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream14():
    print("                (----)")
    print("      (    )")
    print("               \__/ ")
    print("        \/ ")  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream15():
    print("                     (----)")
    print("       (    )")
    print("                     \__/ ")
    print("         \/ ")  

print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream16():
    print("                 (----)")
    print("       (    )")
    print("                   \__/ ")
    print("         \/ ")  
print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream17():
    print("            (----)")
    print("      (    )")
    print("                 \__/ ")
    print("           \/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ice18ream18():
    print("         (----)")
    print("         (    )")
    print("          \__/ ")
    print("           \/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def icecream19():
    print("             (----)")
    print("             (    )")
    print("              \__/ ")
    print("               \/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def icecream20():
    print("                  (----)")
    print("                  (    )")
    print("                   \__/ ")
    print("                    \/  ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


os.system("cls")
time.sleep(.1)
ship1()
time.sleep(.5)
os.system("cls")
ship2()
time.sleep(.5)
os.system("cls")
ship3()
time.sleep(.5)
os.system("cls")
ship4()
time.sleep(.5)
os.system("cls")
ship5()
time.sleep(.5)
os.system("cls")
ship6()
time.sleep(.5)
os.system("cls")
ship7()
time.sleep(.5)
os.system("cls")
ship8()
time.sleep(.5)
os.system("cls")
ship9()
time.sleep(.5)
os.system("cls")
ship10()
time.sleep(.5)
os.system("cls")
ship11()
time.sleep(.5)
os.system("cls")
ship12()
time.sleep(.5)
os.system("cls")
ship13()
time.sleep(.5)
os.system("cls")
ship14()
time.sleep(.5)
os.system("cls")
ship15()
time.sleep(.5)
os.system("cls")
ship16()
time.sleep(.5)
os.system("cls")
ship17()
time.sleep(.5)
os.system("cls")
ship18()
time.sleep(.5)
os.system("cls")
ship19()
time.sleep(.5)
os.system("cls")
ship20()
time.sleep(.5)
os.system("cls")
print("or so you thought...")
time.sleep(.5)
os.system("cls")

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
row = int(input('Enter number of rows: '))

christmastree(row)
trunk (row)

  ```
  
