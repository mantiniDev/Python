secret_number = 20

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

numero = int(input("Digite um numero secreto: "))

while numero != secret_number:
    print("Ha ha! You're stuck in my loop!")
    numero = int(input("Digite um numero secreto: "))
    if numero == secret_number:
        print (secret_number)
        print ("Well done, muggle! You are free now.")

