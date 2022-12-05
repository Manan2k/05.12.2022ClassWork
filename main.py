a_list = [3, 5, 6, 12]
print(a_list[1:])
a_reversed = [a_list]
for i in range(len(a_list)):
    a_reversed.append(a_list[len(a_list) - i - 1])
    print(a_reversed)
