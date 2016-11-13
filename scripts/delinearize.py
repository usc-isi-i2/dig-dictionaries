# This script is used to delinearize the json file. Input is a json file and output is the unique set.
import json

#this function gets all the word from the json file and returns a set.
def getWordList():
    with open('ethinicity-nationality.json') as data_file:
        data = json.load(data_file)

    _set  = set()
    for ele in data:
        for cat,ent in ele.iteritems():
            for nat in ent:
                _set.add(nat.encode("utf8").strip())
    return _set

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
    #unique words
    print getWordList()