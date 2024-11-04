html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>
            <p id="second">class1's second paragraph</p>

            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example	page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.string) # <title>태그의 텍스트만 리턴
print(soup.title.get_text())
print(soup.title.parent)
print(soup.body)
print(soup.h1)
print(soup.h1.string)
print(soup.a) # <a> 태그 전체 추출:<a class="external_link" href="www.google.com">google</a>
print(soup.a.string)					# <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href'])					# <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href'))               # soup.a['href']와 동일 기능
print(soup.find('div'))
print(soup.find('div', {'id': 'text_id2'}))
div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)
print(div_text.string)
href_link =	soup.find('a', {'class': 'internal_link'})
href_link =	soup.find('a', class_='internal_link')
print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)
print('href_link.attrs: ', href_link.attrs) # <a>태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class']) # class 속성의 value 출력
print('values():', href_link.attrs.values()) # 모든 속성들의 값 출력
values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경
print(f'values[0]: {values[0]}, values[1]: {values[1]}')
href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})
print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)
span_tag = soup.find('span')
print('span	tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)
print('class 속성값: ', href_link['class'])
from bs4 import BeautifulSoup
tr = '''
<table>
    <tr class="passed a b c" id="row1 example"><td>t1</td></tr>
    <tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'): # find_all('tag'): 해당 tag를 모두 찾아서 리스트로 리턴
    print(row.attrs)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
# 모든 div 태그를 검색 (리스트 형태로 반환)
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))
for div in div_tags:
    print('-----------------------------------------------')
    print(div)
links = soup.find_all('a')
for alink in links:
    print(alink)
    print(f"url: {alink['href']}, text: {alink.string}")
    print()
links = soup.find_all('a')
for alink in links:
    print(alink)
    print(f"url: {alink['href']}, text: {alink.string}")
    print()
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)
p_tags = soup.find_all('p', {'id':['first', 'third']})
for p in p_tags:
    print(p)
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())
h1 = soup.select_one('h1') # 첫 번째 <h1>태그 선택
print(h1)
footer = soup.select_one('h1#footer')
print(footer)
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())
h1 = soup.select_one('h1') # 첫 번째 <h1>태그 선택
print(h1)
footer = soup.select_one('h1#footer')
print(footer)
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])
link1 = soup.select_one('div#link > a.external_link')
print(link1)
link_find = soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class': 'external_link'})
print('find	external_link: ', external_link)
link2 = soup.select_one('div#class1	p#second')
print(link2)
print(link2.string)
internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)
h1_all = soup.select('h1')
print('h1_all: ', h1_all)
url_links = soup.select('a')
for link in url_links:
    print(link['href'])
div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])
div_urls2 = soup.select('div#class1 a')
print(div_urls2)
h1 = soup.select('#heading, #footer')
print(h1)
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)
national_anthem =	'''
<!DOCTYPE html>
<html lang="en">
<head>
    <metacharset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>																
    </div>
</body>
</html>
'''
soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').string)
contents = soup.select('p.content')
for content in contents:
    print(content.text)
