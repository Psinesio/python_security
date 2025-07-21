import itertools

string = input("Enter a string: ")

result = itertools.permutations(string, len(string))

for i in result:
    print("".join(i))
