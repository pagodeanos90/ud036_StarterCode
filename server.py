import media
import fresh_tomatoes

MOVIES_LIST_PATH = "movies.txt"
MOVIE_ATTRIBUTES_SEPARATOR = "|"


def parse_input_file(f_in, delimiter=MOVIE_ATTRIBUTES_SEPARATOR):
    """Input file parsing
    This function parses the file containing the movies information,
    with each line containing the information for a single movie,
    separated by 'delimiter'
    Arguments:
        f_in(file): The input file.
        delimiter(str): The string that is between the attributes
            for a single movie.    
    Returns:
        [movie.Movies]: an array with the movie objects described in f_in
    """
    movies = []
    for line in f_in:
        try:
            m_title, m_poster_url, m_trailer_url = line.split(delimiter)
        except ValueError:
            raise ValueError("Invalid input line: {}".format(line))
        movies.append(media.Movie(m_title, m_poster_url, m_trailer_url))
    return movies

def run(movies_list_path):
    movies = parse_input_file(open(movies_list_path))
    fresh_tomatoes.open_movies_page(movies)

if __name__=='__main__':
    run(MOVIES_LIST_PATH)
