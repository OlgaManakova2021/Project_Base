# # добавить название цвета если его нет во множестве
#
# colors = {"red", "green", "blue"}
# if "yellow" not in colors:
#     colors.add("yellow")
# print(colors)


#
colors = {'yellow', 'red', 'green', 'blue'}
colors.discard("yellow")
print(colors)