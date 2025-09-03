# 6 სორტირება მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა) პროგრამა სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად, მხოლოდ უნიკალური მონაცემები დატოვოს. რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე დალაგებული სია.

import random


def get_numbers():
    while True:
        s = input("შეიყვანე რიცხვები გამოტოვებით (დაშორებით): ").strip()
        parts = s.split()
        if all(p.isdigit() or (p.startswith('-') and p[1:].isdigit()) for p in parts):
            if parts:
                return [int(x) for x in parts]
            else:
                print("მინიმუმ ერთი რიცხვი მაინც უნდა შეიყვანო")
        else:
            print("მხოლოდ რიცხვები შეიყვანე და გამოტოვებით (დაშორებით) გამოყავი.")


def choose_sorting(numbers):
    while True:
        print("\nროგორ გინდა დალაგება?")
        print("1 - ზრდადობით")
        print("2 - კლებადობით")
        print("3 - შემთხვევით (random)")
        print("4 - მხოლოდ უნიკალური მონაცემები")

        choice = input("აირჩიე (1/2/3/4): ").strip()

        if choice == "1":
            return sorted(numbers)
        elif choice == "2":
            return sorted(numbers, reverse=True)
        elif choice == "3":
            result = numbers[:]
            random.shuffle(result)
            return result
        elif choice == "4":
            return list(set(numbers))
        else:
            print("არასწორი არჩევანი! სცადე თავიდან.\n")


def main():
    print("მონაცემების დალაგება")
    numbers = get_numbers()
    result = choose_sorting(numbers)
    print("\nშედეგი:", result)


# დაწყება
main()
