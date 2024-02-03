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
Steam, creada por Valve Corporation en 2003, es una plataforma de distribución digital de videojuegos inicialmente diseñada para actualizar automáticamente los juegos de Valve. Con el tiempo, se expandió para incluir juegos de otros desarrolladores. Aunque cuenta con más de 325 millones de usuarios y más de 25,000 juegos, las estadísticas precisas son limitadas desde 2018, ya que Steam restringió el acceso a datos detallados.

## Objetivo
El objetivo principal es crear un flujo de trabajo eficiente que incluya la recopilación y transformación de datos, análisis exploratorio, desarrollo de modelos y su implementación utilizando prácticas de MLOps. Este proyecto simula el trabajo de un MLOps Engineer combinando las funciones de Data Engineer y Data Scientist para la plataforma Steam. Se requiere desarrollar un Producto Mínimo Viable que incluya una API en la nube y la implementación de dos modelos de Machine Learning: análisis de sentimientos en comentarios de usuarios y recomendación de juegos basada en nombre o preferencias de usuario.

## Etapas del Proyecto

### 1. Ingeniería de Datos (ETL)
Para iniciar nos centramos en entender los archivos recibidos, en que tipo de formato se presentan y cual es su contenido general.
Para esto último primero revisamos y analizamos el archivo <diccionario de datos de STEAM> para saber con que nos vamos a encontrar. Una vez analizados vemos que dos archivos contienen datos anidados, estos son la columna <reviews> en el archivo <user_reviews.gz.json> y la columna <items> en el archivo <user_items.gz.json>. 
Podemos encontrar el analisis de este diccionario aqui: [Diccionario de Datos STEAM - Analizado](https://docs.google.com/spreadsheets/d/18snvkj9hfdi9519ACAcNWCXqf43o6TBb/edit?usp=sharing&ouid=115734177680772795416&rtpof=true&sd=true).

Una vez preparado el dataset, extraemos los archivos y realizamos ETL cada archivo, podemos enocontrar el codigo que usamos para realizar el ETL [Aqui](https://colab.research.google.com/drive/1wpoG_OeerKu2RNRqlkmaiyt9TrYebUN9?usp=drive_link)).

Una vez realizado el ETL vamos encontrar los mismo archivos, pero en un estado mas ordenado y limpio, haciendo click [Aqui](https://drive.google.com/drive/folders/1qvEJ80g96ZBjeuiH_M_Nv5Mnr_GACZ0t?usp=drive_link) con ello podemos dar commienzo a los siguientes pasos en este proyecto.




#### 1.1 Transformaciones de Datos
Aquí se describen las transformaciones aplicadas a los datos para adaptarlos a las necesidades del proyecto.

#### 1.2 Feature Engineering
Detalles sobre cómo se mejoran las características de los datos para potenciar el rendimiento del modelo.

#### 1.3 Desarrollo de API
Información sobre la creación de la interfaz de programación de aplicaciones para la comunicación efectiva entre los diferentes componentes del sistema.

### 2. Análisis Exploratorio de Datos (EDA)
Esta sección aborda el análisis exploratorio de los datos para obtener insights significativos antes de desarrollar el modelo.

### 3. Modelo de Aprendizaje Automático
Describe la metodología y el desarrollo del modelo de aprendizaje automático.

### 4. Video Explicativo
Enlace o detalles sobre un video explicativo que presenta el proyecto y su funcionalidad.

## Estructura del Repositorio
- **/data**: Contiene los conjuntos de datos utilizados en el proyecto.
- **/notebooks**: Notebooks de Jupyter utilizados para la exploración y desarrollo.
- **/src**: Código fuente del proyecto.
- **/docs**: Documentación adicional, si es necesario.
- **/videos**: Contiene el video explicativo del proyecto.

## Requisitos de Instalación y Ejecución
Proporciona instrucciones detalladas sobre cómo instalar y ejecutar el proyecto.

## Colaboradores
- Orestes Victor
