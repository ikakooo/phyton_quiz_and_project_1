a_and_b = ()
inputed = input()
inputedTuple = tuple(inputed.split(','))

for i in inputedTuple:
    if "a" in i or "b" in i:
         a_and_b+=(i,)
print(a_and_b)