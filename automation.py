import re
from typing import final


with open("potential-contacts.txt") as f:
    text_from_file = f.read()

def add_dash(numbers):
    """
    Takes in a list of ten numbers and return a list with xxx-xxx-xxxx dash format
    """
    final_num = []
    for num in numbers:
        final_num.append(num[:3] + '-' + num[3:6] + '-' + num[6:])
    return final_num    

def strip_numbers(numbers): 
    """
    Takes in a list and strips all characters but numbers 1-9
    """
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
    
    with open('phone_numbers.txt', 'w') as file:
        for number in final_list:
            file.write(number)
            file.write('\n')

def get_emails(text_from_file):
    
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

    emails = re.findall(pattern, text_from_file)
    
    with open('existing-contacts.txt', 'w') as file:
        for number in emails:
            file.write(number)
            file.write('\n')
    
get_emails(text_from_file)
get_phone_numbers(text_from_file)



