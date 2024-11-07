import os
import time
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import face_recognition


# Directorio de entrada
input_dir = 'imagenes/imagenes_originales'

# Directorio de salida
output_dir = 'imagenes/imagenes_procesadas'

# Directorio de imagenes con personas 
personas_dir = 'imagenes/imagenes_con_personas'

#Se validad que los directorios existan
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
os.makedirs(personas_dir, exist_ok=True)



#Carga una imagen desde el disco usando OpenCV 
def cargar_imagen(ruta):
    # Intentar cargar la imagen
    imagen = cv2.imread(ruta) 
    
    # Verificar si la imagen fue cargada correctamente
    if imagen is None:
        print(f"No se pudo cargar la imagen. Verifique la ruta: {ruta}")
        return None
    
    # Si la imagen se carga correctamente, mostrar el tamaño
    alto, ancho = imagen.shape[:2]  # Obtener solo alto y ancho (ignorando los canales)
    print(f"Tamaño de la imagen original: {alto}x{ancho} pixeles.")
    
    return imagen

#Función para redimensioar el tamaño de la imagen
def redimensionar(imagen):
    # Verificar si la imagen fue cargada correctamente
    if imagen is None:
        print("No pudimos encontrar la imagen, por favor intente nuevamente.")
        return None

    print("Se redimensionará la imagen a 800x800 píxeles.")
    imagen = Image.fromarray(imagen)
    imagen = imagen.resize((800, 800), Image.Resampling.LANCZOS)
    return np.array(imagen)

#Funcion para guardar la imagen segun si contiene rostros o no
def guardar_imagen(imagen, nombre, es_persona=False):
    # Verificar  que la imagen exista
    if imagen is None:
        print(f"No se puede guardar una imagen vacia, verificar el archivo: {nombre}")
        return

    if es_persona:
        cv2.imwrite(os.path.join(personas_dir, nombre), imagen)
    else:
        cv2.imwrite(os.path.join(output_dir, nombre), imagen, [int(cv2.IMWRITE_JPEG_QUALITY), 85])

#Función para aplicar desenfoque
def aplicar_desenfoque(imagen):
    print("Aplicando desenfoque a la imagen.")
    return cv2.GaussianBlur(imagen, (5, 5), 0)

# Proceso completo de carga, transformación y guardado de la imagen.
def procesar_imagen(ruta):      
    print(f"Imagen a procesar: {ruta}")
    imagen = cargar_imagen(ruta)
    
    # Redimensionar la imagen a 800x800 px
    imagen = redimensionar(imagen)
    
    # Convertir a escala de grises para que CascadeClassifier funcione correctamente
    imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Cargar el clasificador en cascada
    cascada_frontal = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cascada_perfil = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

    # Detectar rostros en ambas orientaciones (frontal y perfil)
    rostros_frontal = cascada_frontal.detectMultiScale(imagen_grises, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))
    rostros_perfil = cascada_perfil.detectMultiScale(imagen_grises, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

    # Combinar ambas detecciones
    rostros = np.concatenate((rostros_frontal, rostros_perfil), axis=0)

    # Comprobar si se detectaron rostros
    contiene_rostros = len(rostros) > 0
    print(f"La imagen: {ruta} contiene rostros: {'Si' if contiene_rostros else 'No'}")

    #Aplicar desenfoque
    imagen_desenfocada = aplicar_desenfoque(imagen)

    #Guardar img e imprimir el direcorio de destino
    nombre_archivo = os.path.basename(ruta)
    print(f"Imagen a guardar: {nombre_archivo}")
    guardar_imagen(imagen_desenfocada, nombre_archivo, contiene_rostros)
    print(f"Imagen guardada en {personas_dir if contiene_rostros else output_dir}")

# Procesamiento Concurrente, Procesa imágenes en paralelo usando ThreadPoolExecutor.
def procesar_imagenes_concurrentemente():
    with ThreadPoolExecutor() as executor:
        for archivo in os.listdir(input_dir):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                executor.submit(procesar_imagen, os.path.join(input_dir, archivo))

# Medición de rendimiento
inicio = time.time()
procesar_imagenes_concurrentemente()
fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")