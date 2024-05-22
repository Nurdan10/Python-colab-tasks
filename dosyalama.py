# -*- coding: utf-8 -*-
"""dosyalama.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17bXwffRYEwU7Dvxv7ago_qSBV4Uh-7Kz
"""

This is the neSIIR = open("SIIR.txt", "r", encoding="utf-8")
print("Dosya adi:", SIIR.name)
print("Dosya modu:", SIIR.mode)
print("Dosya kaptildi mi?", SIIR.closed)
print("Dosya encoding", SIIR.encoding)
SIIR.close()

FILE = open("/rumi.txt")
type(FILE)

FILE = open("/test_ad.txt", "w")
print("Nurdan\n" * 5, file=FILE)

with open("test_ad.txt", "r", encoding="utf-8") as f:
  for line in f:
    print(line, end='')





with open("test_ad.txt", "r+", encoding="utf-8") as f:
  for line in f:
    print('dede\n', end='')

my_file = open("/content/fishes.txt", mode='r')
print(my_file.read())
my_file.close()

my_file = open("/content/fishes.txt", mode='r')
print(my_file.read(33))
my_file.close()

my_file = open("/content/fishes.txt", mode='r')
print(my_file.read(33))
print(my_file.tell())
my_file.close()

my_file = open("/content/rumi.txt", mode='r')
print(my_file.read())

my_file = open("/content/rumi.txt", mode='r')
print(my_file.read(36))

my_file = open("/content/rumi.txt", mode='r')
print(my_file.read(36))
print(my_file.read(13))
print(my_file.tell())
my_file.seek(15)
print(my_file.read(20))
my_file.close()

sea = open("fishes.txt", 'r')
print(sea.readline())
print(sea.readline())
print(sea.readline())
sea.close()

rumi = open("rumi.txt", 'r')
print(rumi.readline())
print(rumi.readline())
print(rumi.readline())
print(rumi.readlines())
rumi.close()

rumi = open("rumi.txt", 'r')
print(rumi.readlines())
rumi.close()

rumi = open("rumi.txt", 'r')
for line in rumi:
  print(line, end='')
 rumi.close()

rumi = open("rumi.txt", 'r')
for line in rumi.readlines():
  print(line, end='')
rumi.close()

rumi = open("rumi.txt", 'r')
for line in rumi.readlines():
  print(line, end='')
  line.append("++")
rumi.close()

with open("rumi.txt", 'r', encoding="utf-8") as f:

with open("fishes.txt", 'r', encoding="utf-8") as fr:
  print(fr.read())
fr.closed()

colors = ['red..', 'green..', 'yellow..', 'white..', 'black..']
with open("colors.txt", 'w', encoding='utf-8') as file:
    file.write('\n')

colors = ['red..', 'green..', 'yellow..', 'white..', 'black..']

with open("new_file.txt", 'w', encoding='utf-8') as file:
    file.write('red\ngreen\nyellow\nwhite\nblack\n')

colors = ['red', 'green', 'yellow', 'white', 'black']

with open("new_file.txt", 'w', encoding="utf-8") as file:
    for i in colors:
        file.write(i + '\n')  # we create "new_file.txt" for you
with open("new_file.txt", 'a', encoding="utf-8") as file:
    file.write('blue\n')  # add "blue" to the end of the text

with open('/content/fruits.csv', mode='w') as file:
  print('no, fruit, amount', file=file)
  print('1, banana, 4', file=file)
  print('2, orange, 5', file=file)
  print('3, apple, 2', file=file)
  print('4, strawberry, 6', file=file)
  print('5, cherry, 3', file=file)

import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows:
        print(row)

import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter=',')  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows:
        print(row)               # üstteki ile ayni ciktiyi aliriz

import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter=':')  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows:         # virgül yerine : gibi baska bir karakter kullanildiginda satiri tek stringe dönüstürür
        print(row)

list = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']
with open('fruits.txt', 'w') as file:
  for i in list:
    file.write(i+ '\n')
with open('fruits.txt', 'r') as file:
  print(file.read())

flowers = ['Jasmine', 'Rose', 'Lily', 'Daisy', 'Tulip']
with open('flowers.txt', 'w') as file:
  for i in flowers:
    print(i, '\n\n')

flowers = ['Jasmine', 'Rose', 'Lily', 'Daisy', 'Tulip']
with open('flowers.txt', 'w') as file:
  for i in flowers:
    file.writelines(i + '\n')
with open('flowers.txt', 'r') as file:
  print(file.read())

with open('/content/file/project/flowers', 'a') as file:
  file.write('Orchid')
with open('flowers.txt', 'r') as file:
  print(file.read())

my_list = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']
with open('fruits.txt', 'w') as file:
    file.writelines(my_list)
with open('fruits.txt', 'r') as file:
  print(file.read())
with open('fruits.txt', 'r') as file:
  print(file.readlines())

my_list = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']
with open('fruits.txt', 'a') as file:
    file.write('Melon')
with open('fruits.txt', 'r') as file:
  print(file.read())
with open('fruits.txt', 'r') as file:
  print(file.readlines())

my_list = ['Jasmine\n', 'Rose\n', 'Lily\n', 'Daisy\n', 'Tulip\n']
with open('flowers.txt', 'w') as file:
    file.writelines(my_list)
with open('flowers.txt', 'r') as file:
  print(file.read())
with open('flowers.txt', 'r') as file:
  print(file.readlines())

!pwd

my_file = open('istiklal_marsi', 'r')
my_file2 = open('istiklal2.txt', )

with open('istiklal_marsi', 'r') as my_file, open('istiklal2.txt', 'w') as my_file2:
  for i in my_file.readlines():
    my_file2

with open('fruit.csv', 'r') as file:
  print(file.read())

import csv
with open('fruit.csv', 'r') as file:
  for i in csv.reader(file, delimiter=',')
  print(*i)

with open('/content/people.csv', mode='w') as file:
  print('row_num, first_name, last_name, ages', file=file)
  print('1, Mahmut, Coskun, 71', file=file)
  print('2, Nuray, Coskun, 70', file=file)
  print('3, Hakan, Coskun, 49', file=file)
  print('4, Gülcin, Demir, 45', file=file)
  print('5, Eymen, Demir, 20', file=file)
with open('people.csv', mode='r') as file:
  print(file.read())

import csv
with open('people.csv', 'r') as file:
  csv_rows = csv.reader(file)
  for row in csv_rows:
    print(row)

import csv
with open('people.csv', 'r') as file:
  csv_rows = csv.reader(file)
  for row in csv_rows:
    print(*row)  # önüne asterisk koyunca liste formundan kurtuluyoruz

import csv
with open('people.csv', 'r') as file:
  csv_rows = csv.reader(file, delimiter=':')
  for row in csv_rows:
    print(row)

person_list = """row_num  first_name  last_name  ages
1  Mahmut  Coskun  71
2  Nuray  Coskun  70
3  Hakan  Coskun  49
4  Gülcin  Demir  45
5  Eymen  Demir  20
"""
with open('person.csv', 'w') as file:
  file.writelines(person_list)
with open('person.csv', 'r') as file:
    print(file.read())

from PIL import Image
Image.open('/content/Data Science.jpg')