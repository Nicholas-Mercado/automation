import re


with open("potential-contacts.txt") as f:
    text_from_file = f.read()

def add_dash(numbers):
    
    for num in numbers:
        final_num = num[:3] + '-' + num[3:6] + '-' + num[6:]
        print(final_num)    

def get_phone_numbers(text_from_file):
    
    pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    
    phone_numbers_10_digits = re.findall(pattern, text_from_file)
    output = []
    
    for number in phone_numbers_10_digits:
        number1 = re.sub('[-.)(]','', number)
        output.append(number1)
        
    add_dash(output)
    

def get_emails():
    pass

get_phone_numbers(text_from_file)



