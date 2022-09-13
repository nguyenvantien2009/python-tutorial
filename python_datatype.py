print(f'''
    There are 15 data types. They are grouped to 8 groups in python.
        1. NoneType: None Type
        2. Binary Types: bytes, bytearray, memoryview
        3. Boolean Type: bool
        4. Text Type: str 
        5. Numberic: int, float, complex
        6. Sequence Types: list, tuple, range
        7. Set Type: set, frozenset
        8. Map Type: dict
''')


print(f'''
    Data Type of variable will be auto set when assignee value.
    Egs: x = 'Name' (data type of x variable is str)
''')

print(f'''As you can see type of x variable will be changed after assignee value to it''')

x = 'Name'
print(type(x))

x = 12
print(type(x))

## Type of value when assignee value with data type.
print(f'We are also define of variable when assingee value with casting function value.')
x = str('2'); print(type(x))
x = float(2); print(type(x))