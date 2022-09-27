import random

alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
full_alp = 26
tai_alp = 10
kes_alp = 2
try_alp = 2


r = random.sample(alp, tai_alp)
print('対象文字:')
print(r)

ra = random.sample(r, kes_alp)
print('欠損文字:')
print(ra,end=" ")


ans1 = input('欠損文字の数は？')
if int(ans1)== kes_alp:
    print('正解です。欠損文字を答えてください。 ')
    while True:
        ans2 = input('1つ目の文字は？')
        if ans2 != ra:
            print('不正解です。もう一度チャレンジしてください。')
        
    print('正解!!!')
else:
    print('不正解です。また、チャレンジしてください。')



