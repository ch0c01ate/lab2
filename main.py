from location_getter import get_location
from location_parser import parse_locations
import folium


def valid(number):
    try:
        number = int(number)
        if 0 < number < 1001:
            return True
    except:
        return False

    return False


def slice_dict(d, number):
    ks = list(d.keys())
    return {ks[i]: d[ks[i]] for i in range(number)}


def main():
    number_of_locatons = input("Enter number of locations to be mapped: ")

    if valid(number_of_locatons):
        data = parse_locations()
        data = slice_dict(data, int(number_of_locatons))

        map = folium.Map(location=[48.314775, 25.082925],
                         zoom_start=10)
        fg = folium.FeatureGroup(name="Movie-map")

        for location in data.keys():
            lat, lon = get_location(location)
            description = ""

            movie = list(data[location])[0]
            description += str(movie) + "," + str(data[location][movie][0])
            if not str(data[location][movie][0]) == "NO DATA":
                description += "," + str(data[location][movie][0])
            description += "\n"

            fg.add_child(folium.CircleMarker(location=[lat, lon],
                                             radius=10,
                                             popup=description,
                                             color='green',
                                             fill_opacity=0.5))
        map.add_child(fg)
        map.save("Map_result.html")

    else:
        print("Number is not valid")
        main()


if __name__ == "__main__":
    main()
