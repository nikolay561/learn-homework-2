# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
n = 0
for i in word:
    if i.lower() == 'а':
        n += 1
print(f'В вашем слове - {n} букв а.')


# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = ['а', 'е', 'ё', 'у', 'ы', 'о', 'э', 'я', 'и', 'ю']
word = word.lower()
n = 0
for i in word:
    for x in letters:
        if i == x:
            n += 1
print(f'Гласных букв {n}') 


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
n = 0
for i in range(len(sentence)):
    n += 1
print(f'В предложении {n} слов.')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for i in sentence:
    print(i[0])
    



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence = sentence.split()
for i in sentence:
    print(len(i) / 2)

