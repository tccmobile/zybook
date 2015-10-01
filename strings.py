__author__ = 'drwillsmith'

url = 'http://en.wikipedia.org/wiki/Turing'
domain = url[7:23]  # Read 'en.wikipedia.org' from url
print(domain)


numbers = '0123456789'

print('All numbers: %s' % numbers[::])
print('Every other number: %s' % numbers[::2])
print('Every third number between 1 and 8: %s' % numbers[1:9:3])



student_id = int(input('Enter student ID: '))

print('The user entered %d' % student_id)
print('Full 8-character student ID: %08d' % student_id)

user_input = input("Enter sentence:\n")

translation = user_input[:]  # Make a copy of the string

# Replace English with Spanish.
translation = translation.replace('one', 'uno')
translation  = translation.replace('two', 'dos')
translation = translation.replace('three', 'tres')
translation = translation.replace('four', 'quatro')
translation = translation.replace('five', 'cinco')
translation = translation.replace('six', 'seis')
translation  = translation.replace('seven', 'siete')
translation  = translation.replace('eight', 'ocho')
translation = translation.replace('nine', 'nueve')

print('Translation:', translation)

url = input('Enter URL:\n')

tokens = url.split('/')  # Uses '/' separator
print(tokens)

phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''.join(phrases)
print(sentence)