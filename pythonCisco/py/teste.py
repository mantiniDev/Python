try:
    print((""/0))
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")
    
print(3 * 'abc' + 'xyz')

print(ord('c') - ord('a'))

print(chr(ord('z')-2))

assert var == 0
