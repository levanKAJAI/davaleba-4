# 10 მომხმარებელს შეჰყავს წინადადება, ამოცანა: გამოიანგარიშე თითოეული სიტყვის სიგრძე და დააბრუნე dictionary მაგალითად: "Python is fun" → {"Python": 6, "is": 2, "fun": 3}

# ტექსტი
sentence = input("შეიყვანე წინადადება: ")

words = sentence.split()

# dict-ის შექმნა
lengths = {}
for word in words:
    lengths[word] = len(word)

print(lengths)
