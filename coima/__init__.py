import sys
import re

class Template(object):

    def __init__(self, to_substitute, f):
        self.to_substitute = to_substitute
        self.f = f
        self.cache = []


    def file_obj(self):
        try:
            obj = open(self.f).readlines()
            return obj
        except IOError, error:
            print error
        except OSError, error:
            print error


    def line_replacement(self):
        for line in self.file_obj():
            items = [i for i in line.split()]
            for position, item in enumerate(items):
                for i, part in enumerate(re.split(r'\{\{(.*?)\}\}', item)):
                    if i % 2:
                        replace = self.to_substitute.get(part)
                        if replace:
                            items[position] = replace 
            self.cache.append(' '.join(items))


    def render(self):
        self.line_replacement()
        return '\n'.join(self.cache)
