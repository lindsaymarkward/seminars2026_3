# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove? ")
# while name_to_remove != "":
#     # print(name_to_remove)
#     try:
#         names.remove(name_to_remove)
#         print(f"{name_to_remove} removed")
#     except ValueError:
#         print(f"{name_to_remove} is not in the list")
#     name_to_remove = input("Who do you want to remove? ")
# print(", ".join(names))
#
# # DISINFORMATION! i is not an index but we think it is :(
# for i in names:
#     print(names[i])

# Derek       =   7
# Xavier      =  80
# Bob         = 612
# Chantanelle =   9
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanellie', 9]]
# width = 0
# for pair in data:
#     if len(pair[0]) > width:
#         width = len(pair[0])
# print(width)
width = max(len(pair[0]) for pair in data)
print(width)
for pair in data:
    print(f"{pair[0]:{width}} = {pair[1]:3}")
