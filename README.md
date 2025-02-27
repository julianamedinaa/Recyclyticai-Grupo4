---
license: apache-2.0
---
#  **RECYCLYTIC AI** 

### **Nombres:**
1. DANIEL SANIN RAMIREZ
2. JULIANA MEDINA GUERREO
3. JESSICA VIVIANA MARTINEZ MARIN
4. ANDRES FELIPE GARCIA TURRIAGO

# 

### **¿Qué es la reciclaje?**

El reciclaje es el proceso mediante el cual los materiales desechados se transforman en nuevos productos o materias primas para reducir el impacto ambiental. Su objetivo principal es minimizar la cantidad de residuos que terminan en los vertederos, ahorrar recursos naturales y disminuir la contaminación.

El reciclaje suele dividirse en tres etapas:

**Recolección y separación:** Se recogen los residuos reciclables (plástico, papel, vidrio, metal, etc.) y se clasifican según su tipo.

**Procesamiento y transformación:** Los materiales se limpian, trituran o funden para convertirlos en materias primas reutilizables.

**Fabricación de nuevos productos:** Con las materias primas recicladas se crean nuevos objetos, como botellas, papel, ropa o incluso materiales de construcción.

  ![image](https://github.com/user-attachments/assets/f11ba0a5-10af-4bb1-83db-8ccc31fd32d5)

#

### **¿Qué es la RECYCLYTIC AI?**

**RECYCLYTIC AI** es la propuesta de un sistema de clasificación automatizada con el propósito de optimizar la separacion de residuos reciclables en la empresa ECOOReciclaje S.A.S., mejorando la eficiencia operativa y reduciendo errores en el proceso de separación de materiales.

![image](https://github.com/user-attachments/assets/281d4bfe-0d91-46b7-89c4-4d263e4b26cc)
#

### **Propósito y Funcionalidades Principales**

Este proyecto utiliza detección de imagenes para la clasificacion y categorización de residuos y materiales reciclables a partir de tecnicas avanzadas de vision por computadora y deep learning. A través de una red neuronal clasifica los objetos en categorías como papel, cartón, vidrio, metal y plástico, para proporcionar predicciones precisas y confiables.

En condiciones de poca luz, el modelo puede presentar errores debido al ruido en las imágenes o a cambios en la perspectiva de los objetos. Asimismo, es posible que no identifique correctamente residuos poco comunes o que no hayan sido considerados en el conjunto de entrenamiento.

#
### **Requisitos previos**

Antes de instalar y ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

### **Dependencias y librerias necesarias**

### **- Restricciones de Software:**

#### **Sistema operativo**
- Windows 10/11
- mac
- linux

### **licencias**
Este proyecto se distribuye bajo la licencia mit
license APACHE 2.0

**Bibliotecas requeridas:**
- python 3.10+
- tkinter
- PIL (Pillow)
- imutils
- OpenCV
- numpy
- ultralytics (YOLO)
- math
- os
- datetime 
- pyautogui 
Ademas de las utilizadas en **requirements.txt**

### **- Restricciones de Hardware:**

**Procesamiento en tiempo real:**
- CPU de alto rendimiento
- la versión correspondiente de ultralytics instalada
- procesador de 4 nucleos y 2GHz o superior
- 8GB ram o mas
- camara web HD 720p o maximo 4k

#
## **Instalación del Proyecto RecyclytingAI-Grup4**

#### 1. Crea una carpeta en escritorio con el nombre que tu desees

#### 2. Abre VS code --> click derecho dentro de la carpeta, click en "Abrir en Terminal"", escribe "code . " 

#### 3. Clonar el repositorio - control + mayuscula + p, click en "Git: Clone", pega:

 https://github.com/julianamedinaa/RecyclytingAI-Grup4.git

#### 4. En powershell intalar UV: pip install uv

#### 5. Ejecuta el proyecto en la terminal de VS o en powershell con el siguiente comando: uv run main.py

#### 6. para construir y ejecutar el contenedor del Docker usa los siguintes comandos

cd RecyclytingAI-Grup4

docker build -t recyclyticai .
     
docker run -it --rm --device=/dev/video0 recyclyticai /bin/bash









