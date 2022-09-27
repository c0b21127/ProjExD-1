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


def kaito(a):
    ans1 = input('欠損文字の数は？')
    if ans1 == kes_alp:
        print('正解です。欠損文字を答えてください。 ')
        while True:
            ans2 = input('1つ目の文字は？')
            if ans2 != a:
                print('不正解です。もう一度チャレンジしてください。')
        
        print('正解!!!')
    else:
        print('不正解です。また、チャレンジしてください。')


if __name__ == "_main_":
    alp = ['A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
