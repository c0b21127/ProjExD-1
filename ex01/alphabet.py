import random
import time

alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
full_alp = 26 # 全アルファベット数
tai_alp = 10 # 対象文字数
kes_alp = 2 # 欠損文字数
try_alp = 2 # チャレンジできる回数

# 全アルファベットから，対象文字をランダムに10文字選ぶ
r = random.sample(alp, tai_alp)
print('対象文字:')
print(r)

ra = random.sample(r, kes_alp)
print('欠損文字:')
print(ra)


ans1 = input('欠損文字の数はいくつ？')
if int(ans1)== kes_alp:
    print('正解です！欠損文字を答えてください。 ')
    while True:
        ans2 = input('1つ目の文字は？')
        if ans2 != ra:
            print('不正解です。もう一度チャレンジしてください。')
        
    print('正解です!!!')
else:
    print('不正解です。また、チャレンジしてください。')



