__author__ = 'drwillsmith'


price_younger = 4800  # Age less than 25
price_older = 2200  # Age 25 and up

age = int(input('Enter age:\n'))

if age < 25:
    price = price_younger
    print('EXECUTED FIRST BRANCH')
else:
    price = price_older
    print('EXECUTED SECOND BRANCH')

print('Annual price: $%d' % price)


# (2010 carsdirect.com)
age_16_to_24 = 4800  # Age less than 25
age_25_to_39 = 2350  # Ages 25 to 39
age_40_up = 2100     # Ages 40 and up

age = int(input('Enter your age: '))
price = 0

if age <= 15:
    print('Too young for car insurance.')
    price = 0
elif age <= 24:
    price = age_16_to_24
elif age <= 39:
    price = age_25_to_39
else:
    price = age_40_up

print('Annual price: $%d' % price)



barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')