#%%


import requests
lat=41.3153
lon=69.2892
APIkey='29c95342e9f95fc80680b48232d2c84a'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}'
response = requests.get(url)
data = response.json()
print(data['name'])
print('Description:',data['weather'][0]['description'])
print('Temperature:',f'{data['main']['temp']-273.15:.2f}','celcius')
print('Humidity:', data['main']['humidity'])
print('Pressure:',data['main']['pressure'])
print('Visibility:',data['visibility'])



#%%
import random
Api_key='2bf7722e95121a161eac0c5769d1deee'
def get_genres():
    res = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={Api_key}&language=en' )
    genres=res.json()['genres']
    return {genre['name'].lower():genre['id'] for genre in genres}
def get_movies(genreid):
    res= requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={Api_key}&with_genres{genreid}&language=en' )
    movies=res.json()['results']
    return movies

def recommend_movies():
    genres=get_genres()
    print(f"available genres:")
    for genre in genres:
        print(f" {genre.title()}")

    userinput=input("enter genre: ").strip().lower()
    genreid=genres.get(userinput)
    if not genreid:
        print("genre not found")
        return
    movies=get_movies(genreid)
    movie=random.choice(movies)
    print(f"recommended movie: {movie['title']}")
    print(f"recommended genre: {movie['overview']}")



recommend_movies()
#%%
