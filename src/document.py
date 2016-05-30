import settings
from os import listdir

class DocReader(object):

    def get_cache(self):
        path = settings.PATH_DOCS
        cache = listdir(path)
        return cache

    def read_docs(self, cache):
        docs = []
        path = settings.PATH_DOCS

        print "\nDOCUMENT READER : Reading...%d docs..\n" % len(cache)
        for c in cache:
            print "Reading  %s\t[%s]" % (c, "OK")
            f = open(path + c)
            d = f.read()
            docs.append(d)
            f.close()
        return docs
    
