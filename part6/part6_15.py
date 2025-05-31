import math

def get_station_data (filename : str) -> dict :
    ret_dict = {}

    with open (filename) as file_handle :
        for line in file_handle :
            if line[0] == 'L' : continue;
            cur = line.split (";")

            ret_dict[cur[3]] = (float(cur[0]), float(cur[1]))

    return ret_dict

def distance (stations : dict, s1 : str, s2 : str) -> float :

    if s1 in stations :
        latitude1  = stations[s1][0]
        longitude1 = stations[s1][1]
    else :
        print (f"Station with name {s1} not found")
        return

    if s2 in stations :
        latitude2  = stations[s2][0]
        longitude2 = stations[s2][1]
    else :
        print (f"Station with name {s2} not found")
        return

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1  - latitude2)  * 111.2

    distance_km = math.sqrt((x_km**2) + (y_km**2))

    return distance_km  


if __name__ == "__main__" :
    filename = "station.txt"

    ret_dict = get_station_data (filename)
    print (ret_dict)
    
    d = distance (ret_dict, "Kaivopuisto", "Kapteeninpuistikko")
    print(d)

    d = distance (ret_dict, "Laivasillankatu", "Kaivopuisto")
    print(d)

    d = distance(ret_dict, "Designmuseo", "Hietalahdentori")
    print(d)

    d = distance (ret_dict, "Laivasillankatu", "Kapteeninpuistikko")
    print(d)
    