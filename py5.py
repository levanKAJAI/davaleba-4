# 5 ზედმეტსახელების გენერატორი
# მომხმარებელს შემოაქვს მხოლოდ ერთი სიტყვა(სხვა შემთხვევები დაბლოკე) და შენ სთავაზობ 5 ზედმეტსახელს ამ სიტყვასთან კავშირში.

import random


def get_one_word():
    while True:
        w = input("შეიყვანე ერთი სიტყვა (მხოლოდ ასოები, გამოტოვების გარეშე): ").strip()
        if w and w.isalpha() and " " not in w:
            return w
        print("უნდა იყოს ზუსტად ერთი სიტყვა და მხოლოდ ასოები (ქართ. ან ლათ.). სცადე თავიდან.")


def gen_nicks(base):
    base_cap = base.capitalize()
    prefixes = ["Mr", "Ms", "Pro", "The", "Ultra", "Neo", "Mega", "Mini", "Super", "Hyper"]
    suffixes = ["X", "Pro", "Master", "King", "Queen", "99", "2000", "Boss", "Guru"]

    ideas = set()
    # სხვადასხვა შაბლონი, რომ ბაზის სიტყვასთან იყოს კავშირში
    while len(ideas) < 5:
        mode = random.choice([1, 2, 3, 4, 5, 6])
        if mode == 1:
            ideas.add(f"{random.choice(prefixes)}{base_cap}")
        elif mode == 2:
            ideas.add(f"{base_cap}{random.choice(suffixes)}")
        elif mode == 3:
            ideas.add(f"{base}{random.randint(10, 99)}")
        elif mode == 4:
            ideas.add(f"x_{base}_x")
        elif mode == 5:
            ideas.add(f"{base_cap}_{random.choice(['dev', 'pro', 'max', 'plus', 'zone'])}")
        else:
            ideas.add(f"{random.choice(['i', 'e'])}{base_cap}")

    return list(ideas)


def main():
    print("ზედმეტსახელების გენერატორი (5 შეთავაზება)")
    word = get_one_word()
    for i, nick in enumerate(gen_nicks(word), 1):
        print(f"{i}. {nick}")


# დაწყება
main()
