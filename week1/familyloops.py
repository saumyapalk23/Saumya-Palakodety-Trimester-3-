Family = []
# List with dictionary records placed in a list
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
              "DOBs": ["August 26", "September 28", "April 5", "November 21"],
              "Cousins": ["Siva","Harini", "Pranav", "Nithya"],  
              "Emails":["saumyp3@gmail.com", "ravips1@gmail.com", "k_palakodety@yahoo.com","shreya.palakodety@gmail.com"]  
              })

print (Family)


a = input("Enter key: " )
b = input("Enter value: " )

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


