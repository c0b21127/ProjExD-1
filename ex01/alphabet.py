import random

full_alp = 26
tai_alp = 10
kes_alp = 2
try_alp = 2

def shutudai():
    r = random.sample(alp, tai_alp)
    print('対象文字:')
    print(r)

    ra = random.samle(r, kes_alp)
    print('欠損文字:')
    print(ra)


if __name__ == "_main_":
    alp = ['A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
