import pandas

def get_locations():
    data_voc = {}

    data = pandas.read_csv("locations.csv", error_bad_lines=False)
    movies = data['movie']
    years = data['year']
    infos = data['add_info']
    locations = data['location']

    for m, y, i, l in zip(movies, years, infos, locations):
        if l in data_voc:
            data_voc[l][m] = [years, infos]

        else:
            data_voc[l] = {m: [years, infos]}

    return data_voc