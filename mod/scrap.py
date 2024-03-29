from bs4 import BeautifulSoup


def scrap_lang(session):
    url = "http://buildit.iare.ac.in/tutorials"
    response = session.get(url)
    response_edit = response.text[response.text.find("document.getElementById('flat')"):response.text.find(
        '<footer class="bg-dark footer-section">')]
    text = response_edit.split('<li ')
    lang = []
    sel = 'data-flip-title="'
    hr = '/tutorials'
    for i in text:
        a = []
        t = i[i.find(sel):]
        t = t[t.find(sel) + len(sel):t.find('>') - 1]
        lsp = i[i.find(hr):]
        lsp = lsp[:lsp.find('">')]
        a.append(t)
        a.append(lsp)
        lang.append(a)
    lang = lang[1:]
    return lang


#
def scrap_level(session, url):
    url = 'http://buildit.iare.ac.in/tutorials/' + url
    response = session.get(url)
    soup = BeautifulSoup(response.text)
    lt = soup.select('#carousel')[0]
    level = []
    li = lt.select('li')
    a = lt.select('a')
    lil = []
    al = []
    for i in li:
        lil.append(i.attrs['data-flip-title'])
    for i in a:
        al.append(i.attrs['href'])
    for i in range(len(lil)):
        all_li = [lil[i], al[i]]
        level.append(all_li)
    return level[:-3]


def scrap_question(session, url):
    url = 'http://buildit.iare.ac.in/tutorials/' + url
    response = session.get(url)
    soup = BeautifulSoup(response.text)
    l = soup.select('#questions > tbody')[0]
    td = l.select('a')
    qul_all = []
    qul_t = []
    qul_l = []
    cll = []
    for i in td:
        qul_l.append(i['href'])
        qul_t.append(i.text)
    cl = l.select('tr')
    for i in cl:
        cll.append(i['style'])
    for i in range(len(cll)):
        sin = [qul_t[i], qul_l[i], cll[i]]
        qul_all.append(sin)
    return qul_all


def scrap_read(session, url):
    url = 'http://buildit.iare.ac.in/tutorials/questions/' + url
    response = session.get(url)
    soup = BeautifulSoup(response.text)
    liv = soup.select('div.cover')[0]
    liv = liv.text.strip()
    liv = liv.split('\n')
    a = []
    for i in range(len(liv)):
        liv[i] = liv[i].strip()
        if liv[i] != '':
            a.append(liv[i])
    return a
