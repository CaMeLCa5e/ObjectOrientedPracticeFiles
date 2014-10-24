#sets10.23.14.py

print set('my name is Jack and Jack is my name'.split())

a = set(['Jack', 'John', 'Bill'])
b = set(['John', 'Jill'])

print a.intersection(b)
print a.symmetric_difference(b)
print a.difference(b)
print a.union(b)
