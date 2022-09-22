import re


# hello
def find_letter_a(string):
    return re.search('a', string).start()
    

print(find_letter_a('uganda'))


def find_capitals(string):
    return re.match(r'([A-Z])\w+', string)


print(find_capitals('string'))

def check_uganda_phone_nums(phone):
    return re.match(r'^(077|075|070|074|076|078|072|071|079)\d{7}$', phone)

phones = ['0752541359',
'0712345678',
'0781234567',
'0701234567',
'0812345678',]


for phone in phones:
    if check_uganda_phone_nums(phone):
        print('{} is a ugandan phone number'.format(phone))
    else:
        print('{} is not a ugandan phone number'.format(phone))


def check_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
    