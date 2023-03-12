
import glob
import os

from file_common import *

class NumberSuffixFile:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.numbers = []

        self.scan()

    def scan(self):
        self.numbers = []
        for i in glob.glob(self.directory_path + "/*"):
            e = os.path.basename(i).split("_")
            n = remove_file_ext(e[len(e)-1])
            self.numbers.append(int(n))

    def max(self):
        return max(self.numbers)

    def next(self):
        return self.max() + 1


