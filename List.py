#   Add items to the end of a list
suitcase = [] 
suitcase.append("sunglasses")

suitcase.append('cup')
suitcase.append('phone')
suitcase.append('wallet')



list_length = len(suitcase) # Set this to the length of suitcase


#   A portion of a list.

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]                # Third and fourth items (index two and three)
last   = suitcase[(len(suitcase)-2):(len(suitcase))]  


#   Slice a string
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end


#    Index and Insert
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =animals.index("duck")   # Use index() to find "duck"

animals.insert(duck_index,"cobra")

animals.remove("duck")


# List & Loop

start_list = [5, 3, 1, 2, 4]
square_list = [1,2,3,4,5] # it's required to make i work
#square_list[0]=1
print square_list
# Your code here!
for n in start_list:
    i=start_list.index(n)
    square_list[i]=n**2
    #print start_list.index(n)

square_list.sort()

print square_list



# Dictionary Key not list
residents={} #empty dictionary

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # residents[0] index doesn't work
print residents["Sloth"]
print residents["Burmese Python"]


del residents["Sloth"]  #Case sensitive

for x in residents:
	print residents[x]


#Dictonary List Example

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket']=['seashell', 'strange berry', 'lint']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort()
# Your code here
inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold']+50




################################################

def fizz_count(list):
    total=0
    for x in list:
        if x=='fizz':
            total=total+1
    return total


print fizz_count(["fizz","cat","fizz"])



################################################


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total=0
    for n in food:
        if stock[n]>0:
            total=total+prices[n]
            stock[n]=stock[n]-1
    return total
    
print compute_bill(shopping_list)