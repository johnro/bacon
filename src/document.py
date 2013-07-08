import settings
from os import listdir

class DocReader(object):

    def get_cache(self):
        cache = listdir(settings.DOC_PATH)
        return cache

    def read_docs(self, cache):
        docs = []

        print "Reading...%d docs.. " % len(cache)
        for c in cache:
            with open(settings.DOC_PATH + c) as f:
                d = f.read()
                docs.append(d)
        return docs
    
