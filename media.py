import webbrowser

class Movie():
    """ Movie class has 2 methods:
     - The __init__ method: When Movie() its called an instance of the class is created
     and passes it as the first parameter to the __init__ method. Then, four properties are created with
     its title storyline, poster and youtube trailer.

     - The show_trailer method opens browser to watch movie trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
