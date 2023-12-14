# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    combined_data = {}
    with open(filename) as stations:
        index = 0
        for station in stations:
            if index:
                station = station.replace("\n", "")
                parts = station.split(";")
                combined_data[parts[3]] = (float(parts[0]), float(parts[1]))
            index += 1
    return combined_data

def distance(stations: dict, station1: str, station2: str):
    x_km = (float(stations[station1][0]) - float(stations[station2][0])) * 55.26
    y_km = (float(stations[station1][1]) - float(stations[station2][1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return float(distance_km)

def greatest_distance(stations: dict):
    station_names = list(stations.keys())
    max_distance = 0
    station_pair = ()
    
    for i in range(len(station_names)):
        for j in range(i+1, len(station_names)):
            station1 = station_names[i]
            station2 = station_names[j]
            curr_distance = distance(stations, station1, station2)

            if curr_distance > max_distance:
                max_distance = curr_distance
                station_pair = (station1, station2)

    return (station_pair[0], station_pair[1], max_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)