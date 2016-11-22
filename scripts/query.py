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
            if ethinicity.upper() in [e.upper() for e in ele["category"]]:
                for nats in ele["entries"]:
                    _set.add(nats.lower().encode("utf8"))
                for c in ele["category"]:
                    _set.add(c.lower().encode('utf8'))
        return list(_set)


def expand_dictionary(d):
    out = dict()
    for o in d:
        s = set()
        c = o['category']

        for cc in c:
            s.add(cc.lower())
        e = o['entries']
        for ee in e:
            s.add(ee.lower())
        for x in c:
            out[x.lower()] = ' '.join(list(s))
        for y in e:
            if y.lower() in out:
                out[y.lower()] = out[y.lower()] + ' ' + y.lower()
            else:
                out[y.lower()] = y.lower()
    return out

if __name__ == "__main__":
    # dictionary = json.load(codecs.open('../ethnicities/ethnicity-nationality.json', 'r', 'utf-8'))
    # q = Q(dictionary)
    # print q.get_entries_from_category('LATINA')




    hair_color_file = '/Users/amandeep/Github/dig-dictionaries/haircolor/haircolor-reference-customized.json'
    eye_color_file = '/Users/amandeep/Github/dig-dictionaries/eyecolor/eyecolor-reference-customized.json'
    ethnicity_file = '../ethnicities/ethnicity-nationality-reference.json'

    out_file = codecs.open('/Users/amandeep/Github/dig-dictionaries/expanded-dictionaries.json', 'w', 'utf-8')

    haircolor_d = json.load(codecs.open(hair_color_file, 'r', 'utf-8'))
    eyecolor_d = json.load(codecs.open(eye_color_file, 'r', 'utf-8'))
    ethnicity_d = json.load(codecs.open(ethnicity_file, 'r', 'utf-8'))

    result = dict()
    result['ethnicity'] = expand_dictionary(ethnicity_d)
    result['hair_color'] = expand_dictionary(haircolor_d)
    result['eye_color'] = expand_dictionary(eyecolor_d)

    out_file.write(json.dumps(result))
