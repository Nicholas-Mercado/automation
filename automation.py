import re
from typing import final


with open("potential-contacts.txt") as f:
    text_from_file = f.read()

def add_dash(numbers):
    final_num = []
    for num in numbers:
        final_num.append(num[:3] + '-' + num[3:6] + '-' + num[6:])
    return final_num    

def strip_numbers(numbers): 
    
    output = []
    
    for number in numbers:
        stripped_numbers = re.sub('[-.)(]','', number)
        output.append(stripped_numbers) 
    return output

def get_phone_numbers(text_from_file):
    
    pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    
    phone_numbers_10_digits = re.findall(pattern, text_from_file)
    
    output = strip_numbers(phone_numbers_10_digits)
        
    List_with_duplicates = add_dash(output)
    
    final_list = list(dict.fromkeys( List_with_duplicates))
    
    print(final_list)

def get_emails():
    pass

get_phone_numbers(text_from_file)



