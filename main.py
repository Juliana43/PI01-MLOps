from fastapi import FastAPI
from funciones import Movies
from sistema_recomendacion import Recomendacion

movies_obj = Movies()
recomendation_obj = Recomendacion()
app = FastAPI()

@app.get('/cantidad_filmaciones_mes/{month}')
async def get_count_movies_month(month: str):
    """Obtenemos la cantidad de películas estrenadas en el mes solicitado.

         Argumentos:
             mes (str, opcional): mes de lanzamiento. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_count_movies_month(month=month)


@app.get('/cantidad_filmaciones_dia/{day}')
async def get_count_movies_day(day: str):
    """Obtenemos la cantidad de películas estrenadas en el día solicitado.

         Argumentos:
             día (str, opcional): Día de lanzamiento. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_count_movies_day(day=day)


@app.get('/score_titulo/{title}')
async def get_score_title(title: str):
    """Obtenemos el año de lanzamiento y la puntuación del título solicitado.

         Argumentos:
             título (str, opcional): Película a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_score_title(title=title)


@app.get('/votos_titulo/{title}')
async def get_votes_title(title: str):
    """Obtenemos el año de publicación, el recuento de votos y el promedio de votos del título solicitado.

         Argumentos:
             título (str, opcional): Película a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_votes_title(title=title)


@app.get('/get_actor/{actor}')
async def get_actor(actor: str):
    """Obtenemos las películas de los actores, la rentabilidad máxima y la rentabilidad media.

         Argumentos:
             actor (str, opcional): Actor a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_actor(actor=actor)


@app.get('/get_director/{director}')
async def get_director(director: str):
    """Obtenemos todas las películas, año de estreno, rendimiento, ingresos y presupuesto del director solicitado.

         Argumentos:
             director (str, opcional): Director a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
    """
    return movies_obj.get_director(director=director)


@app.get('/recomendacion/{title}')
async def get_recomendation(title: str):
    """Obtenemos la recomendación de acuerdo al título solicitado.

    Args:
        title (str, optional): película que se buscará. ''.

    Returns:
        dict: Mensaje con la información solicitada.
    """
    return recomendation_obj.recommendation(title=title)