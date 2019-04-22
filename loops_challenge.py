# Challenge: Loop and Conditionals
my_numbers = range(0,100)
for i in my_numbers:
    if (i%2!=0) and i!=57:
        print(i)

# Challenge: Longest Name
names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']
array=[]
# for loop
for name in names:
    array.append(len(name))   
    print(array)

for name in names:
    if len(name)==max(array):
        print(f"hello {name}")

# while loop
names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']
array = []
i=0
while i<len(names):
    array.append(len(names[i]))
    i+=1

x=0
while x<len(names):
    if max(array)==len(names[x]):
        print(names[x])
    x+=1



