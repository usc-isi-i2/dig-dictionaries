import json
from optparse import OptionParser
import codecs

# given a query as ethinicity like Arab the function return a unnique set of all the nationality.
# if query is in multiple categories then the result will be aggregation of all the entries.
def getNatFomEthnicity(ethinicity, data):
    _set = set()
    for ele in data:
        if ethinicity.upper() in [ e.upper() for e in ele["category"]]:
            for nats in ele["entries"]:
                _set.add(nats.encode("utf8"))
    return _set

if __name__ == "__main__":
    parser = OptionParser()
    (c_options, args) = parser.parse_args()
    input_path = args[0]
    data = json.load(codecs.open(input_path, 'r', 'utf-8'))
    nationality = getNatFomEthnicity('arabs', data)
    print nationality
