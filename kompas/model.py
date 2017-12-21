import bs4
import requests


class KompasScraping:
    def __init__(self, linkIndex):
        self.linkIndex = linkIndex
    def scraptIndexLink(self):
        content = requests.get(self.linkIndex)
        bs = bs4.BeautifulSoup(content.text, "html.parser")

        index = [item['data-ci-pagination-page'] for item in bs.find_all('a', attrs={'data-ci-pagination-page': True})]
        lastPage = int(index[len(index) - 1]) + 1

        urlPagination = []
        for i in range(1, lastPage):
            urlPagination.append("%s%s" % (self.linkIndex,i))

        return urlPagination

    def scraptLinkNews(self, urlIndex):
        news = []
        content = requests.get(urlIndex)
        response = bs4.BeautifulSoup(content.text, "html.parser")
        data = response.find_all('div', 'latest--indeks')
        data = data[0]

        for d in data.select('.article__title--medium'):
            href = d.find_all('a', href=True)

            content = requests.get(href[0]["href"])
            bs = bs4.BeautifulSoup(content.text, "html.parser")

            contentNews = bs.find('div', 'read__content')
            paragrafNews = []
            for paragraf in contentNews.select('p'):
                check = True
                if paragraf.get_text().find('Baca juga') != -1:
                    check = False

                if check and paragraf.get_text().strip() != "":
                    paragrafNews.append(paragraf.get_text().strip())

            listNews = {}
            listNews['url'] = href[0]["href"]
            listNews['title'] = d.get_text()
            listNews['content'] = paragrafNews
            news.append(listNews)

        return news

    def returnListNews(self):

        news = []
        urlIndex = self.scraptIndexLink()
        for url in urlIndex:
            news.append(self.scraptLinkNews(url))

        return news
