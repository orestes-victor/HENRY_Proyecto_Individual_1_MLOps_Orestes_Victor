![Steam](Assets/Steam.png)
<br />


   
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# Sistema de recomendación de videojuegos para usuarios de Steam

## Descripción del Proyecto
Este proyecto se centra en el desarrollo de un sistema de MLOps, abarcando desde la ingeniería de datos hasta la implementación de modelos de aprendizaje automático.

## Contexto
[Steam](https://store.steampowered.com/?l=spanish), creada por Valve Corporation en 2003, es una plataforma de distribución digital de videojuegos inicialmente diseñada para actualizar automáticamente los juegos de Valve. Con el tiempo, se expandió para incluir juegos de otros desarrolladores. Aunque cuenta con más de 325 millones de usuarios y más de 25,000 juegos, las estadísticas precisas son limitadas desde 2018, ya que Steam restringió el acceso a datos detallados.

## Conjunto de datos
El proyecto parte de 3 archivos que nos proporciona [HENRY](https://www.soyhenry.com/) para desarrollar el análisis :

* `australian_user_reviews.json` es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, además de datos adicionales como si recomiendan o no ese juego, emoticones de gracioso y estadísticas de si el comentario fue útil o no para otros usuarios. También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.

* `australian_users_items.json` es un dataset que contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.

* `output_steam_games.json` es un dataset que contiene datos relacionados con los juegos en sí, como los título, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

## Objetivo
___
El objetivo principal es crear un flujo de trabajo eficiente que incluya la recopilación y transformación de datos, análisis exploratorio, desarrollo de modelos y su implementación utilizando prácticas de MLOps. <p/> 

Este proyecto simula el trabajo de un MLOps Engineer combinando las funciones de Data Engineer y Data Scientist para la plataforma Steam. Se requiere desarrollar un Producto Mínimo Viable que incluya una API en la nube y la implementación de dos modelos de Machine Learning: análisis de sentimientos en comentarios de usuarios y recomendación de juegos basada en nombre o preferencias de usuario.

## Etapas del Proyecto
___

![Proceso](Assets/Procesos MLOps.png)
<br />

### 1. Ingeniería de Datos (ETL)
Para iniciar nos centramos en entender los archivos recibidos, en que tipo de formato se presentan y cual es su contenido general.
Para esto último primero revisamos y analizamos el archivo `diccionario de datos de STEAM` para saber con que nos vamos a encontrar. Una vez analizados vemos que dos archivos contienen datos anidados, estos son la columna `reviews` en el archivo `user_reviews.gz.json` y la columna `items` en el archivo `user_items.gz.json`. 

Una vez preparado el dataset, extraemos los archivos y realizamos ETL a cada archivo, podemos enocontrar el codigo que usamos para realizar el ETL [Aqui](https://colab.research.google.com/drive/1wpoG_OeerKu2RNRqlkmaiyt9TrYebUN9?usp=drive_link).

Una vez realizado el ETL vamos encontrar los mismo archivos, pero en un estado mas ordenado y limpio, haciendo click [Aqui](https://drive.google.com/drive/folders/1qvEJ80g96ZBjeuiH_M_Nv5Mnr_GACZ0t?usp=drive_link) con ello podemos dar commienzo a los siguientes pasos en este proyecto.

### 2. Análisis Exploratorio de Datos (EDA)
Se llevó a cabo un Análisis Exploratorio de Datos (EDA) en tres conjuntos de datos que fueron sometidos a un proceso de Extracción, Transformación y Carga (ETL). El objetivo era identificar las variables que serían útiles en la creación de un modelo de recomendación. Para realizar esto, se utilizó la biblioteca Pandas para manipular los datos, y las bibliotecas Matplotlib y Seaborn para visualizar la información.

Específicamente para el modelo de recomendación, se decidió construir un conjunto de datos específico. Este conjunto incluye el identificador del usuario que hizo reseñas, los nombres de los juegos que fueron objeto de comentarios y una columna de calificación. Esta calificación se generó combinando el análisis de sentimientos y las recomendaciones para los juegos.

### 3. Modelo de Aprendizaje Automático
En proceso

### 4. Video Explicativo
En proceso

## Estructura del Repositorio
- **/Assets**: sirve para almacenar y organizar los archivos multimedia y otros recursos necesarios.
- **/Datasets**: Archivos necesarios donde consultará nuestro codigo principal.
- **/Notebooks**: Notebooks de Jupyter utilizados para la exploración y desarrollo.
- **main**: Código principal del proyecto.
- **requirements**: Librerias necesarias para que el modelo funcione en render

## Requisitos de Instalación y Ejecución
En proceso

## Colaboradores
- Orestes Victor
