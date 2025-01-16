import tmdbsimple as tmdb

# Configura tu clave de API de TMDb
tmdb.API_KEY = ''

def obtener_detalles_pelicula(nombre_pelicula):
    # Buscar la película por nombre
    search = tmdb.Search()
    response = search.movie(query=nombre_pelicula, language='es-CL')

    if not response['results']:
        return None, None, None, None

    # Obtener el ID de la primera película encontrada
    movie_id = response['results'][0]['id']
    poster_path = response['results'][0]['poster_path']
    puntuacion = response['results'][0]['vote_average']
    descripcion = response['results'][0]['overview']

    # Obtener los proveedores de visualización para la película
    movie = tmdb.Movies(movie_id)
    providers_response = movie.watch_providers()

    if 'results' in providers_response and 'CL' in providers_response['results']:
        watch_providers = providers_response['results']['CL']['flatrate']
    else:
        watch_providers = None

    # Construir la URL del póster
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

    return watch_providers, poster_url, puntuacion, descripcion

# Ejemplo de uso
nombre_pelicula = input("Por favor, ingresa una Pelicula: ")
watch_providers, poster_url, puntuacion, descripcion = obtener_detalles_pelicula(nombre_pelicula)

if descripcion:
    print(f"Descripcion: {descripcion}")
else:
    print("No se encontró la descripcion.")

if watch_providers:
    for provider in watch_providers:
        print(f"Proveedor: {provider['provider_name']}")
else:
    print("No se encontraron proveedores de visualización.")

if poster_url:
    print(f"URL del póster: {poster_url}")
else:
    print("No se encontró el póster.")

if puntuacion:
    print(f"Puntuación: {puntuacion}")
else:
    print("No se encontró la puntuación.")
