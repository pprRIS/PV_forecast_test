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
    dist_to_red = np.linalg.norm(frame_first - [255, 0, 0], axis=2)
    dist_to_gray = np.linalg.norm(frame_first - [128, 128, 128], axis=2)
    dist_to_white = np.linalg.norm(frame_first - [255, 255, 255], axis=2)

    # Clasificar los píxeles filtrados
    pixels_blue_first = np.count_nonzero(dist_to_red < dist_to_gray)
    pixels_blue_first += np.count_nonzero(dist_to_red < dist_to_white)

    # Aplicar máscara para excluir píxeles azules
    mask = np.logical_not(np.logical_or(dist_to_red < dist_to_gray, dist_to_red < dist_to_white))
    frame_first_masked = frame_first[mask]

    # Cálculo de light y clasificación para el primer cuadro
    frame_first_light = (frame_first_masked[..., 0] + frame_first_masked[..., 1] + frame_first_masked[..., 2]) / 3

    # Clasificar los píxeles filtrados
    pixels_thin_cloud_first = np.count_nonzero(frame_first_light > 200)
    pixels_thick_cloud_first = np.count_nonzero(frame_first_light <= 200)

    # Guardar el primer cuadro como imagen
    cv2.imwrite("primer_cuadro.png", frame_first)

    # Imprimir resultados
    print("Primer cuadro:")
    print("Total de píxeles:", pixels_first)
    print("Píxeles clasificados como blue:", pixels_blue_first)
    print("Píxeles clasificados como thin cloud:", pixels_thin_cloud_first)
    print("Píxeles clasificados como thick cloud:", pixels_thick_cloud_first)

    # Clasificación para el último cuadro
    pixels_last = frame_last.shape[0] * frame_last.shape[1]

    # Calcular la distancia a los colores de referencia
    dist_to_red = np.linalg.norm(frame_last - [255, 0, 0], axis=2)
    dist_to_gray = np.linalg.norm(frame_last - [128, 128, 128], axis=2)
    dist_to_white = np.linalg.norm(frame_last - [255, 255, 255], axis=2)

    # Clasificar los píxeles filtrados
    pixels_blue_last = np.count_nonzero(dist_to_red < dist_to_gray)
    pixels_blue_last += np.count_nonzero(dist_to_red < dist_to_white)

    # Aplicar máscara para excluir píxeles azules
    mask_last = np.logical_not(np.logical_or(dist_to_red < dist_to_gray, dist_to_red < dist_to_white))
    frame_last_masked = frame_last[mask_last]

    # Cálculo de light y clasificación para el último cuadro
    frame_last_light = (frame_last_masked[..., 0] + frame_last_masked[..., 1] + frame_last_masked[..., 2]) / 3

    # Clasificar los píxeles filtrados
    pixels_thin_cloud_last = np.count_nonzero(frame_last_light > 200)
    pixels_thick_cloud_last = np.count_nonzero(frame_last_light <= 200)

    # Guardar el último cuadro como imagen
    cv2.imwrite("ultimo_cuadro.png", frame_last)

    # Imprimir resultados
    print("Último cuadro:")
    print("Total de píxeles:", pixels_last)
    print("Píxeles clasificados como blue:", pixels_blue_last)
    print("Píxeles clasificados como thin cloud:", pixels_thin_cloud_last)
    print("Píxeles clasificados como thick cloud:", pixels_thick_cloud_last)

    # Liberar el objeto VideoCapture
    cap.release()

if __name__ == "__main__":
    video_path = '/home/paula/Escritorio/bluesky_thinclouds.mp4'
    video_path_2 = '/home/paula/Escritorio/thckthickclouds.mp4'
    video_path_3 = '/home/paula/Escritorio/thick_thinclouds.mp4'
    video_path_4 = '/home/paula/Escritorio/sunset_w_clouds.mp4'

    clasificar_video(video_path_4)
