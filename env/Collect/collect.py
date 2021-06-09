import requests
from bs4 import BeautifulSoup
import re
import csv

try:

    #创建txt文件写入
    file = open('collect.txt', 'w', encoding='utf-8')

    # 创建csv文件
    f = open('collect.csv', 'wt', newline='', encoding='utf-8')
    writer = csv.writer(f)

    # 写入表头
    writer.writerow(('单词', '释义'))

    # 循环爬取考研英语必备大纲单词，共65页
    for page in range(0,65,1):

        file.write("第{}章".format(page + 1))
        file.write('\n')

        base_url = 'http://www.kuakao.com/english/ch/39' + str(183 + page) + '.html'

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        }
        r = requests.get(base_url, headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.content, 'lxml')
        # 利用stripped_strings可以将多余的有含空格的冗余列表排除
        for string in soup.stripped_strings:
            #正则表达式筛选以编号开头 英文为中 词性 中文释义结尾的 （这个正则写了我一个小时我淦）
            text = re.findall(r'\d{1,2} [a-zA-Z]* \w+.[\u4e00-\u9fa5]+',repr(string))
            for t in text:

                #写入txt文本
                file.write(t)
                file.write('\n')

                #写入CSV格式
                words = re.findall(r'[a-zA-Z]+ ',t)
                paraphrase = re.findall(r'[\u4e00-\u9fa5]+$',t)
                for word,par in zip(words,paraphrase):
                    writer.writerow((word,par))

    file.close()
    f.close()
except Exception as e:
    print(e)