# Proyecto de Procesamiento de Imágenes

Este proyecto tiene como objetivo procesar un conjunto de imágenes mediante técnicas de concurrencia y paralelismo en Python. Se enfoca en aplicar transformaciones básicas, como redimensionamiento y desenfoque, así como la detección de imágenes que contienen rostros utilizando la biblioteca `face_recognition`.

## Requisitos del Proyecto

- **Resolución mínima**: 1200 x 1200 píxeles.
- **Tamaño máximo de las imágenes**: 10 MB.
- **Detección de rostros**: Las imágenes que contienen rostros se guardan en una carpeta específica.
- **Aplicación de desenfoque**: Se aplica un desenfoque a todas las imágenes procesadas.

## Tecnologías y Librerías Utilizadas

- **Lenguaje**: Python 3
- **Librerías**:
  - `Pillow`: Para la manipulación de imágenes.
  - `opencv-python`: Para aplicar desenfoque y guardar imágenes.
  - `face_recognition`: Para la detección de rostros en las imágenes.
  - `numpy`: Para manipulación de arrays y compatibilidad con OpenCV.
  - `concurrent.futures`: Para el manejo de tareas concurrentes y paralelas.
  - `os` y `time`: Para interactuar con el sistema de archivos y medir el tiempo de ejecución.

## Estructura del Proyecto

Programacion Aplicada/
  ├──imagenes/ 
  |  ├── imagenes_originales/ # Carpeta donde se colocan las imágenes originales 
  |  ├── imagenes_procesadas/ # Carpeta donde se guardan las imágenes procesadas 
  |  └── imagenes_con_personas/ # Carpeta donde se guardan las imágenes que contienen caras 
  ├── readme.md
  └── procesar_imagenes.py # Script principal para procesar las imágenes
    



