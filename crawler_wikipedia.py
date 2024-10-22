from bs4 import BeautifulSoup
import requests


def obtem_url_pagina_do_dia():
    url = 'https://pt.wikipedia.org'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    slug = soup.select_one('div.main-page-responsive-columns.main-page-second-row > div '
                           '> div.main-page-block-contents > div.plainlinks > a')['href']
    url_pagina_do_dia = url + slug
    return url_pagina_do_dia


def obtem_eventos_comemorativos(url_pagina_do_dia):
    response = requests.get(url=url_pagina_do_dia)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_ul_com_eventos = soup.select_one('h3#Brasil').find_next('ul')
    lista_tags_li_com_eventos = tag_ul_com_eventos.select('li')
    lista_eventos = [li.text for li in lista_tags_li_com_eventos]
    return lista_eventos


if __name__ == '__main__':
    url_pagina_do_dia = obtem_url_pagina_do_dia()
    lista_eventos = obtem_eventos_comemorativos(url_pagina_do_dia)
    [print(evento) for evento in lista_eventos]
