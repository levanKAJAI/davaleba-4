# 1 დაწერეთ პაროლის გენერატორი. დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,სტრიქონის ფორმატირება.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”


import random
import string

# დასაწყისი
print("password-ის გენერატორი")


# პაროლის სიგრძის განსაზღვრა
def get_length():
    while True:
        length = input("მიუთითეთ პაროლის სიგრძე: ")
        if length.isdigit():
            return int(length)
        else:
            print("შეიყვანე მხოლოდ რიცხვი!")


# კითხვების დასმა:
def get_choice(question):
    while True:
        answer = input(question + " (yes/no ან y/n): ").lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("შეიყვანე მხოლოდ yes/no ან y/n!")


def password_gene():
    # პაროლის სიგრძის წამოღება
    length = get_length()

    # კითხვები
    use_lower = get_choice("გამოვიყენოთ პატარა ლათინური ასოები?")
    use_upper = get_choice("გამოვიყენოთ დიდი ლათინური ასოები?")
    use_digits = get_choice("გამოვიყენოთ რიცხვები?")
    use_symbols = get_choice("გამოვიყენოთ სიმბოლოები?")

    # არჩეული სიმბოლოები
    chars = ""
    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    # სიმბოლოების შემოწმება
    if not chars:
        print("უნდა აირჩიო ერთი მაინც სიმბოლო (ასო(დიდი და პატარა)/რიცხვი/სიმბოლო).")
        return

    # პაროლის მიღება
    global password
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"\n შენი გენერირებული პაროლია: {password}")


# გაშვება
password_gene()

# პაროლის გადამოწმება
if get_choice("გინდა პაროლის გადამოწმება?"):
    check = input("შეიყვანე პაროლი: ")
    if check == password:
        print("პაროლი სწორია!")
    else:
        print("არასწორია!")
else:
    print("წარმატებებს გისურვებ!")
