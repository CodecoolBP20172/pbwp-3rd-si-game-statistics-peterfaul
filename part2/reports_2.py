def get_most_played(file_name):

    most_sold = 0

    with open(file_name) as games:
        for line in games.readlines():
            if most_sold < float(line.split("\t")[1]):
                most_sold = float(line.split("\t")[1])

    with open(file_name) as games:
        for line in games.readlines():
            if most_sold == float(line.split("\t")[1]):

                return line.split("\t")[0]


def sum_sold(file_name):

    summa = 0

    with open(file_name) as games:
        for line in games.readlines():
            summa += float(line.split("\t")[1])

    return summa


def get_selling_avg(file_name):

    summa = 0
    len_of_list = 0

    with open(file_name) as games:
        for line in games.readlines():
            summa += float(line.split("\t")[1])
            len_of_list += 1
            average = summa / len_of_list

    return average


def count_longest_title(file_name):

    longest_title = 0

    with open(file_name) as games:
        for line in games.readlines():
            if longest_title < len(line.split("\t")[0]):
                longest_title = len(line.split("\t")[0])

    return longest_title


def get_date_avg(file_name):

    summa_date = 0
    len_of_lines = 0

    with open(file_name) as games:
        for line in games.readlines():
            summa_date += float(line.split("\t")[2])
            len_of_lines += 1
            average = summa_date / len_of_lines
            average = round(average)

    return average


def get_game(file_name, title):

    props_of_games = []

    with open(file_name) as games:
        for line in games.readlines():
            if line.split("\t")[0] == title:
                props_of_games = line.split("\t")
                props_of_games[1] = float(props_of_games[1])
                props_of_games[2] = int(props_of_games[2])
                props_of_games[4] = props_of_games[4].rstrip()

    return props_of_games


# def count_grouped_by_genre(file_name):
#
#     genre_counter = 0
#     counter = 0
#     list_of_genres = []
#     genre_count = {}
#     x = 0
#
#     with open(file_name) as games:
#         result = len(games.readlines())
#
#     with open(file_name) as games:
#         for line in games:
#             list_of_genres.append(line.split("\t")[3])
#
#     while counter <= result:
#         for genre in list_of_genres:
#             counter += 1
#             if genre == list_of_genres[x]:
#                 genre_counter += 1
#
#     with open(file_name) as games:
#         for line in games:
#             genre_count.update({line.split("\t")[3] : genre_counter})
#
#     print(list_of_genres)
#     print(genre_count)
#
# count_grouped_by_genre("game_stat.txt")


def get_date_ordered(file_name):

    with open(file_name) as games:
        for line in games.readlines():






get_date_ordered("game_stat.txt")
