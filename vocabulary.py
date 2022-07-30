import PyPDF2
import os
import requests
from bs4 import BeautifulSoup

print("第何回ですか？",end="")
num = input()
print("実行中")

with open("IE2 vocabulary Week "+num+".pdf", "rb") as f:#ここでPDFファイルの読み込み
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    words=page.extractText().split()





for l in words:#一個ずつ入れる


    url1 = 'https://ejje.weblio.jp/content/'

    url = url1+str(l)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems1 = soup.select('#summary > div.summaryM.descriptionWrp > p > span.content-explanation.ej')
    #単語の意味を取り出す↑
    filepath = 'vocabulary'+num+'.txt'
    exists = os.path.exists(filepath)#ファイルがあるかの確認

    if str(exists) =="True":
        try:
            with open("vocabulary"+num+".txt", mode='a') as f:
                f.write(l)#英単語を書き込む
                f.write(elems1[0].contents[0])#意味を書き込む
                f.write("\n")
        except IndexError:
            continue
    else:#存在しなければファイルを作成
        try:
            elems1[0].contents[0]
            with open("vocabulary"+num+".txt", mode='a') as f:
                f.write(l)
                f.write(elems1[0].contents[0])
                f.write("\n")
        except IndexError:
            continue

print("実行完了")