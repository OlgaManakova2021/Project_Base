class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_values(self):
        print(f"{self.age = }")
        print(f"{self.name = }")

import pickle

with open("User.bin", "wb") as file:
    pickle.dump(User, file)

with open("User.bin", "rb") as file:
   user = pickle.load(file)

# print(id(user), id(User))

Max = user(10, "Max")
# print(Max.age)
# print(Max.name)
Max.get_values()

Tom = user(15, "Tom")
# print(Tom.age)
# print(Tom.name)
Tom.get_values()

