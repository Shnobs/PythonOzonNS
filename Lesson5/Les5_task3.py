kotoschetchik = 0
with open('lesson05_cats_of_ulthar.txt', 'r+') as book:
    for line in book:
        if line.count('кошка ') > 0:
            kotoschetchik += line.count('кошка ')
            print(line)
print(kotoschetchik)
