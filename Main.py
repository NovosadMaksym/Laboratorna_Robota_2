users = {
    "Yevhen_Melnyk": {
        "password": "Melnyk2009",
        "marks": (10, 11, 8, 7, 8, 6, 2, 4, 3, 4),
    },
    "Anastasiia_Shevchenko": {
        "password": "Shevchenko2009",
        "marks": (8, 10, 5, 11, 7, 3, 8, 9, 10, 4),
    },
    "Oleksandr_Kovalenko": {
        "password": "Kovalenko2010",
        "marks": (11, 8, 10, 6, 5, 9, 4 , 4, 3, 11),
    },
    "Vladyslav_Bondarenko": {
        "password": "Bondarenko2009",
        "marks": (10, 9, 4, 3, 8, 8, 4, 7, 2, 8),
    },
}

login = str(input("Введіть логін: "))
if login in users:
    for user in users:
        if user == login:
            password = str(input("Введіть пароль: "))
            if password == users[user]["password"]:
                goodMarks = 0
                for mark in users[user]["marks"]:
                    if mark >= 5:
                        goodMarks += 1
                print("Кількість задовільних оцінок: ", str(goodMarks))
                badMarks = 0
                for mark in users[user]["marks"]:
                    if mark < 5:
                        badMarks += 1
                print("Кількість незадовільних оцінок: ", str(badMarks))
            else:
                print("Невірний пароль")
else:
    print("Невірний логін")
