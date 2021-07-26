import csv
import random

def word_test(c):

    with open('BSL.csv', 'r', encoding='utf-8_sig') as f:
        row = csv.reader(f)
        words = [i for i in row]
    t = 0
    f = 0
    for _ in range(int(c)):
        oo = random.choice(words)
        print(oo[1], oo[0])
        ans = input('答え:')
        if ans == 'fin':
            break
        elif ans == oo[0]:
            print('true')
            t += 1
        else:
            print('fault')
            f += 1
    p = t/(t+f)*100
    print('per {:.1f}%'.format(p))


cc = input('number of tests->')
word_test(cc)
