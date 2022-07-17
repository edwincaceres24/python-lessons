import sys

param=sys.argv[1]

alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
main__array= alphabet+numbers+symbols

password=[]

def chart_validator(__input__):
    __input__=__input__.lower()
    input_encripted = str(main__array.index(__input__)*(len(param)))
    password.append(input_encripted)
    return password

def encription(chart):
    encripted_password=""
    for chart in param:
        chart_validator(chart)
    print(f'Your password encription for {param} is:')
    print(encripted_password.join(password))

encription(param)


