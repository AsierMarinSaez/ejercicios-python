# coding=utf-8
__Author__="José Gaspar Sánchez García"
from bs4 import BeautifulSoup
import requests, webbrowser

# Programa principal
def main():
    print("Web Scrapping con Beatiful Soap")
    print(30*"=")
    url="https://www.elmundo.es/quijote/capitulo.html?cual=1";
    print("Abriendo página web {0} en una nueva pestaña.".format(url))
    webbrowser.open_new_tab(url)
    print("WEB SCRAPPING")
    print(30*"=")

    
    resultado=requests.get(url)
    html=resultado.text;

    sopa=BeautifulSoup(html)
    print(sopa.prettify())

    texto=sopa.find('div',id='contenido').get_text()


    txt=texto.replace("Prólogo","").replace("Capítulo II","").replace("<","").replace(">","")

    print(txt)

    # Guardamos el texto en un fichero

    nombreFichero=input("Introduzca el nombre del fichero a guardar: ")
    with open(nombreFichero,'w') as fichero :
        fichero.write("Don Quijote de la Mancha:\n")
        fichero.write(50*"="+"\n")
        fichero.write(txt)
        fichero.close()
    print("El fichero "+nombreFichero+" ha sido escrito.")

if __name__== "__main__" :
   main()
