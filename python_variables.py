# Create variable
print('== Create variable.')
name = 'Tien Nguyen'
Name = 'Tien Nguyen 2'
print(f'Different between variable Name and name. {Name} & {name}')

print('-- Declare variables inline.')
a,b = 1,2 
print(a,b)

print('-- Unpack tuple to variables')
a, b = (1, 2)
print(a,b)

print('== Casting')
age = '2'
int_age = int(age)
float_age = float(age)
str_age = str(2)

print(int_age)
print(float_age)
print(str_age)

print('== Data Type')
print(type('2'))
print(type(2))
print(type(2.0))