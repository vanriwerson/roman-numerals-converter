def int_to_roman_numeral(int_to_convert):
    if not isinstance(int_to_convert, int):
        return "O número que será convertido precisa ser um inteiro."
    
    if int_to_convert > 3999:
        return "O número que será convertido não pode ser maior do que 3999."

    roman_algarisms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    correspondent_integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    converted = ""
    index = 0

    while int_to_convert > 0:
        if int_to_convert >= correspondent_integers[index]:
            converted += roman_algarisms[index]
            int_to_convert -= correspondent_integers[index]
        else:
            index += 1

    return converted