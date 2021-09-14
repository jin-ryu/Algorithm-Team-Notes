import re

def getUrl(html):
     # \S+ : 공백 문자가 아닌 모든 문자 한개 이상
    p = re.compile('<meta property="og:url" content="https://\S+"')
    r = p.search(html)
    meta = html[r.start(): r.end()]
    
    p = re.compile('content="https://\S+"')
    r = p.search(meta)
    content = meta[r.start(): r.end()]
    
    return content.split('"')[1]

def getLink(html):
    result = []
    
    p = re.compile('<a href="\S+"')
    r = p.findall(html)
    
    for link in r:
        result.append(link.split('"')[1])
    
    return result

def getMatch(html, word):
    # 전부 소문자로 전환
    html = html.lower()
    word = word.lower()
    
    p = re.compile(word)
    w = re.split('[^a-z]', html)
    
    return w.count(word)
    
def solution(word, pages):
    answer = 0
    urls = []
    links = []
    matches = []
    
    for page in pages:
        urls.append(getUrl(page))
        links.append(getLink(page))
        matches.append(getMatch(page, word))
    
    # 링크점수 계산
    scores = [i for i in matches]   # 기본점수 세팅
    
    for i in range(len(pages)):
        for j in range(len(links)):
            if urls[i] in links[j]:
                scores[i] += matches[j] / len(links[j])
    
    max_value = max(scores)
    
    return scores.index(max_value)