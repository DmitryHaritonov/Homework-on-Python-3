letters = {
     "AEIOULNSTRАВЕИНОРСТ": 1,
     "DGДКЛМПУ": 2,
     "BCMPБГЁЬЯ": 3,
     "FHVWYЙЫ": 4,
     "KЖЗХЦЧ": 5,
     "JXШЭЮ": 8,
     "QZФЩЪ": 10
          }

user_word = input('Введите ваше слово: ')
eng_letter = []
rus_letter = []

while True:
    while len(user_word) == 0:
        user_word = input('Введите ваше слово (Поле не должно быт пустым): ')

    for i in user_word:
        if ord(i.upper()) in range(65, 91):
            eng_letter.append(ord(i.upper()))
        if ord(i.upper()) in range(1040, 1072):
            rus_letter.append(ord(i.upper()))
    if len(eng_letter) == len(user_word):
        print(f'Ваше слова на латинице, в нём {len(eng_letter)} букв(ы).')
        break
    elif len(rus_letter) == len(user_word):
        print(f'Ваше слова на кириллице, в нём {len(rus_letter)} букв(ы).')
        break
    else:
        user_word = input('Введите слово используя буквы одного из двух алфавитов (латиница, кириллица): ')

letters_sum = []

for i in user_word:
    for key in letters.keys():
         if i.upper() in key:
              letters_sum.append(letters[key])

print(f'Сумма букв вашего слова, согласно условию задачи: {sum(letters_sum)}')