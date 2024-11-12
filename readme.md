# Proyecto de Procesamiento de Imágenes

Este proyecto tiene como objetivo procesar un conjunto de imágenes utilizando los conceptos de concurrencia y paralelismo en Python. Se enfoca en aplicar transformaciones básicas, como redimensionamiento y desenfoque, así como la detección de imágenes que contienen rostros utilizando funciones de reconocimiento facial (CascadeClassifier) utilizando el modulo cv2 de la libreria OpenCV .

## Objetivos del proyecto

- **Resize de imagenes**: Setear una resolución estandar de las imagenes en **: 800 x 800 píxeles.
- **Escala de grises:**: Aplicar escala de grises en las imagenes.
- **Detección de rostros**: Las imágenes que contienen rostros se guardan en una carpeta específica.
- **Aplicación de desenfoque**: Aplicar un desenfoque a las imágenes procesadas.

## Tecnologías y Librerías Utilizadas

- **Lenguaje**: Python 3
- **Librerías**:
  - `Pillow`: Para la manipulación de imágenes.
  - `opencv-python`: Para procesamiento de imagenes y la detección de rostros.
  - `numpy`: Para manipulación de arrays y compatibilidad con OpenCV.
  - `concurrent.futures`: Para el manejo de tareas concurrentes (ThreadPoolExecutor) y paralelas (ProcessPoolExecutor).
  - `os` y `time`: Para interactuar con el sistema de archivos y medir el tiempo de ejecución.

## Estructura del Proyecto

Programacion Aplicada/
  ├──imagenes/ 
  |  ├── imagenes_originales/ # Carpeta donde se colocan las imágenes originales 
  |  ├── imagenes_procesadas/ # Carpeta donde se guardan las imágenes procesadas 
  |  └── imagenes_con_personas/ # Carpeta donde se guardan las imágenes que contienen caras 
  ├── readme.md
  └── procesar_imagenes.py # Script principal para procesar las imágenes




