import random
import string

def passwordGen( min_len, numbers, special) :
    letters = string.ascii_letters
    digits = string.digits
    special_chr = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special_chr

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_chr = random.choice(characters)
        pwd += new_chr

        if new_chr in digits:
            has_number = True
        elif new_chr in special_chr:
            has_special = True

        meets_criteria = True
        if numbers :
            meets_criteria = has_number
        if special :
            meets_criteria = meets_criteria and has_special

    return pwd
min_len= int(input("Enter the minimum length :"))
has_num = input("Do you want to have numbers(y/n)").lower() == "y"
has_sp = input("Do you want to have special characters(y/n)").lower() == "y"
pwd = passwordGen(min_len,has_num,has_sp)
print("The generated password is:",pwd)

