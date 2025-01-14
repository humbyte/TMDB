import tmdbsimple as tmdb

# Configura tu clave de API de TMDb
tmdb.API_KEY = 'ce870475b3eaab2e657e0ed0eae9d086'

def obtener_detalles_serie(nombre_serie):
    # Buscar la serie por nombre
    search = tmdb.Search()
    response = search.tv(query=nombre_serie, language='es-CL')

    if not response['results']:
        return None, None, None

    # Obtener el ID de la primera serie encontrada
    serie_id = response['results'][0]['id']
    poster_path = response['results'][0]['poster_path']
    puntuacion = response['results'][0]['vote_average']
    descripcion = response['results'][0]['overview']

    # Obtener los proveedores de visualización para la serie
    tv = tmdb.TV(serie_id)
    providers_response = tv.watch_providers()

    if providers_response and 'results' in providers_response and 'CL' in providers_response['results']:
        watch_providers = providers_response['results']['CL']['flatrate']
    else:
        watch_providers = None

    # Construir la URL del póster
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

    return watch_providers, poster_url, puntuacion, descripcion

# Ejemplo de uso
nombre_serie = input("Por favor, ingresa una serie: ")
watch_providers, poster_url, puntuacion, descripcion = obtener_detalles_serie(nombre_serie)

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