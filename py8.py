""""#8 პირამიდა მომხმარებელი შეჰყავს რიცხვების სია (მაგ. 3,5,7,2).
ამოცანა:
შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთაა წინა ორი რიცხვის ჯამი.
3 5 7 2
8 12 9
20 21
41
"""


def pyramid(numbers):
    pyramid_nums = [numbers]

    while len(pyramid_nums[-1]) > 1:
        prev_row = pyramid_nums[-1]
        new_row = []
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        pyramid_nums.append(new_row)

    # დაბეჭდვა
    for row in pyramid_nums:
        print(" ".join(map(str, row)))


def get_numbers():
    while True:
        s = input("შეიყვანე რიცხვები გამოტოვებით (დაშორებით): ").strip()
        parts = s.split()

        # ყველა ელემენტი უნდა იყოს რიცხვი (მინუსიც დაიშვება)
        if parts and all(x.lstrip("-").isdigit() for x in parts):
            return [int(x) for x in parts]
        else:
            print("მხოლოდ რიცხვები შეიყვანე და გამოტოვებით (დაშორებით) გამოყავით.")


# დაწყება
print("რიცხვების პირამინდა")
nums = get_numbers()
pyramid(nums)
