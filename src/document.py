import settings
import pcolors
from os import listdir

class DocReader(object):

    def get_cache(self):
        path = settings.PATH_PROJECT + settings.PATH_DOCS
        cache = listdir(path)
        return cache

    def read_docs(self, cache):
        docs = []
        path = settings.PATH_PROJECT + settings.PATH_DOCS

        print "\nDOCUMENT READER : Reading...%d docs..\n" % len(cache)
        for c in cache:
            print "Reading  %s\t[%s]" % (c, pcolors.OKGREEN+ "OK" + pcolors.ENDC)
            f = open(path + c)
            d = f.read()
            docs.append(d)
            f.close()
        return docs
    
