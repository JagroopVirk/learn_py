list1 = []
list2 = ["one", "two", "threee"]
list3 = [["item1", "item2", "item3"], [9, 8, 6]]

list1.append(1)
list1.append(2)
list1.append(3)

list2[2] = ["three"]
list3[1][2] = 7

print(list2[2])
print()
print(list3[1][2])
print()
print(list1)
print()
print(list1 + list2 + list3)