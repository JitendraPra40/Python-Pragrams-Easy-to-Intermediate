def roman_to_decimal():
    print("This program converts a roman numeral to a decimal number.")
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_num = input("Enter a roman numeral: ")
    roman_num = roman_num.upper()
    total = 0
    provious_value = 0
    for i in reversed(roman_num):
        value = roman[i]
        if value >= provious_value:
            total += value
        else:
            total -= value
        provious_value = value
    return total
print(roman_to_decimal())