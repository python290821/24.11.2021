
# enumerate
_tup1 = ('apple', 'banana', 'cherry')
y = enumerate(_tup1)
print(list(y))

grocery = [('bread', 5.5), ('milk', 7.2), ('butter', 13.90)]
for index, item in enumerate(grocery):
    if item[1] == 13.90:
        print(f'13.9 index is {index} in the list')
    print(item)
for item in enumerate('hello'):
    print(item)
for count, item in enumerate(grocery, 10): # starts at 10
    print(count, item)

# zip
a = ("john", "charles", "mike")
b = ("jenny", "monika", "sandra", "vikky")
#  iterator(20..100) index:0
# [20, 21 .. 100] index: 80
# []
zip_iterator_for_names = zip (a, b)
print(tuple(x))
print(list(zip(a, b)))