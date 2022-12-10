#collections error in python 3.10; try python ver 3.9
import base64
from PIL import Image
from gensim.summarization.summarizer import summarize
import collections
from collections.abc import Mapping
import textwrap
import re

#기사 본문 준비
with open("article.txt", 'rb') as article:
    article: bytes = article.read()
article= article.decode('utf-8') # 기사 본문 디코딩

# 기사 이미지 processing
with open("img.jpeg", 'rb') as img :
    image = img.read()
path = "image_2.jpeg"
with open(path, 'wb') as f:
    decoded_data = base64.decodebytes(image)
    f.write(image)

#이미지 확인
#img = Image.open(path)
#print(img)

#문서 요약
article_summarized = summarize(article, ratio=0.4)
#정렬하기
text_align = textwrap.fill(article, width=40) #줄바꿈이 자동으로 됨.
words = re.findall(r'\w+', text_align)
#단어 세기

counter = collections.Counter(words)
#키워드
keywords = counter.most_common(3)
keys = ['#' + element[0] for element in keywords]
keys = ' '.join(keys)

#리포트 생성 html로
htmlfile = open("summary.html", "w")
htmlfile.write("<html>\n")
htmlfile.write ("<h1>"+ '카카오 먹통 방지법’ 여야 이견 없이 법사위 통과' + "</h2>\n")
htmlfile.write ("<img src='image_2.jpeg'/>\n")
htmlfile.write ("<h2>"+ article_summarized + "</h2>\n")
htmlfile.write ("<h2 style='background-color:powderblue;''>"+ keys + "</h2>\n")
htmlfile.write("</html>\n")
htmlfile.close()
