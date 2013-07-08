import re

class Tokenizer(object):

    def normalize(self, line):
        line = re.sub(r'[^a-zA-Z0-9\'\"]', " ", line)
        line = re.sub(r'\\s+'," ", line)
        return line.lower()

    def tokenize(self, line):
        tokens = []
        values = self.normalize(line).split()
         
        for i in range(len(values)): 
            t = Token(values[i], i, i)
            tokens.append(t)
        return tokens

    def stem(self, line):
        #TODO : Simple stemmer?
        return
        
class Token(object):

    def __init__(self, value, linenumber, position):
        self.value = value
        self.position = position
        self.linenumber = linenumber

    def get_value(self):
        return self.value
    
    def get_position(self):
        return self.position
        
    def get_linenumber(self):
        return self.linenumber

    def debugprint(self):
        print "v(%s)\tln(%d)\tpos(%d)" % (self.value, self.linenumber, self.position)

