#mejorar la clasificación me lo clasifica
#en cerrado soleado que es el else final

import cv2
import numpy as np
import os

def clasificar_video(video_path):
    # Leer el video
    cap = cv2.VideoCapture(video_path)

    # Leer el primer y último cuadro del video
    ret, frame_first = cap.read()
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
    ret, frame_last = cap.read()

    # Calcular el total de píxeles en los cuadros
    total_pixels_first = frame_first.shape[0] * frame_first.shape[1]
    total_pixels_last = frame_last.shape[0] * frame_last.shape[1]

    # Rango de valores para la clasificación azul
    azul_min = [0, 0, 200]
    azul_max = [50, 50, 255]

    # Rango de valores para la clasificación gris
    gris_min = [120, 120, 120]
    gris_max = [180, 180, 180]

    # Rango de valores para la clasificación blanco
    blanco_min = [200, 200, 200]
    blanco_max = [255, 255, 255]

    # Rango de valores para la clasificación anaranjado
    anaranjado_min = [0, 100, 200]
    anaranjado_max = [100, 200, 255]

    # Calcular la cantidad de píxeles de cada color en el primer cuadro
    pixels_azul_first = np.count_nonzero(
        np.logical_and(
            np.all(frame_first >= azul_min, axis=2),
            np.all(frame_first <= azul_max, axis=2)
        )
    )
    pixels_gris_first = np.count_nonzero(
        np.logical_and(
            np.all(frame_first >= gris_min, axis=2),
            np.all(frame_first <= gris_max, axis=2)
        )
    )
    pixels_blanco_first = np.count_nonzero(
        np.logical_and(
            np.all(frame_first >= blanco_min, axis=2),
            np.all(frame_first <= blanco_max, axis=2)
        )
    )
    pixels_anaranjado_first = np.count_nonzero(
        np.logical_and(
            np.all(frame_first >= anaranjado_min, axis=2),
            np.all(frame_first <= anaranjado_max, axis=2)
        )
    )

    # Calcular la cantidad de píxeles de cada color en el último cuadro
    pixels_azul_last = np.count_nonzero(
        np.logical_and(
            np.all(frame_last >= azul_min, axis=2),
            np.all(frame_last <= azul_max, axis=2)
        )
    )
    pixels_gris_last = np.count_nonzero(
        np.logical_and(
            np.all(frame_last >= gris_min, axis=2),
            np.all(frame_last <= gris_max, axis=2)
        )
    )
    pixels_blanco_last = np.count_nonzero(
        np.logical_and(
            np.all(frame_last >= blanco_min, axis=2),
            np.all(frame_last <= blanco_max, axis=2)
        )
    )
    pixels_anaranjado_last = np.count_nonzero(
        np.logical_and(
            np.all(frame_last >= anaranjado_min, axis=2),
            np.all(frame_last <= anaranjado_max, axis=2)
        )
    )

    # Calcular el porcentaje de píxeles de cada color en el primer y último cuadro
    percentage_azul_first = (pixels_azul_first / total_pixels_first) * 100
    percentage_gris_first = (pixels_gris_first / total_pixels_first) * 100
    percentage_blanco_first = (pixels_blanco_first / total_pixels_first) * 100
    percentage_anaranjado_first = (pixels_anaranjado_first / total_pixels_first) * 100

    percentage_azul_last = (pixels_azul_last / total_pixels_last) * 100
    percentage_gris_last = (pixels_gris_last / total_pixels_last) * 100
    percentage_blanco_last = (pixels_blanco_last / total_pixels_last) * 100
    percentage_anaranjado_last = (pixels_anaranjado_last / total_pixels_last) * 100

    # Clasificar el video en la carpeta correspondiente
    video_name = os.path.basename(video_path)
    if (percentage_azul_first > 60 and percentage_azul_last > 60 and percentage_anaranjado_first < 10 and percentage_anaranjado_last < 10):
        classification_folder = "Cielo despejado"
    elif (percentage_azul_first > 60 and percentage_azul_last > 60 and percentage_anaranjado_first >= 10 and percentage_anaranjado_last >= 10):
        classification_folder = "Despejado Soleado"
    elif (percentage_blanco_first > 50 and percentage_blanco_last > 50):
        classification_folder = "Nublado"
    elif  (percentage_gris_first > 50 and percentage_gris_last > 50):
        classification_folder = "Cerrado"
    else:
        classification_folder = "Cerrado Soleado"

    # Mover el video a la carpeta correspondiente
    destination_folder = os.path.join(classification_folder, video_name)
    os.makedirs(classification_folder, exist_ok=True)
    os.rename(video_path, destination_folder)

    # Liberar el objeto VideoCapture
    cap.release()

if __name__ == "__main__":
    video_path = '/home/paula/Escritorio/bluesky_thinclouds.mp4'
    video_path_2 = '/home/paula/Escritorio/thckthickclouds.mp4'
    video_path_3 = '/home/paula/Escritorio/thick_thinclouds.mp4'
    video_path_4 = '/home/paula/Escritorio/sunset_w_clouds.mp4'

    clasificar_video(video_path)