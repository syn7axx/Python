import random
#random username generator

print("--Press any key to generate--")
names = ["devil", "dark", "matrix", "hero", "super", "blood", "hellx", "hunter", "solo", "dart", "unstopable", "arise", "bloody", "rizz", "delta", "doom", "Whero", "lynx","shadow","shade","colorless","spidy","unreal","fake","dirt","holo"]
surnames = ["soul","pro","hero","brine","w","chad","devil","angel"]
middle = str(random.randint(999,9999))
ends = ["l","w","z","y","t","i","m","n","d","s","k"]
username = random.choice(names) + random.choice(surnames) + middle +  random.choice(ends)
start = str(input("      "))
start = start.lower()
print("")
if not start or start:
    print("----", username, "----")

