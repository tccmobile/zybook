__author__ = 'drwillsmith'

def print_face(eye, face_char):

   print('  ', eye, ' ', eye)  # Print eyes
   print('    ', face_char)    # Print nose
   print('  ', face_char*5)    # Print mouth
   return

print_face('o', 'x')


cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * inches_per_foot + inches
    cm = total_inches * cm_per_inch
    return cm

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))



def add(x, y):
    return x + y

print('add(5, 7) is', add(5, 7))
print("add('Tora' + 'Bora') is", add('Tora', 'Bora'))




def ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', ebay_fee(selling_price))



def modify(my_list):
    my_list[1] = 99

my_list = [10, 20, 30]
modify(my_list) # modify(my_list[:])

print(my_list)



def sandwich(bread, meat, *args):
    print('%s on %s with' % (meat, bread), end=' ')
    for extra in args:
        print(extra, end=' ')

sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')

student_scores = [75, 84, 66, 99, 51, 65]

def get_grade_stats(scores):
    # Calculate the arithmetic mean
    mean = sum(student_scores)/len(scores)

    # Calculate the standard deviation
    tmp = 0
    for i in range(len(scores)):
        tmp += (scores[i] - mean )**2
    std_dev = (tmp/len(scores))**0.5

    # Package and return average, standard deviation in a tuple
    return mean, std_dev

# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print('Average score:', average)
print('Standard deviation:', standard_deviation)
