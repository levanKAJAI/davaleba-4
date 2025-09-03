# 4 პალინდრომი
# ამოცანა: შეამოწმე, არის თუ არა შეყვანილი ტექსტი პალინდრომი (მხოლოდ ასოები/ციფრები). თუ არაა, შესთავაზე ყველაზე ახლო პალინდრომი ერთი სიმბოლოს ჩასმით/წაშლით.

def near_palindrome(s):
    s = "".join(ch for ch in s if ch.isalnum()).lower()

    if s == s[::-1]:
        return "პალინდრომია!", s

    n = len(s)

    # ერთი სიმბოლის წაშლა
    for i in range(n):
        temp = s[:i] + s[i + 1:]
        if temp == temp[::-1]:
            return f"პალინდრომი გახდება მაგალითად თუ წაშლით '{s[i]}' სიმბოლოს პოზიციიდან {i + 1}", temp

    # ერთი სიმბოლის დამატება
    for i in range(n + 1):
        for ch in "abcdefghijklmnopqrstuvwxyz0123456789":
            temp = s[:i] + ch + s[i:]
            if temp == temp[::-1]:
                return f"პალინდრომი გახდება თუ დაამატებთ '{ch}' სიმბოლოს პოზიციაზე {i + 1}", temp

    # სიმბოლის ჩანაცვლება
    for i in range(n - 1, -1, -1):
        for ch in "abcdefghijklmnopqrstuvwxyz0123456789":
            if ch != s[i]:
                temp = s[:i] + ch + s[i + 1:]
                if temp == temp[::-1]:
                    return f"პალინდრომი გახდება თუ შეცვლით '{s[i]}' სიმბოლოს პოზიციაზე {i + 1} '{ch}'-ზე", temp

    return "ერთ მოქმედებით (წაშლა/დამატება/ჩანაცვლება) პალინდრომის შექმნა შეუძლებელია.", None


# მხოლოდ ლათინური ასოები და ციფრები
def get_valid():
    while True:
        user_input = input("შეიყვანე ტექსტი/რიცხვი (a-z, A-Z, 0-9): ").strip()
        if all(ch.isalnum() and ch.isascii() for ch in user_input):
            return user_input
        else:
            print("არასწორია! მხოლოდ ლათინური ასოები და ციფრებია დაშვებული. სცადე თავიდან.")


# მთავარი ნაწილი
print("პალინდრომის შემოწმება\n(მხოლოდ ლათინური ანბანის ასოები და ციფრები გამოიყენება)")
user_input = get_valid()

filtered = "".join(ch for ch in user_input if ch.isalnum()).lower()

if filtered == filtered[::-1]:
    print(f"'{user_input}' არის პალინდრომი!")
else:
    message, result = near_palindrome(filtered)
    print(f"'{user_input}' არ არის პალინდრომი.")
    print(message)
    if result:
        print(f"მიღებული პალინდრომი: '{result}'")
