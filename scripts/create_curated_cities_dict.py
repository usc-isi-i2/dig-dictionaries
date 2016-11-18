__author__ = 'majid'
import json
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-l", "--landmarkRules", action="store", type="string", dest="landmarkRules")
    (c_options, args) = parser.parse_args()
    all_cities_path = args[0]
    backpage_cities_path = args[1]
    stop_cities_path = args[2]
    curated_cities_path = args[3]

    all_cities = set(json.load(open(all_cities_path)))
    backpage_cities = set(json.load(open(backpage_cities_path)).keys())
    stop_cities = set(json.load(open(stop_cities_path)))

    curated_cities = all_cities - stop_cities
    # print(curated_cities)
    curated_cities.update(backpage_cities)

    curated_cities_file = open(curated_cities_path, 'w')
    curated_cities_file.write(json.dumps(list(curated_cities)))
