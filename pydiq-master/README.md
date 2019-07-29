! [Versión más reciente] (https://img.shields.io/pypi/v/pydiq.svg)] (https://pypi.python.org/pypi/pydiq/)
[! [Licencia] (https://img.shields.io/pypi/l/pydiq.svg)] (https://pypi.python.org/pypi/pydiq/)
[! [DOI] (https://zenodo.org/badge/3862/janpipek/pydiq.png)] (http://dx.doi.org/10.5281/zenodo.11480)

pydiq
=====
Sencillo navegador / visor DICOM multiplataforma de código abierto en Python y Qt.

Caracteristicas
--------

* Visualización fácil (y rápida) de todas las imágenes en un directorio
* Zoom (1: N y N: 1)
* Control del mouse del centro de la ventana y el ancho (como en Aeskulap Viewer)
* Medición adecuada de las unidades de Hounsfield y posición con el mouse.
* Exportación de imágenes PNG

Acciones
-----

* Mejor zoom
* Mejor soporte de imágenes de resonancia magnética
* Soporte de imágenes de dosis RT
* Ver en diferentes planos (rectangular + otros).
* Mapeo de coordenadas (utilizando la matriz de traducción y rotación)
* Información del archivo DICOM en una pantalla fácil de usar.

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

Instalación
------------

1- Crear carpeta donde se alojara el codigo

sudo mkdir Dicom

2- Crear entorno virtual para la ejecucion de la aplicacion

##### cd Dicom
##### virtualenv -p python3.7 EntornoDicom

Activamos el entorno:

##### cd EntornoDicom
EntornoDicom# source bin/activate

Una vez activado el entorno procedemos a alojarnos en la carpeta creada anteriormente

(EntornoDicom)Dicom/EntornoDicom# cd..
(EntornoDicom)Dicom# 

descargamos el repositorio https://github.com/nicolastaglialegna/Dicom.git

(EntornoDicom)Dicom#  git clone https://github.com/nicolastaglialegna/Dicom.git

Ingresamos a la carpeta descargada

(EntornoDicom)Dicom# cd Dicom
(EntornoDicom)Dicom/Dicom# cd pydiq-master

Instalamos las librerias necesarias para su funcionamiento
(EntornoDicom)Dicom/Dicom/pydiq-master# pip install -r instalacion.txt
(EntornoDicom)Dicom/Dicom/pydiq-master# pip install pydiq

Ejecutamos la aplicacion mediante:
(EntornoDicom)Dicom/App-dicom/pydiq-master# python run.py


Limitaciones
-----------

Actualmente, el visor solo admite radiografía computarizada (CR), tomografía computarizada (CT) y
Imágenes de resonancia magnética (MRI) con orientación normal (x, y, z)
en formato de una porción por archivo.
