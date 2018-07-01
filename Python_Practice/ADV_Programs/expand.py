str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8

result = str.expandtabs()

print(result)
print('Tabsize 3:', str.expandtabs(3))

# tabsize# tabsize is set to 2
 #is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))
