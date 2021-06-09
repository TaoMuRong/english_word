#导入模块requests,re
import requests
import re

#定义请求url
#爬取网页URL: https://wenku.baidu.com/view/cc07fec19b8fcc22bcd126fff705cc1755275f01.html
#考研英语词汇大全百度文库
from pip._vendor.html5lib.treebuilders.etree_lxml import Document

urlList = {

    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=204844-&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.jZJvHbDmpra4M5bIfkOqwz1F4j2ycwky18p1KDsy6Gg%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=180815-204843&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.YZ1ivZEn45CHbssI8KhCIHc2ZvtYcmeeExgKwzNfqh4%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=151125-180814&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.j2bnjiXFaejozDjStH8nr7VqSZYq6wO1BCWhATy48WU%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=122739-151124&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Q%2FdzQzDnkcJ38GtLK9t8rKzNbL4Dw9Jx7pkqJVzbEr0%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=102147-122738&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.xdsMUXTYX1PSHyULZb2slW9H7EFocSQHurMaxFoAxlY%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=74489-102146&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.rQvi75bXZka5O6zZsuR1zj9fKkfZrVqZmb0AW93vYqY%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=55894-74488&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.W67%2F1pPRB6ZU94w2Rtvv2xuaFsmR6O6baPFNJvpfhT8%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=37138-55893&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.JDmLySUM%2FwKx0bYOY366SfllQ5a6vr0Mcy%2BtOHytZH8%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=17434-37137&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.iVoCx72Z%2FNs8wdBZ7zE2BI4mhp5HXq68p%2Fv6bo5yAEY%3D.1623235227",
    "https://wkbjcloudbos.bdimg.com/v1/docconvert3059/wk/b0b8ad403f5e0d8bff2ccaa8f265ecf0/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sat%2C%2024%20Jul%202021%2017%3A40%3A27%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-06-09T09%3A40%3A27Z%2F3600%2Fhost%2F2ef1e71ab1c07ae2b834ecbcc015b9f9d570a27c11f6a467fb0cf542de1addb5&x-bce-range=0-17433&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYyMzIzNTIyNywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.6jib1xLmlGFQZsj8AhNflIsem%2FCQMG7mJkurx1LyIQA%3D.1623235227"


}

#定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
    "Host": "wkbjcloudbos.bdimg.com"
}

#请求内容
for url in urlList:
    content = requests.get(url=url,headers=headers)
    if 200 <= content.status_code < 300:  # 如果状态码是200，则表示爬取成功
        print("成功")
    else:print(url + "请求失败:"+ content.reason )
    #设置编码方式
    content.encoding = "unicode_escape"
    #正则提取所需要的内容
    content_list = re.findall('"c":"(.*?)","p"',content.text)
    #保存到txt文件内
    file = open('analyze.txt', 'w', encoding='utf-8')
    for str in content_list:
        file.write(str)
        file.write('\n')
    file.close()