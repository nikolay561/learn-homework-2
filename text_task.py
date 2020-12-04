with open('referat.txt', 'r', encoding='utf-8') as text:
	print(f'{len(text.read())} - символов в тексте.\n')


with open('referat.txt', 'r', encoding='utf-8') as text:
	result = str(text.readlines())
	print(f'{len(set((result.split())))} - слово в текте.\n')


with open('referat.txt', 'r', encoding='utf-8') as text:
	for i in text:
		i = i.replace('.', '!')
		print(i)


with open('referat2.txt', 'w', encoding='utf-8') as text:
	text.write(i) # почему-то сохраняет только последний абзац