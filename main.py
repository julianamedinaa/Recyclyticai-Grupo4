# Libraries
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math
import os
from datetime import datetime
import pyautogui

def clean_lbl():
    """Clear the image labels."""
    lblimg.config(image='')
    lblimgtxt.config(image='')

def images(img, imgtxt):
    img = img
    imgtxt = imgtxt

    """Update the displayed images."""
    img = np.array(img, dtype="uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = Image.fromarray(img)

    img_ = ImageTk.PhotoImage(image=img)
    lblimg.configure(image=img_)
    lblimg.image = img_

    # Img Text
    imgtxt = np.array(imgtxt, dtype="uint8")
    imgtxt = cv2.cvtColor(imgtxt, cv2.COLOR_BGR2RGB)
    imgtxt = Image.fromarray(imgtxt)

    img_txt = ImageTk.PhotoImage(image=imgtxt)
    lblimgtxt.configure(image=img_txt)
    lblimgtxt.image = img_txt

# Scanning Function
def Scanning():
    global frame_show  # Hacerla accesible desde tomar_captura()
    global img_metal, img_glass, img_plastic, img_carton, img_medical
    global img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medicaltxt, pantalla
    global lblimg, lblimgtxt

    # Interfaz
    lblimg = Label(pantalla)
    lblimg.place(x=75, y=260)

    lblimgtxt = Label(pantalla)
    lblimgtxt.place(x=995, y=310)
    detect = False

    # Read VideoCapture
    if cap is not None:
     ret, frame = cap.read()
     if not ret or frame is None:
        print("⚠️ No se pudo leer un frame de la cámara.")
        return
     frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # True
     if ret == True:
            # Yolo | Procesar el frame
            results = model(frame, stream=True, verbose=False)
            for res in results:
                # Box
                boxes = res.boxes
                for box in boxes:
                    detect = True
                    # Bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Error < 0
                    if x1 < 0: x1 = 0
                    if y1 < 0: y1 = 0
                    if x2 < 0: x2 = 0
                    if y2 < 0: y2 = 0

                    # Class
                    cls = int(box.cls[0])

                    # Confidence
                    conf = math.ceil(box.conf[0])
                    #print(f"Clase: {cls} Confidence: {conf}")
                    # Metal
                    if cls == 0:
                        # Draw
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                        # Text
                        text = f'{clsName[cls]} {int(conf) * 100}%'
                        sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                        dim = sizetext[0]
                        baseline = sizetext[1]
                        # Rect
                        cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (0, 0, 0),cv2.FILLED)
                        cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

                        # Clasificacion
                        images(img_metal, img_metaltxt)

                    if cls == 1:
                        # Draw
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 255), 2)
                        # Text
                        text = f'{clsName[cls]} {int(conf) * 100}%'
                        sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                        dim = sizetext[0]
                        baseline = sizetext[1]
                        # Rect
                        cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline),
                                      (0, 0, 0), cv2.FILLED)
                        cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                        # Clasificacion
                        images(img_glass, img_glasstxt)

                    if cls == 2:
                        # Draw
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        # Text
                        text = f'{clsName[cls]} {int(conf) * 100}%'
                        sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                        dim = sizetext[0]
                        baseline = sizetext[1]
                        # Rect
                        cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline),
                                      (0, 0, 0), cv2.FILLED)
                        cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                        # Clasificacion
                        images(img_plastic, img_plastictxt)

                    if cls == 3:
                        # Draw
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), (150, 150, 150), 2)
                        # Text
                        text = f'{clsName[cls]} {int(conf) * 100}%'
                        sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                        dim = sizetext[0]
                        baseline = sizetext[1]
                        # Rect
                        cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline),
                                      (0, 0, 0), cv2.FILLED)
                        cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)

                        # Clasificacion
                        images(img_carton, img_cartontxt)

                    if cls == 4:
                        # Draw
                        cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 0, 0), 2)
                        # Text
                        text = f'{clsName[cls]} {int(conf) * 100}%'
                        sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                        dim = sizetext[0]
                        baseline = sizetext[1]
                        # Rect
                        cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline),
                                      (0, 0, 0), cv2.FILLED)
                        cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                        # Clasificacion
                        images(img_medical, img_medicaltxt)

            if detect == False:
                # Clean
                clean_lbl()


            # Resize
            frame_show = imutils.resize(frame_show, width=640)

            # Convertimos el video
            im = Image.fromarray(frame_show)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, Scanning)

    else:
            cap.release()
 
# Tomar Captura 
def tomar_captura():
    global pantalla  # La ventana de Tkinter

    # Definir la carpeta donde se guardarán las capturas
    carpeta_capturas = "capturas"

    try:
        # Crear la carpeta si no existe
        if not os.path.exists(carpeta_capturas):
            os.makedirs(carpeta_capturas)
            print(f"✅ Carpeta '{carpeta_capturas}' creada correctamente.")

        # Obtener coordenadas de la ventana de la aplicación
        x0 = pantalla.winfo_rootx()
        y0 = pantalla.winfo_rooty()
        x1 = x0 + pantalla.winfo_width()
        y1 = y0 + pantalla.winfo_height()

        # Generar un nombre de archivo con fecha y hora
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(carpeta_capturas, f"ventana_{timestamp}.png")

        # Capturar solo la ventana de la aplicación
        screenshot = pyautogui.screenshot(region=(x0, y0, x1 - x0, y1 - y0))
        screenshot.save(filename)

        print(f"✅ Captura de la ventana guardada en {filename}")

    except Exception as e:
        print(f"⚠️ Error en la captura de la ventana: {e}")

# main
def ventana_principal():
    global cap, lblVideo, model, clsName, img_metal, img_glass, img_plastic, img_carton, img_medical
    global img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medicaltxt, pantalla
    # Ventana principal
    pantalla = Tk()
    pantalla.title("RECICLAJE INTELIGENTE")
    pantalla.geometry("1280x720")
    pantalla.configure(bg="#2E3B55") # Color de fondo

    # Background
    imagenF = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagenF, text="Inicio")
    background.place(x=0, y=0, relwidth=1, relheight=1)

        # Clases: 0 -> Metal | 1 -> Glass | 2 -> Plastic | 3 -> Carton | 4 -> Medical
    # Model
    model = YOLO('Modelos/best.pt')

    # Clases
    clsName = ['Metal', 'Glass', 'Plastic', 'Carton', 'Medical']

    # Images
    img_metal = cv2.imread("setUp/metal.png")
    img_glass = cv2.imread("setUp/vidrio.png")
    img_plastic = cv2.imread("setUp/plastico.png")
    img_carton = cv2.imread("setUp/carton.png")
    img_medical = cv2.imread("setUp/medical.png")
    img_metaltxt = cv2.imread("setUp/metaltxt.png")
    img_glasstxt = cv2.imread("setUp/vidriotxt.png")
    img_plastictxt = cv2.imread("setUp/plasticotxt.png")
    img_cartontxt = cv2.imread("setUp/cartontxt.png")
    img_medicaltxt = cv2.imread("setUp/medicaltxt.png")

    # Video
    lblVideo = Label(pantalla)
    lblVideo.place(x=320, y=180)

     # Elegimos la camara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)
 
    # Añadir Boton a la interfaz
    btn_captura = Button(pantalla, text="Capturar Imagen", command=tomar_captura, font=("Arial", 12), bg="#FFD700", fg="black")
    btn_captura.place(x=550, y=600, width=180, height=40)

    # Iniciando Escaneo
    Scanning()

    # Eject
    pantalla.mainloop()
    
if __name__ == "__main__":
    ventana_principal()


