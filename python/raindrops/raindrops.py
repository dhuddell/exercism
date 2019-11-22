def convert(number):
# Have 3 strings, they either add the string or not, if none then give the number
# This could be shorter, but I feel like this is the purest approach?
    isPling = 'Pling' if number%3 == 0 else ''
    isPlang = 'Plang' if number%5 == 0 else ''
    isPlong = 'Plong' if number%7 == 0 else ''
    return f'{isPling}{isPlang}{isPlong}' or str(number)
