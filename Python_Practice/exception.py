try:
   x = int(input("Please enter a small positive integer: "))
   print("x =", x)
except ValueError:
   print("Input cannot be parsed as an integer")
