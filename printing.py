import pprint
import reports

def count_games_print(file_name):

    pp = pprint.PrettyPrinter()
    pp.pprint(reports.count_games(file_name))
    return reports.count_games(file_name)

def decide_print(file_name, year):

    pp = pprint.PrettyPrinter()
    pp.pprint(reports.decide(file_name, year))
    return reports.decide(file_name, year)

def get_latest_print(file_name):

    pp = pprint.PrettyPrinter()
    pp.pprint(reports.get_latest(file_name))
    return reports.get_latest(file_name)

def count_by_genre_print(file_name, genre):

    pp = pprint.PrettyPrinter()
    pp.pprint(reports.count_by_genre(file_name, genre))
    return reports.count_by_genre(file_name, genre)

def get_line_number_by_title_print(file_name, title):

    pp = pprint.PrettyPrinter()
    pp.pprint(reports.get_line_number_by_title(file_name, title))
    return reports.get_line_number_by_title(file_name, title)

def main():
    name_of_the_file = "game_stat.txt"
    year = 2000
    genre = "RPG"
    title = "Half-Life"

    count_games_print(name_of_the_file)
    decide_print(name_of_the_file, year)
    get_latest_print(name_of_the_file)
    count_by_genre_print(name_of_the_file, genre)
    get_line_number_by_title_print(name_of_the_file, title)

# last commit
