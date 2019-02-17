import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')



def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors_dict = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        csv_content = csv.DictReader(f)
        for r in csv_content:
            director = r['director_name']
            movie = r['movie_title'].replace('\xa0','')
            year = int(r['title_year'] or 0)
            score = float(r['imdb_score'])
            m = Movie(title=movie,year=year,score=score)
            directors_dict[director].append(m)
        return directors_dict


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    counter = Counter()
    scores_dict = {}
    for d,m in directors.items():
        if d:
            counter[d] += len(m)
    for d in counter :
        if counter[d]>=MIN_MOVIES:
            scores_dict[d] =  round(sum([m[2] for m in directors[d]])/counter[d],1)
    return dict(sorted(scores_dict.items(), key= lambda x: x[1],reverse=True))


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([m[2] for m in movies])/len(movies),1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
