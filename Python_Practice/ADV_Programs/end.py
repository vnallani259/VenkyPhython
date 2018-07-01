text = "Python is easy to learn."

result = text.endswith('easy to learn.')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)
