from kompas.model import KompasScraping

def scrapKompas(url):
    kompas = KompasScraping(url)
    result = kompas.returnListNews()

    return result