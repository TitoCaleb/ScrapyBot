from bs4 import BeautifulSoup
import requests
from Bases_datos.conexion_sqlite import insert, limpiarData
from clases import Productos
from datetime import date, timedelta

website = ('https://www.impacto.com.pe/catalogo',
           'https://www.sercoplus.com/731-armando-tu-pc',
           'https://cyccomputer.pe/250-pc-componentes')

# Contador
cont = 1

# Listas IMPACTO
nombresIMPACTO = []
preciosIMPACTO = []
imagenIMPACTO = []
urlImpacto = []

# Listas Sercoplus
preciosSERCOPLUS = []
nombresSERCOPLUS = []
imagenSERCOPLUS = []
urlSERCOPLUS = []

# Listas CYC
preciosCYC = []
nombresCYC = []
imagenCYC = []
urlCYC = []

# hoy = date.today()
# ayer = hoy - timedelta(1)
# limpiarData(ayer)

# Bucle recolector
for i in website:
    result = requests.get(i)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # IMPACTO
    if cont == 1:
        # # PAGINACION IMPACTO
        # paginationImpacto = soup.find('ul', class_='pagination')
        # pagesImpacto = paginationImpacto.find_all('li', class_='page-item')
        # last_pageImpacto = pagesImpacto[-2].text
        #
        # for page in range(1,2): #int(last_pageImpacto)+1
        #     url = f'{i}?page={page}'
        #     re_urlimpacto = requests.get(url)
        #     contenidoImpacto = re_urlimpacto.text
        #     soupImpacto = BeautifulSoup(contenidoImpacto, 'lxml')
        #     try:
        #         rowsNombreImpacto = soupImpacto.find('div', attrs='row p-3').findAll('h4',
        #                                                                              class_='text-center product-title')
        #         rowsPrecioImpacto = soupImpacto.find('div', attrs='row p-3').findAll('span', class_='price-sale-2')
        #         rowsImagenImpacto = soupImpacto.find('div', attrs='row p-3').findAll('img', class_='first-image')
        #         rowsUrlImpacto = soupImpacto.find('div', attrs='row p-3').findAll('div', class_="product-image")
        #
        #         for row_nombre in rowsNombreImpacto:
        #             nombre = row_nombre.get_text("", "\n")
        #             nombresIMPACTO.append(nombre)
        #             pass
        #
        #         for row_precio in rowsPrecioImpacto:
        #             precio = row_precio.get_text("", "\n")
        #             preciotxt = precio
        #             indiceDolar = precio.index("$")
        #             finalDolar = precio.index(" -")
        #             indiceSoles = precio.index("S")
        #             precioFinal = f'{preciotxt[indiceDolar:finalDolar]} - {preciotxt[indiceSoles:]}'
        #             preciosIMPACTO.append(precioFinal)
        #             pass
        #
        #         for row_imagen in rowsImagenImpacto:
        #             imagen = row_imagen.get('src')
        #             imagenIMPACTO.append(str(imagen))
        #             pass
        #
        #         for row_url in rowsUrlImpacto:
        #             url = row_url.find('a').get('href')
        #             urlImpacto.append(str(url))
        #
        #     except:
        #         pass

        # for z in range(0, len(preciosIMPACTO)):
        #     producto = Productos(nombresIMPACTO[z], preciosIMPACTO[z], 'IMPACTO', imagenIMPACTO[z], urlImpacto[z])
        #     insert(producto)
        print('Impacto: DONE')

    # SERCOPLUS
    elif cont == 2:
        # PAGINACION SERCOPLUS
        paginationSercoplus = soup.find('ul', class_='page-list')
        pagesSercoplus = paginationSercoplus.find_all('li')
        last_pageSercoplus = pagesSercoplus[-2].text

        for page in range(1, 2): #int(last_pageSercoplus)+1
            url = f'{i}?page={page}'
            re_urlSercoplus = requests.get(url)
            contenidoSercoplus = re_urlSercoplus.text
            soupSercoplus = BeautifulSoup(contenidoSercoplus, 'lxml')
            try:
                rowsNombreSercoplus = soupSercoplus.find('section', id='products').findAll('h5', class_='product-name')
                rowsPrecioSercoplus = soupSercoplus.find('section', id='products').findAll('div',
                                                                                           class_='first-prices d-flex flex-column')
                rowsImagenSercoplus = soupSercoplus.find('section', id='products').findAll('img')
                rowsUrlSercoplus = soupSercoplus.find('section', id='products').find_all('div',
                                                                                         class_='product-thumbnail')

                for row_nombre in rowsNombreSercoplus:
                    nombre = row_nombre.get_text()
                    nombresSERCOPLUS.append(nombre)
                    pass

                for row_precio in rowsPrecioSercoplus:
                    precio = row_precio.get_text("", "\n")
                    indexer = precio.find('(')
                    indexerSercoplus = precio[:indexer] + ' - ' + precio[indexer:]
                    preciosSERCOPLUS.append(indexerSercoplus)
                    pass

                for row_imagen in rowsImagenSercoplus:
                    imagen = row_imagen.get('data-original')
                    imagenSERCOPLUS.append(str(imagen))
                    pass

                for row_url in rowsUrlSercoplus:
                    url = row_url.find('a').get('href')
                    urlSERCOPLUS.append(str(url))
                    pass

            except:
                pass

        # for z in range(0, len(preciosSERCOPLUS)):
        #     producto = Productos(nombresSERCOPLUS[z], preciosSERCOPLUS[z], 'SERCOPLUS', imagenSERCOPLUS[z],
        #                          urlSERCOPLUS[z])
        #     insert(producto)
        print('SercoPlus: DONE')

    # CYComputer
    elif cont == 3:
        # PAGINACION CYC
        paginationCyc = soup.find('ul', class_='page-list clearfix text-sm-center')
        pagesCyc = paginationCyc.find_all('li')
        last_pageCyc = pagesCyc[-2].text

        for page in range(1, 2): #int(last_pageCyc)+1
            url = f'{i}?page={page}'
            re_urlCYC = requests.get(url)
            contenidoCYC = re_urlCYC.text
            soupCYC = BeautifulSoup(contenidoCYC, 'lxml')
            try:
                rowsNombresCYC = soupCYC.find('section', id='products').findAll('h2', class_='productName')
                rowsPrecioCYC = soupCYC.find('section', id='products').findAll('span', class_='price pr')
                rowsImagenCyC = soupCYC.find('section', id='products').findAll('span', class_='cover_image')
                rowsUrlCyC = soupCYC.find('section', id='products').findAll('div', class_='laberProduct-container')

                for row_nombre in rowsNombresCYC[0:24]:
                    nombre = row_nombre.get_text()
                    nombresCYC.append(nombre)
                    pass

                for row_precio in rowsPrecioCYC:
                    preciocyc = row_precio.get_text("", "\n").split()
                    CYCprecio = f"{preciocyc[0]} - {preciocyc[2]}"
                    preciosCYC.append(CYCprecio)
                    pass

                for row_imagen in rowsImagenCyC[0:24]:
                    imagen = row_imagen.find('img')
                    txt_imagen = str(imagen)
                    indice_src = txt_imagen.index('src="')
                    indice_comilla = txt_imagen.index('" width')
                    nuevaimagen = txt_imagen[indice_src + 5:indice_comilla]
                    imagenCYC.append(nuevaimagen)
                    pass

                for row_url in rowsUrlCyC[0:24]:
                    url = row_url.find('a').get('href')
                    urlCYC.append(str(url))
                    pass

            except:
                pass

        # for z in range(0, len(preciosCYC)):
        #     producto = Productos(nombresCYC[z], preciosCYC[z], 'CYComputer', imagenCYC[z], urlCYC[z])
        #     insert(producto)

        print("CYC: DONE")

    cont = cont + 1
