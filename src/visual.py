import os
import sys
import json
import collections

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class ZipfLaw:

    def __init__(self, path=("essay.txt","./data/wordcount.json")):

        try :
            self.path = sys.argv[1]
        except IndexError :
            self.path = path[0]

        try :
            self.jsonPath = sys.argv[2]
        except IndexError :
            self.jsonPath = path[1]

        self.essay = open(self.path, 'r')
        self.wordCount = {}

        self.wordSplit()
        self.jsonifyDict()
        self.drawGraph()

        self.essay.close()

    def wordSplit(self):
        """ Splits the words from 'self.essay' to become a key and value
        of dictionary 'self.wordCount' with the key being the word and the value
        being the count of the word. """

        wordList = self.essay.read().split()

        for word in wordList:
            if word.isalpha():
                if word in self.wordCount:
                    self.wordCount[word.lower()] += 1
                else :
                    self.wordCount[word.lower()] = 1

    def jsonifyDict(self):
        """ Sorts and puts the content of 'self.wordCount' to './src/data/wordcount.json' """

        self.sortedWordCount = collections.OrderedDict(reversed(sorted(self.wordCount.items(), key= lambda t : t[1])))
        # Hey, I know its weird, but trust me it works...
        #print(sortedWordCount)

        with open(self.jsonPath, 'w') as jsonData:
            json.dump(self.sortedWordCount, jsonData, ensure_ascii=False)

    def drawGraph(self, graphLimit=10):
        """ Draws the graph of 'self.sortedWordCount' using matplotlib """

        x_axis = []
        y_axis = []

        for i in range(graphLimit):
            x_val = list(self.sortedWordCount.items())[i][0]
            y_val = list(self.sortedWordCount.items())[i][1]
            x_axis.append(x_val)
            y_axis.append(y_val)

        plt.scatter(x_axis, y_axis, color='r', marker='*', s=20)
        plt.xlabel("Words", fontsize=10)
        plt.ylabel("Frequency", fontsize=10)
        plt.grid(True)
        plt.title("Zipf's Law using Matplotlib")
        plt.savefig('./data/zipf_py.png')
        plt.show()
        #print(x_axis, y_axis)


if __name__ == '__main__':
    ZipfLaw()
