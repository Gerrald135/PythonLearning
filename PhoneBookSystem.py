names = []
phones = []
number_of_contacts = int(input('How many contacts do you want to store? '))
for i in range(number_of_contacts):
    name = str(input('Enter name: '))
    num = str(input('Enter phone number: '))

    names.append(name)
    phones.append(num)

for n, p in zip(names, phones):
    print(f'{n} -> {p}')

name_to_search = str(input('Enter a name to search: '))

if name_to_search in names:
    index = names.index(name_to_search)
    print(f'{name_to_search} -> {phones[index]}')
else:
    print('Contact not found!')