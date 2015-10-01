__author__ = 'drwillsmith'

nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(' %s %s ' % (user_value, user_value))  # Print eyes
    print('  %s  ' % nose)  # Print nose
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): ")
    user_value = user_input[0]

print('Goodbye.\n')



daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: $%f' % total)
print('Daily average revenue: $%f' % average)



'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years:\n'))

savings = initial_savings
for i in range(years):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)

print('\n')



"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('%s%s.com' % (letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)





empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('$%d buys %d empanadas and %d tacos without change.' %
        (meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')