# 7 ტექსტის ფილტრი მომხმარებელი შეჰყავს ტექსტი. ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და სივრცეები.


def text_filter():
    text = input("შეიყვანე ტექსტი: ")
    result = ""

    for ch in text:
        if ch.isalpha() or ch.isspace():
            result += ch

    print("\nგაფილტრული ტექსტი:")
    print(result)


# დაწყება
print("ტექსტის ფილტრი")
text_filter()
