import tmdbsimple as tmdb

tmdb.API_KEY = 'ce870475b3eaab2e657e0ed0eae9d086'

def obtener_trailer(movie_name):
    search = tmdb.Search()
    response = search.movie(query=movie_name)
    
    if response['results']:
        movie_id = response['results'][0]['id']
        movie = tmdb.Movies(movie_id)
        videos = movie.videos()
        
        for video in videos['results']:
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                return f"https://www.youtube.com/watch?v={video['key']}"
    
    return "No se encontró el tráiler."

# Prueba
movie_name = 'Jack Reacher'  # Nombre de la película
print(obtener_trailer(movie_name))