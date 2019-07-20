from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
import re
import pdb
import string
from unittest.mock import patch

def transList(inputstr):
    #pdb.set_trace()
    rulesdic = {key:" " for key in string.punctuation}
    rulesdic["\n"] = " "
    strTransRule = str.maketrans(rulesdic)
    tempstr = inputstr.translate(strTransRule)
    wordslist = tempstr.split(" ")
    wordslist = filter(None, wordslist)
    return list(wordslist)


resultdic = {}


def putdic(inputstr):
    wordslist = transList(inputstr)
    for word in wordslist:
        if word not in resultdic:
            resultdic[word] = 0
        resultdic[word] += 1

def sortDic(inputDic):
    return sorted(inputDic.keys())

@patch("%s.transList", returnvalue=["a"])
def test_putdic_1(self):
    putdic(None)
    self.assassertDictEqual(resultdic, {"a":1})

@patch("%s.transList", returnvalue=["a","a","c","d","d","b","c","c","b","e"])
def test_putdic_2(self):
    putdic(None)
    self.assassertDictEqual(resultdic, {"a":2,"b":2,"c":3,"d":2,"e":1})

if __name__ == "__main__":
    unittest.main()

url="http://10.X.X.X:8800"
with urlopen(url) as html:
    bsoup = BeautifulSoup(html)
    titletag = bsoup.find("title")
    print(titletag.getText())
    putdic(titletag.getText())
    ptaglist = bsoup.findAll("p")
    for ptag in ptaglist:
        print(ptag.getText())
        putdic(ptag.getText())
    print(resultdic)
    print(sort(resultdic))
