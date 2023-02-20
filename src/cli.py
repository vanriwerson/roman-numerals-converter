import click
from converter import int_to_roman_numeral, roman_numeral_to_int

@click.command()
def main():
    conversion_type = click.prompt('What type of conversion would you like to perform? (arabic = A/roman = R)', type=click.Choice(['arabic', 'roman']))

    if conversion_type == 'arabic':
        arabic_numeral = click.prompt('Enter the Arabic numeral', type=int)
        roman_numeral = int_to_roman_numeral(arabic_numeral)
        click.echo(f'{arabic_numeral} = {roman_numeral}')
    else:
        roman_numeral = click.prompt('Enter the Roman numeral', type=str)
        arabic_numeral = roman_numeral_to_int(roman_numeral)
        click.echo(f'{roman_numeral} = {arabic_numeral}')

if __name__ == '__main__':
    main()
