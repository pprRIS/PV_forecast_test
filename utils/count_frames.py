import cv2

def obtener_numero_frames(video_path):
    # Abrir el video
    cap = cv2.VideoCapture(video_path)

    # Inicializar contador de frames
    num_frames = 0

    # Leer frames hasta que no haya más
    while True:
        ret, frame = cap.read()

        # Si no se pudo leer el frame, se termina el bucle
        if not ret:
            break

        # Incrementar el contador de frames
        num_frames += 1

    # Cerrar el video
    cap.release()

    return num_frames

if __name__ == "__main__":
    # Ejemplo de uso
    video_path = "/home/paula/python_projects/PV_forecast_test/Cerrado Soleado/thick_thinclouds.mp4"
    num_frames = obtener_numero_frames(video_path)
    print("El video tiene", num_frames, "frames.")
