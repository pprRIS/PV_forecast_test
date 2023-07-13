import cv2
import numpy as np

def clasificar_video(video_path):
    # Leer el video
    cap = cv2.VideoCapture(video_path)

    # Leer el primer y último cuadro del video
    ret, frame_first = cap.read()
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
    ret, frame_last = cap.read()

    # Clasificación para el primer cuadro
    pixels_first = frame_first.shape[0] * frame_first.shape[1]

    # Rango de valores para la clasificación azul
    azul_min = [200, 0, 0]
    azul_max = [255, 50, 50]

    # Rango de valores para la clasificación gris
    gris_min = [120, 120, 120]
    gris_max = [180, 180, 180]

    # Rango de valores para la clasificación blanco
    blanco_min = [200, 200, 200]
    blanco_max = [255, 255, 255]

    # Rango de valores para la clasificación anaranjado
    anaranjado_min = [0, 100, 200]
    anaranjado_max = [100, 200, 255]

    # Calcular la media de cada intervalo de colores
    media_azul = np.mean([azul_min, azul_max], axis=0)
    media_gris = np.mean([gris_min, gris_max], axis=0)
    media_blanco = np.mean([blanco_min, blanco_max], axis=0)
    media_anaranjado = np.mean([anaranjado_min, anaranjado_max], axis=0)

    # Calcular las distancias de los píxeles a las medias de los intervalos de colores
    dist_to_media_azul = np.linalg.norm(frame_first - media_azul, axis=2)
    dist_to_media_gris = np.linalg.norm(frame_first - media_gris, axis=2)
    dist_to_media_blanco = np.linalg.norm(frame_first - media_blanco, axis=2)
    dist_to_media_anaranjado = np.linalg.norm(frame_first - media_anaranjado, axis=2)

    # Clasificar los píxeles del primer cuadro
    pixels_azul_first = np.count_nonzero(
        np.logical_and(
            dist_to_media_azul < dist_to_media_gris,
            dist_to_media_azul < dist_to_media_blanco,
            dist_to_media_azul < dist_to_media_anaranjado
        )
    )

    pixels_gris_first = np.count_nonzero(
        np.logical_and(
            dist_to_media_gris < dist_to_media_azul,
            dist_to_media_gris < dist_to_media_blanco,
            dist_to_media_gris < dist_to_media_anaranjado
        )
    )

    pixels_blanco_first = np.count_nonzero(
        np.logical_and(
            dist_to_media_blanco < dist_to_media_azul,
            dist_to_media_blanco < dist_to_media_gris,
            dist_to_media_blanco < dist_to_media_anaranjado
        )
    )

    pixels_anaranjado_first = np.count_nonzero(
        np.logical_and(
            dist_to_media_anaranjado < dist_to_media_azul,
            dist_to_media_anaranjado < dist_to_media_gris,
            dist_to_media_anaranjado < dist_to_media_blanco
        )
    )

    # Clasificación para el último cuadro
    pixels_last = frame_last.shape[0] * frame_last.shape[1]

    # Calcular las distancias de los píxeles a las medias de los intervalos de colores
    dist_to_media_azul = np.linalg.norm(frame_last - media_azul, axis=2)
    dist_to_media_gris = np.linalg.norm(frame_last - media_gris, axis=2)
    dist_to_media_blanco = np.linalg.norm(frame_last - media_blanco, axis=2)
    dist_to_media_anaranjado = np.linalg.norm(frame_last - media_anaranjado, axis=2)

    # Clasificar los píxeles del último cuadro
    pixels_azul_last = np.count_nonzero(
        np.logical_and(
            dist_to_media_azul < dist_to_media_gris,
            dist_to_media_azul < dist_to_media_blanco,
            dist_to_media_azul < dist_to_media_anaranjado
        )
    )

    pixels_gris_last = np.count_nonzero(
        np.logical_and(
            dist_to_media_gris < dist_to_media_azul,
            dist_to_media_gris < dist_to_media_blanco,
            dist_to_media_gris < dist_to_media_anaranjado
        )
    )

    pixels_blanco_last = np.count_nonzero(
        np.logical_and(
            dist_to_media_blanco < dist_to_media_azul,
            dist_to_media_blanco < dist_to_media_gris,
            dist_to_media_blanco < dist_to_media_anaranjado
        )
    )

    pixels_anaranjado_last = np.count_nonzero(
        np.logical_and(
            dist_to_media_anaranjado < dist_to_media_azul,
            dist_to_media_anaranjado < dist_to_media_gris,
            dist_to_media_anaranjado < dist_to_media_blanco
        )
    )

    # Guardar el primer y último cuadro como imágenes
    cv2.imwrite("primer_cuadro.png", frame_first)
    cv2.imwrite("ultimo_cuadro.png", frame_last)

    # Imprimir resultados
    print("Primer cuadro:")
    print("Total de píxeles:", pixels_first)
    print("Píxeles clasificados como azul:", pixels_azul_first)
    print("Píxeles clasificados como gris:", pixels_gris_first)
    print("Píxeles clasificados como blanco:", pixels_blanco_first)
    print("Píxeles clasificados como anaranjado:", pixels_anaranjado_first)

    print("Último cuadro:")
    print("Total de píxeles:", pixels_last)
    print("Píxeles clasificados como azul:", pixels_azul_last)
    print("Píxeles clasificados como gris:", pixels_gris_last)
    print("Píxeles clasificados como blanco:", pixels_blanco_last)
    print("Píxeles clasificados como anaranjado:", pixels_anaranjado_last)

    # Liberar el objeto VideoCapture
    cap.release()

if __name__ == "__main__":
    video_path = '/home/paula/Escritorio/bluesky_thinclouds.mp4'
    video_path_2 = '/home/paula/Escritorio/thckthickclouds.mp4'
    video_path_3 = '/home/paula/Escritorio/thick_thinclouds.mp4'
    video_path_4 = '/home/paula/Escritorio/sunset_w_clouds.mp4'

    clasificar_video(video_path_4)
