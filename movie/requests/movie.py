import requests

def get_movie_by_title(apikey='', tTitleMovie=''):
    r = requests.get(f'http://www.omdbapi.com/?apikey={apikey}&t={tTitleMovie}')
    return r

def get_movie_by_id(apikey='', idMovie=''):
    r = requests.get(f'http://www.omdbapi.com/?apikey={apikey}&i={idMovie}')
    return r

def get_movie_by_title_with_filter(apikey='6e6d5fd6', tTitleMovie='', typeMovie=None, year=None):
    r = requests.get(f'http://www.omdbapi.com/?apikey={apikey}&t={tTitleMovie}&type={typeMovie}&y={year}')
    return r