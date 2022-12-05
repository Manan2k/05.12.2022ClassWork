tupleList = [ (), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d') ]
Conversion = list(tupleList)

output_list = []
for i in Conversion:
    if i != ():
        output_list.append(i)

print(output_list)