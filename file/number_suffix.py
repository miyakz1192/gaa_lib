
import glob
import os

from file_common import *

class NumberSuffixFile:
    def __init__(self, directory_path=None):
        self.directory_path = directory_path
        self.numbers = []

        self.scan()

    def scan(self):
        self.numbers = []
        for i in glob.glob(self.directory_path + "/*"):
            e = os.path.basename(i).split("_")
            if len(e) < 2:
                continue
            n = remove_file_ext(e[len(e)-1])
            self.numbers.append(int(n))

    def max(self):
        if len(self.numbers) == 0:
            return 0
        return max(self.numbers)

    def next(self):
        if self.max() == 0:
            return 0
        return self.max() + 1


