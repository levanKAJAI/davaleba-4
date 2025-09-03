# 2 პაროლის შეფასება ამოცანა: მომხმარებლის შეყვანილი პაროლი შეაფასე 0–10 შკალით: სიგრძე, ციფრები, სიმბოლოები, დიდი/პატარა ასოები, განმეორებადი სიმბოლოების არსებობა. მოთხოვნები: გამოიტანე “weak/medium/strong”.

import string


def password_Check(password):
    score = 0

    # სიგრძე
    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1
    else:
        score += 0

    # ციფრი
    if any(ch.isdigit() for ch in password):
        score += 2

    # პატარა ასო
    if any(ch.islower() for ch in password):
        score += 2

    # დიდი ასო
    if any(ch.isupper() for ch in password):
        score += 2

    # სიმბოლო
    if any(ch in string.punctuation for ch in password):
        score += 2

    # განმეორებადი სიმბოლოები (მინუს ქულა)
    if len(password) != len(set(password)):
        score -= 1

    # შეფასება
    if score <= 3:
        level = "weak"
    elif score <= 6:
        level = "medium"
    else:
        level = "strong"

    return score, level


# დაწყება
user_password = input("password-ის შემოწმება\n(გამოიყენეთ მხოლოდ ლათინური ასოები)\nშეიყვანეთ თქვენი პაროლი: ")

score, level = password_Check(user_password)

print(f"პაროლი შეფასდა როგორც: {level} ~ ქულა: {score}/10")
