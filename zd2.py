from numpy import *
import pylab

t = str('Нет такого понятия, как «судьба». Это всего лишь сочетание нескольких обстоятельств')
def count_letters():
    abetka = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
              'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
              'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
              'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
              ]
    for i in range(0, len(abetka)):
        x = [abetka[i]]
        y = [t.count(abetka[i])]
        pylab.bar(x, y)
    pylab.show()
count_letters()
