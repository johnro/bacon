import settings

class Lexicon(object):

    def __init__(self):
        self.vocabulary= {}

    def lookup(self, value):
        if self.vocabulary.has_key(value):
            return self.vocabulary[value]
        else:
            return settings.INVALID 

    def add_value(self, value):
        if self.vocabulary.has_key(value):
            return self.vocabulary[value]
        else:
            self.vocabulary[value] = self.size()
            return self.vocabulary[value]

    def get_vocabulary(self):
        return self.vocabulary.keys()

    def size(self):
        return len(self.vocabulary)
    
    def debugprint(self):
        for k in self.vocabulary:
            print k, self.vocabulary[k]
        print "\n\n"
        print self.size()

