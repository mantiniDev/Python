income = float(input("Enter the annual income: "))
imposto = 0.18

if income > 85.828:
    tax = (income*imposto)-556
else:
    val = income - 85.828
    tax = 14.839 + (0.32*val)
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
