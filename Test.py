for i in range(1,10):
    for j in range(1, i + 1):
        print("{0}*{1}={2}".format(i, j, i*j), end="\t")
    print()



l1 = {"name":"A", "age":1, "location":"北京"}
l2 = {"name":"B", "age":100, "location":"北京"}
l3 = {"name":"C", "age":70, "location":"北京"}
array = [l1,l2,l3]

print(type(l1))
for i in array:
    if(i.get("age") > 50):
        print(i)


