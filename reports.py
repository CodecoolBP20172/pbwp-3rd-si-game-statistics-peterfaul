def count_games(file_name):

    with open(file_name) as file:
        result = len(file.readlines())
    return result


def decide(file_name, year):

    file = open(file_name)
    year = str(year)
    file_tuple = tuple(file.read().split())
    file.close()

    if year not in file_tuple:
        return False
    else:
        return True


def get_latest(file_name):

    file = file_name
    title_and_year = {}

    with open(file) as var:
        for line in var:
            title_and_year.update({line.split("\t")[0] : line.split("\t")[2]})

    return max(title_and_year, key=title_and_year.get)


def count_by_genre(file_name, genre):

    file = file_name
    list_of_genres = []

    with open(file) as var:
        for line in var:
            list_of_genres.append(line.split("\t")[3])

    genre_counter = 0
    for i in list_of_genres:
        if i == genre:
            genre_counter += 1

    return genre_counter


def get_line_number_by_title(file_name, title):

    file = file_name
    with open(file) as var:
        try:
            for number, line in enumerate(var, 1):
                if title == line.split("\t")[0]:
                    return number
            if title not in file:
                raise ValueError("%s is not on the list." %title)
        except ValueError as err:
            print("FAILURE! %s" % err)
