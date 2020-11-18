# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

cities = {}
while True:
    print("When done, type 'done'")
    a = input("Pick an American city: ")
    if a == "done":
        break
    b = input("What state is that city in?: ")
    if b == "done":
        break
    cities[a] = b



for key_name, value_name in cities.items():
    print(key_name, value_name)