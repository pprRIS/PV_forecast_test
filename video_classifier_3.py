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

    # Calcular la distancia a los colores de referencia
    dist_to_blue = np.linalg.norm(frame_first - [255, 0, 0], axis=2)
    dist_to_thick_cloud = np.linalg.norm(frame_first - [128, 128, 128], axis=2)
    dist_to_thin_cloud = np.linalg.norm(frame_first - [255, 255, 255], axis=2)

    # Clasificar los píxeles
    pixels_blue_first = np.count_nonzero(np.logical_and(dist_to_blue < dist_to_thick_cloud, dist_to_blue < dist_to_thin_cloud))
    pixels_thick_cloud_first = np.count_nonzero(np.logical_and(dist_to_thick_cloud < dist_to_blue, dist_to_thick_cloud < dist_to_thin_cloud))
    pixels_thin_cloud_first = np.count_nonzero(np.logical_and(dist_to_thin_cloud < dist_to_blue, dist_to_thin_cloud < dist_to_thick_cloud))

    # Guardar el primer cuadro como imagen
    cv2.imwrite("primer_cuadro.png", frame_first)

    # Imprimir resultados
    print("Primer cuadro:")
    print("Total de píxeles:", pixels_first)
    print("Píxeles clasificados como blue:", pixels_blue_first)
    print("Píxeles clasificados como thick cloud:", pixels_thick_cloud_first)
    print("Píxeles clasificados como thin cloud:", pixels_thin_cloud_first)

    # Clasificación para el último cuadro
    pixels_last = frame_last.shape[0] * frame_last.shape[1]

    # Calcular la distancia a los colores de referencia
    dist_to_blue = np.linalg.norm(frame_last - [255, 0, 0], axis=2)
    dist_to_thick_cloud = np.linalg.norm(frame_last - [128, 128, 128], axis=2)
    dist_to_thin_cloud = np.linalg.norm(frame_last - [255, 255, 255], axis=2)

    # Clasificar los píxeles
    pixels_blue_last = np.count_nonzero(np.logical_and(dist_to_blue < dist_to_thick_cloud, dist_to_blue < dist_to_thin_cloud))
    pixels_thick_cloud_last = np.count_nonzero(np.logical_and(dist_to_thick_cloud < dist_to_blue, dist_to_thick_cloud < dist_to_thin_cloud))
    pixels_thin_cloud_last = np.count_nonzero(np.logical_and(dist_to_thin_cloud < dist_to_blue, dist_to_thin_cloud < dist_to_thick_cloud))

    # Guardar el último cuadro como imagen
    cv2.imwrite("ultimo_cuadro.png", frame_last)

    # Imprimir resultados
    print("Último cuadro:")
    print("Total de píxeles:", pixels_last)
    print("Píxeles clasificados como blue:", pixels_blue_last)
    print("Píxeles clasificados como thick cloud:", pixels_thick_cloud_last)
    print("Píxeles clasificados como thin cloud:", pixels_thin_cloud_last)

    # Liberar el objeto VideoCapture
    cap.release()

if __name__ == "__main__":
    video_path = '/home/paula/Escritorio/bluesky_thinclouds.mp4'
    video_path_2 = '/home/paula/Escritorio/thckthickclouds.mp4'
    video_path_3 = '/home/paula/Escritorio/thick_thinclouds.mp4'
    video_path_4 = '/home/paula/Escritorio/sunset_w_clouds.mp4'

    clasificar_video(video_path)
