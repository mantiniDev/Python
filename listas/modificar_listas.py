beatles = []
print("Step 1:", beatles)

beatles.append("john lennon")
beatles.append("paul mccartney")
beatles.append("George Harrison")

print("\nStep 2:\n", beatles)

for i in range(2):
    beatles.append(input("adicione um nome: "))
print("\nStep 3:\n", beatles)

del beatles[-2]
del beatles[-1]
print("\nStep 4:\n", beatles)

beatles.insert(0,"Ringo Star")
print("\nStep 5:\n", beatles)


# testing list legth
print("\nThe Fab", len(beatles))