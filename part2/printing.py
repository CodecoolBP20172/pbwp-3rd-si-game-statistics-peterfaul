import pprint
import reports

pp = pprint.PrettyPrinter()


def get_most_played_print(file_name):

    pp.pprint(reports.get_most_played(file_name))
    return reports.get_most_played(file_name)


def sum_sold_print(file_name):

    pp.pprint(reports.sum_sold(file_name))
    return reports.sum_sold(file_name)


def get_selling_avg_print(file_name):

    pp.pprint(reports.get_selling_avg(file_name))
    return reports.get_selling_avg(file_name)


def count_longest_title_print(file_name):

    pp.pprint(reports.count_longest_title(file_name))
    return reports.count_longest_title(file_name)


def get_date_avg_print(file_name):

    pp.pprint(reports.get_date_avg(file_name))
    return reports.get_date_avg(file_name)


def get_game_print(file_name, title):

    pp.pprint(reports.get_game(file_name, title))
    return reports.get_game(file_name, title)


def main():
    name_of_the_file = "game_stat.txt"
    title = "Half-Life 2"

    get_most_played_print(name_of_the_file)
    sum_sold_print(name_of_the_file)
    get_selling_avg_print(name_of_the_file)
    count_longest_title_print(name_of_the_file)
    get_date_avg_print(name_of_the_file)
    get_game_print(name_of_the_file)
