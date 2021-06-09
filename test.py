import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
#创建csv文件
f = open('words.csv','wt',newline='')
writer = csv.writer(f)
#写入表头
writer.writerow(('words','chs'))
def get_words(url):
    html = requests.get(url,headers=headers)
    html.raise_for_status()
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text,'lxml')
    words = soup.select('body > div.wap12.clearfix.mtt > div.leftWidth.borT > div.artCon > div.artTxt > table:nth-child(3) > tbody > tr > td:nth-child(1)')
    chs = soup.select('body > div.wap12.clearfix.mtt > div.leftWidth.borT > div.artCon > div.artTxt > table:nth-child(3) > tbody > tr > td:nth-child(2)')
    for word,ch in zip(words,chs):
        writer.writerow((word.get_text(),ch.get_text()))
url='https://www.kuakao.com/english/ch/152726.html'
get_words(url)
f.close()