from datetime import datetime
import random


def random_string(length: int = 5):
    sample_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(sample_characters) for x in range(length))


def random_number(length: int = 3):
    sample_numbers = "0123456789"
    return ''.join(random.choice(sample_numbers) for x in range(length))


def random_email():
    return random_string(5) + "." + random_string(5) + random_number(3) + "@gmail.com"


def get_date_offset_years(offset_years: int = -20, date_format="%d-%m-%Y"):
    date = (datetime.today().replace(year=datetime.today().year + offset_years)).strftime(date_format)
    return date


dob = str(get_date_offset_years(-27))
print(dob)
print(dob[0:2])
print(dob[3:5])
print(dob[6:10])
