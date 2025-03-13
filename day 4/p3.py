my_name = 'aaryaadesh'

print(my_name)
print(my_name.upper())
try:
    print(my_name.index('tt'))
except ValueError:
    print(f'the sub-string\'tt\' not foumd in {my_name}')
print(my_name.capitalize)
print(my_name.find('tt'))