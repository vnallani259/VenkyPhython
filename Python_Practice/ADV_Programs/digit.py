s = '23455'
print(s.isdigit())

#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())

# s = '½'
# fraction is not a digit
s = '\u00Bd'
print(s.isdigit())
