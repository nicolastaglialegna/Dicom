! [Versi�n m�s reciente] (https://img.shields.io/pypi/v/pydiq.svg)] (https://pypi.python.org/pypi/pydiq/)
[! [Licencia] (https://img.shields.io/pypi/l/pydiq.svg)] (https://pypi.python.org/pypi/pydiq/)
[! [DOI] (https://zenodo.org/badge/3862/janpipek/pydiq.png)] (http://dx.doi.org/10.5281/zenodo.11480)

pydiq
=====
Sencillo navegador / visor DICOM multiplataforma de c�digo abierto en Python y Qt.

Caracteristicas
--------

* Visualizaci�n f�cil (y r�pida) de todas las im�genes en un directorio
* Zoom (1: N y N: 1)
* Control del mouse del centro de la ventana y el ancho (como en Aeskulap Viewer)
* Medici�n adecuada de las unidades de Hounsfield y posici�n con el mouse.
* Exportaci�n de im�genes PNG

Acciones
-----

* Mejor zoom
* Mejor soporte de im�genes de resonancia magn�tica
* Soporte de im�genes de dosis RT
* Ver en diferentes planos (rectangular + otros).
* Mapeo de coordenadas (utilizando la matriz de traducci�n y rotaci�n)
* Informaci�n del archivo DICOM en una pantalla f�cil de usar.

Dependencias
------------

Package       Version    

------------- -----------

dicom         0.9.9.post1

Jinja2        2.5        

numpy         1.17.0     

pip           19.2.1     

pkg-resources 0.0.0      

pydic         1.0.0      

pydiq         0.2.1      

PyQt5         5.13.0     

PyQt5-sip     4.19.18    

QtPy          1.9.0      

setuptools    41.0.1     

wheel         0.33.4     


Probado en Linux y Windows.

Instalaci�n
------------

1- Crear carpeta donde se alojara el codigo

sudo mkdir Dicom

2- Crear entorno virtual para la ejecucion de la aplicacion

# cd Dicom
# virtualenv -p python3.7 EntornoDicom

Activamos el entorno:

# cd EntornoDicom
EntornoDicom# source bin/activate

Una vez activado el entorno procedemos a alojarnos en la carpeta creada anteriormente

(EntornoDicom)Dicom/EntornoDicom# cd..
(EntornoDicom)Dicom# 

descargamos el repositorio https://github.com/nicolastaglialegna/App-dicom.git

(EntornoDicom)Dicom#  git clone https://github.com/nicolastaglialegna/App-dicom

Ingresamos a la carpeta descargada

(EntornoDicom)Dicom# cd App-dicom
(EntornoDicom)Dicom/App-dicom# cd pydiq-master

Instalamos las librerias necesarias para su funcionamiento
(EntornoDicom)Dicom/App-dicom/pydiq-master# pip install -r instalacion.txt
(EntornoDicom)Dicom/App-dicom/pydiq-master# pip install pydiq

Ejecutamos la aplicacion mediante:
(EntornoDicom)Dicom/App-dicom/pydiq-master# python run.py


Limitaciones
-----------

Actualmente, el visor solo admite radiograf�a computarizada (CR), tomograf�a computarizada (CT) y
Im�genes de resonancia magn�tica (MRI) con orientaci�n normal (x, y, z)
en formato de una porci�n por archivo.