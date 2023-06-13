import pandas as pd

class Movies():
    """Clase que contiene todas las funciones que necesita la API."""

    def __init__(self):
        """Constructor"""
        url='https://drive.google.com/file/d/1UxZlxSz8MsyNR-X5dVNkOranIZncSEDy/view?usp=sharing'
        url='https://drive.google.com/uc?id=' + url.split('/')[-2]
        self._df_movies = pd.read_csv(url)
        self._df_movies['release_date'] = pd.to_datetime(self._df_movies['release_date'],
                                                         format='%Y-%m-%d')


    def get_count_movies_month(self, month=''):
        """Obtenemos la cantidad de películas estrenadas en el mes solicitado.

         Argumentos:
             mes (str, opcional): mes de lanzamiento. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        valid_months = {'enero': '1', 'febrero': '2', 'marzo': '3', 'abril': '4',
                        'mayo': '5', 'junio': '6', 'julio': '7', 'agosto': '8',
                        'septiembre': '9', 'setiembre': '9', 'octubre': '10',
                        'noviembre': '11', 'diciembre': '12'}

        if month.lower() in valid_months:
            variable = valid_months.get(month.lower())
            condition = self._df_movies['release_date'].dt.strftime('%m') == variable
            return {'mes': month,
                    'cantidad': f'{self._df_movies[condition]["title"].count()}'}

        return {'message': f'Month not exists: {month}'}


    def get_count_movies_day(self, day=''):
        """Obtenemos la cantidad de películas estrenadas en el día solicitado.

         Argumentos:
             día (str, opcional): Día de lanzamiento. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        valid_days = {'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
                      'viernes': 4, 'sabado': 5, 'domingo': 6}

        if day.lower() in valid_days:
            condition = self._df_movies['release_date'].dt.dayofweek == valid_days.get(day.lower())
            return {'dia': day, 'cantidad': f'{self._df_movies[condition]["title"].count()}'}

        return {'message': f'Mes no existente: {day}'}


    def get_score_title(self, title=''):
        """Obtenemos el año de lanzamiento y la puntuación del título solicitado.

         Argumentos:
             título (str, opcional): Película a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        df_aux = self._df_movies['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies.iloc[index][['title', 'release_year', 'popularity']]
            return {'titulo': f'{df_aux["title"].values[0]}',
                    'anio': f'{df_aux["release_year"].values[0]}',
                    'popularidad': f'{df_aux["popularity"].values[0].round(1)}'}

        return {'message': f'Movie `{title}` not found'}


    def get_votes_title(self, title=''):
        """Obtenemos el año de publicación, el recuento de votos y el promedio de votos del título solicitado.

         Argumentos:
             título (str, opcional): Película a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        df_aux = self._df_movies['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies.iloc[index][['title', 'release_year', 'vote_count',
                                                  'vote_average']]
            if df_aux["vote_count"].values[0] >= 2000:
                return {'titulo': f'{df_aux["title"].values[0]}',
                        'anio': f'{df_aux["release_year"].values[0]}',
                        'voto_total': f'{int(df_aux["vote_count"].values[0])}',
                        'voto_promedio': f'{df_aux["vote_average"].values[0].round(1)}'}

            return {'message': f'Movie `{title}` has not enough votes'}

        return {'message': f'Movie `{title}` not found'}


    def get_actor(self, actor=''):
        """Obtenemos las películas de los actores, la rentabilidad máxima y la rentabilidad media.

         Argumentos:
             actor (str, opcional): Actor a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        df_aux = self._df_movies['cast'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(actor.lower())].index.values)
        movies_count = len(index_list)
        if movies_count > 0:
            ret_mean = 0
            for index in index_list:
                ret_mean += self._df_movies.iloc[index]['return']
            if movies_count > 0:
                ret_mean = (ret_mean/movies_count).round(1)
            else:
                ret_mean = 0
            return_list = [self._df_movies['return'].iloc[ret] for ret in index_list]
            max_value = max(return_list)
            index_max_return = index_list[return_list.index(max_value)]
            return {'actor': actor,
                    'cantidad_filmaciones': f'{movies_count}',
                    'retorno_total': f'{self._df_movies.iloc[index_max_return]["return"].round(1)}',
                    'retorno_promedio': f'{ret_mean}'}

        return {'message': f'Actor `{actor}` not found'}


    def get_director(self, director=''):
        """Obtenemos todas las películas, año de estreno, rendimiento, ingresos y presupuesto del director solicitado.

         Argumentos:
             director (str, opcional): Director a buscar. El valor es ''.

         return:
             dict: Mensaje con la información solicitada.
        """
        df_aux = self._df_movies['director'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(director.lower())].index.values)
        if len(index_list)> 0:
            m_list = [self._df_movies['title'].iloc[ret] for ret in index_list]
            d_list = [self._df_movies['release_year'].iloc[ret] for ret in index_list]
            rev_list = [self._df_movies['revenue'].iloc[ret] for ret in index_list]
            c_list = [self._df_movies['budget'].iloc[ret] for ret in index_list]
            ret_list = [self._df_movies['return'].iloc[ret] for ret in index_list]
            max_value = max(ret_list)

            index_var = index_list[ret_list.index(max_value)]
            return {'director': director,
                    'retorno_total_director': f'{self._df_movies.iloc[index_var]["return"].round(1)}',
                    'peliculas': f'{m_list}',
                    'anio': f'{d_list}',
                    'retorno_pelicula': f'{ret_list}',
                    'budget_pelicula': f'{c_list}',
                    'revenue_pelicula': f'{rev_list}'}

        return {'message': f'Director `{director}` not found'}