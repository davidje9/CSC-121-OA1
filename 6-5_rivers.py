major_rivers = {'ganges': 'india', 'seine':'france','yangtze': 'china'}

for river, country in major_rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print('\nWhat major river runs through these countries?')

for country in sorted(major_rivers.values()):
    print(f'{country.title()}')
