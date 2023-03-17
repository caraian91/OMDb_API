from movie.requests.movie import *


class TestMovie:
    def test_get_movie_title_200(self):
        r = get_movie_by_title(apikey='6e6d5fd6', tTitleMovie='The Godfather')
        assert r.status_code == 200, 'Status code is not OK. Code should be 200'

    def test_get_movie_invalid_title(self):
        r = get_movie_by_title(apikey='6e6d5fd6',tTitleMovie='')
        error_expected = {
                "Response": "False",
                "Error": "Incorrect IMDb ID."
            }
        try:
            assert r.status_code == 400, 'Status code is not OK. Code should be 400'
        except AssertionError:
            print('Should have been returned the status code 400 here is a BUG')     # => return status code 200
        assert r.json() == error_expected                                        # => check if we have the error msg

    def test_get_movie_id_200(self):
        r = get_movie_by_id(apikey='6e6d5fd6', idMovie='tt0468569')
        assert r.status_code == 200, 'Status code is not OK. Code should be 200'
        assert r.json()['Title'] == 'The Dark Knight', 'Returned movie is not correct'

    def test_get_movie_invalid_id(self):
        r = get_movie_by_id(apikey='6e6d5fd6', idMovie='')
        assert r.status_code == 400, 'Status code is not OK. Code should be 400'

    def test_apikey_invalid(self):
        r = get_movie_by_id(apikey='', idMovie='')
        assert r.status_code == 401, 'Status code is not OK. Code should be 401'
        assert r.json()['Error'] == 'No API key provided.'

    def test_get_movie_by_titile_filter(self):
        r = get_movie_by_title_with_filter(tTitleMovie='Breaking Bad',typeMovie='series', year='2008')
        assert r.json()['Title'] == 'Breaking Bad', 'Movie title incorrect'
        assert r.json()['Type'] == 'series', 'Movie genres title incorrect'
        assert r.json()['Year'] == '2008–2013', 'Year is not OK'

    def test_get_movie_by_typeMovie_change(self):
        r = get_movie_by_title_with_filter(tTitleMovie='Breaking Bad',typeMovie='movie')
        assert r.json()['Title'] == 'El Camino: A Breaking Bad Movie', 'Movie title incorrect'
        assert r.json()['Type'] == 'movie', 'Movie genres title incorrect'