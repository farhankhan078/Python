a = 'Give me your card number'
b = 'Give me your telegram'
c = 'please join'
d = 'Buy Now'
e = 'Subscribe Now To get a Ferrari'

i = input('Enter msg: ')
if(i in a or i in b or i in c or i in d or i in e):
    print('True Info.')
else:
    print('Scam')