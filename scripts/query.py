import json
import codecs

# given a query as ethinicity like Arab the function return a unnique set of all the nationality.
# if query is in multiple categories then the result will be aggregation of all the entries.


class Q(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_entries_from_category(self, ethinicity):
        _set = set()
        for ele in self.dictionary:
            if ethinicity.upper() in [ e.upper() for e in ele["category"]]:
                for nats in ele["entries"]:
                    _set.add(nats.encode("utf8"))
        return list(_set)

if __name__ == "__main__":
    dictionary = json.load(codecs.open('../ethnicities/ethnicity-nationality.json', 'r', 'utf-8'))
    q = Q(dictionary)
    print q.get_entries_from_category('arabs')
