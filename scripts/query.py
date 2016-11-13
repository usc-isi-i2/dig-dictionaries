#This script is used to get the data from ethinicity-nationality.json and query any ethinicity to return nationality.
import json

#json format
[
    {
	    "category": ["latina", "latino", "Latin America", "hispanic", "caramel"],
	    "entries": ["Spainish", "Argentinean", "Cuban", "Colombian", "Puerto Rico", "Mexican", "Dominican", "Costa Rican", "Guatemalan", "Honduras", "Nicaraguan", "Panamanian", "Salvadoran", "Bolivian", "Chilean", "Ecuadorean", "Paraguayan", "Peruvian", "Uruguayan", "Venezuelan"]
    }
]
#read the json file.
def getDataFromJson():
    with open('ethinicity-nationality.json') as data_file:
        data = json.load(data_file)
    return data

#given a query as ethinicity like Arab the function return a unnique set of all the nationality.
#if query is in multiple categories then the result will be aggregation of all the entries.

def getNatFomEthnicity(ethinicity, data):
    _set = set()
    for ele in data:
        if ethinicity in ele["category"]:
            for nats in ele["entries"]:
                _set.add(nats.encode("utf8"))
    return _set

if __name__ == "__main__":
    data = getDataFromJson()
    nationality = getNatFomEthnicity('Arabs', data)
    print nationality
