class Movie:
    def __init__(self, title, director, release_year):  # Corrected the constructor
        self.title = title
        self.director = director
        self.release_year = release_year

    def get_movie_details(self):
        return f"Title: {self.title}, Director: {self.director}, Release Year: {self.release_year}"

# Example usage
movie = Movie("Inception", "Christopher Nolan", 2010)
print(movie.get_movie_details())
