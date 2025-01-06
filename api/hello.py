# Me dusting off the rust by doing some string stuff.

print("Hello World!")
i = 0;
while i < 10:
    print("Hello " + str(i))
    i = i + 1
for j in range(10):
    print("Hello range " + str(j))
ar = ["this", "is", "a", "demo"]
for word in ar:
    print("word " + word)
ar.append("again")
ar.insert(0, "hello")
for word in ar:
    print("two " + word)
ar.remove("again")
ar.reverse()
print(ar)
for temp in range(1, len(ar) + 1):
    print(ar[-temp])
