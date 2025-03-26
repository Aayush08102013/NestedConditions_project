#variable:
age = input("Is your age 10>= and =<20,: yes or no: ")
# if esle conditions:
y = "yes" 
n = "no"
#nested condition:
#yes:
if age == y:
    print("You're allowed in Rajs class :)")
    age2= int(input("Enter youre age: "))
    if age2 >= 10 and age2 <= 12:
        print("youre a tween in Rajs class")
    if age2 >= 13 and age2 <= 18:
        print("youre a teenager in Rajs class")
    if age2 >= 19 and age2 <= 20:
        print("youre a young adult in Rajs class")
#no:
elif age == n:
    print("youre NOT allowed in Rajs class")
