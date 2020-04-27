"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

file = open('test_file', 'r')
lines = file.readlines()

result = []
for itm in lines:
    itm = itm.split()
    result.append(itm)

print('Quantity', len(result))

for itm in result:
    print('word count', len(itm))

file.close()

