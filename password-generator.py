# input = "ALA"
# It searches around the character and become it into a special character
# Create function to encrypt str
# Create function to encrypt ints
import sys

param=sys.argv[1]
chart_variable = "l"
number_variable = 1
symbol_variable = "$"


print(type(chart_variable))
print(type(number_variable))
print(type(symbol_variable))


def encryption( user_input):
    switcher={
                0: int,
                1: str,
                2: "symbol"
            }
    for chart in user_input:
        #Here we need to add the algorithm
        # Case if it is a letter ✅
        # Case if it is a number ✅
        # Case if it is a symbol ✅       

        if type(chart)==str:
            print(f'This is the chart: {chart}')

encryption(param)
