import sys

param=sys.argv[1]

alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]

password=""

def chart_validator(__input__):
    __input__=__input__.lower()
    if __input__ in alphabet:
        chart_input_encripted = alphabet.index(__input__)*(len(param))
        print(f'This is the chart encripted: {chart_input_encripted}')
        str(chart_input_encripted)
        password=password+chart_input_encripted
        return print(password)
    elif __input__ in numbers:
        int_input_encripted=numbers.index(__input__)*(len(param))
        print(f'This is an int: {int_input_encripted}')
        str(int_input_encripted)
        password=password+int_input_encripted
        return print(password)
    else:
        return print("Not found")

def encription(chart):
    for chart in param:
        chart_validator(chart)

encription(param)


#Concat each encripted value into a variable
