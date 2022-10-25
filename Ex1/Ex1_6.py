roman_numerals = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")

number = int(input("please enter the number"))
if number:
    print(roman_numerals[number-1])
else:
    print("error")
#int -> str
#help:enter a number in the range of 1 through 10 then The program display the Roman numeral version of that number
