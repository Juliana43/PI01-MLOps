 
# Sistema de recomendacion de peliculas
<p align=center><img src=_src/movies_cover.png><p>
  
  ### Introduccion
Este sistema de recomendación de películas, es un enfoque basado en MACHINE LEARNING para filtrar o predecir las preferencias cinematográficas de los usuarios en función de sus elecciones y comportamiento anteriores. Es un mecanismo de filtración avanzado que predice las posibles opciones de películas del usuario en cuestión y sus preferencias hacia un elemento específico del dominio, también conocido como película.
  
## Guia de contenidos
  - Proceso de limpieza y preparación de datos (ETL)
  - Análisis exploratorio de Datos (EDA)
  - Modelo de recomendacion
  - API Endpoints
  - Librerias
  
  <p align=center><img src=_src/DiagramaConceptualDelFlujoDeProcesos.png><p>
    
## 1. Proceso de limpieza y preparación de datos (ETL)
El primer paso en nuestro proyecto es la limpieza y preparación de datos. En este paso, normalizamos y limpiamos nuestro conjunto de datos para su posterior análisis y modelado. [Ver mas](https://github.com/Juliana43/PI01-MLOps/blob/main/ETL.ipynb "Ver mas") 
    
## 2. Análisis exploratorio de Datos (EDA)
Una vez que los datos están limpios y preparados, realizamos un EDA para descubrir patrones, tendencias y relaciones en los datos. 
    [Ver mas](https://github.com/Juliana43/PI01-MLOps/blob/main/EDA_ML.ipynb "Ver mas")
    
## 3. Modelo de recomendacion
Usamos el análisis de los datos para construir nuestro sistema de recomendación, que proporciona sugerencias de películas basadas en el título de una película especificada por el usuario. [Ver mas](https://github.com/Juliana43/PI01-MLOps/blob/main/main.py "Ver mas")
    
## 4. API Endpoints
La API ofrece varios puntos finales que brindan funcionalidades únicas para la exploración de datos de películas y la generación de recomendaciones. Aquí describimos cada uno de ellos:
    
**- @app.get('/cantidad_filmaciones_mes/{month}'):** Este endpoints permite conocer la cantidad de filmaciones realizadas en un mes en particular. Solo necesitas indicar el nombre del mes (en español) o su número correspondiente.
    
**- @app.get('/cantidad_filmaciones_dia/{day}'):** De forma similar al anterior, este endpoint devuelve el número de rodajes realizados en un día concreto de cualquier mes. Solo necesita proporcionar el día en formato numérico.
    
**- @app.get('/score_titulo/{title}'):**Le permite conocer la puntuación de popularidad de una película en función de su título. Solo necesita proporcionar el título de la película.
    
**- @app.get('/votos_titulo/{title}'):** Este punto final proporciona información sobre los votos de una película según su título, incluido el número total de votos y el promedio de votos.
    
**- @app.get('/get_actor/{actor}'):** Le permite recuperar información sobre un actor específico, como la cantidad de películas en las que ha participado, el retorno total y el retorno promedio de sus películas. Solo necesitas proporcionar el nombre del actor.
    
**- @app.get('/get_director/{director}'):** Este punto final proporciona información sobre un director específico, como el retorno total de sus películas y una lista de sus películas con detalles como el título, el año de estreno, el retorno, el presupuesto y los ingresos. Solo necesita proporcionar el nombre del director.
    
**- @app.get('/recomendacion/{title}'):** Este es el punto final de recomendación principal que proporciona una lista de películas recomendadas según el título de la película.
    
## 5. Librerias
- pandas
- numpy
- seaborn
- matplotlib
- sklearn
- FastAPI
- Uvicorn
- missingno
- sweetviz
- wordcloud
    
## LICENCIA
   Este proyecto está autorizado bajo la GNU GENERAL LICENSE Version 2, June 1991. [Ver mas](https://github.com/Juliana43/PI01-MLOps/blob/main/LICENSE "Ver mas")
    
    
    
    
  
  
  


  
