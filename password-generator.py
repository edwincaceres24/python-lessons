import sys

param=sys.argv[1]

alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=[0,1,2,3,4,5,6,7,8,9]


def chart_validator(__input__):
    __input__=__input__.lower()
    if __input__ in alphabet :
        print(f'This is the chart: {__input__}')
        return str
    elif __input__ in numbers:
        print(f'This is an int: {__input__}')
        return int
    else:
        return print("Not found")

def encription(chart):
    for chart in param:
        chart_validator(chart)

encription(param)
