import json
from optparse import OptionParser
import codecs

#this function gets all the word from the json file and returns a set.
def getWordList(data):
    _set  = set()
    for ele in data:
        for cat,ent in ele.iteritems():
            for nat in ent:
                _set.add(nat.encode("utf8").strip())
    return list(_set)

#this function reads all the nationalities and returns a set.s
def getnatDict():
    with open('nationality.json') as data_file:
        data = json.load(data_file)
    nset = set()
    for ele in data:
        nset.add(ele.encode("utf8").strip())
    return nset

#this function returns all the value that are in set1 but not in set2.
def getminus(set1, set2):
    ans = []
    for ele in set2:
        if ele not in set1:
            ans.append(ele)
    return ans

if __name__ == "__main__":
    parser = OptionParser()
    # parser.add_option("-l", "--landmarkRules", action="store", type="string", dest="landmarkRules")
    (c_options, args) = parser.parse_args()
    input_path = args[0]
    output_path = args[1]
    input_file = json.load(codecs.open(input_path, 'r', 'utf-8'))
    word_list = getWordList(input_file)

    output_file = codecs.open(output_path, 'w', 'utf-8')
    output_file.write(json.dumps(word_list))
    output_file.close()
