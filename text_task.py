with open('referat.txt', 'r', encoding='utf-8') as reader:
	text = reader.read()
	symbols = len(text)
	print(f'{symbols} - символов в тексте.\n')
	line = text.replace('.', '!')
	print(line)
	print(f'{len((text.split()))} - слово в текте.\n')


with open('referat2.txt', 'w', encoding='utf-8') as text:
	text.write(line)


# with open('referat.txt', 'r', encoding='utf-8') as text:
# 	result = str(text.readlines())
# 	print(f'{len(set((result.split())))} - слово в текте.\n')
#
#
# with open('referat.txt', 'r', encoding='utf-8') as reader:
		# line = line.replace('\n','')
		# line = line.rstrip('\n')



