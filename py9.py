# 9 მომხმარებელი შეჰყავს ნებისმიერი ტექსტი, მოძებნე, რომელი სიტყვა მეორდება ტექსტში ყველაზე მეტჯერ. მაგ: "Python is great and python is easy" → ყველაზე ხშირია "python". თუ ორი ან მეტი სიტყვაა ტოლი, დააბრუნე ყველა.

def most_freq_words(text):
    text = text.lower()
    words = text.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    max_count = max(counts.values())
    most_frequent = [word for word, count in counts.items() if count == max_count]

    return most_frequent


# დაწყება
print("ყველაზე მეტჯერ განმეორებული სიტყვის (სიტყვების) პოვნა")
user_input = input("შეიყვანეთ ტექსტი: ")
result = most_freq_words(user_input)

print("ყველაზე ხშირად განმეორებადი სიტყვაა/სიტყვებია:", result)
