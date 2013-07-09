import settings
import pcolors
from tokenizer import Tokenizer
from lexicon import Lexicon
from document import DocReader

class InvertedIndex():

    def __init__(self):
        self.invertedindex = {}
        self.lexicon = Lexicon()
        self.tokenizer = Tokenizer()
        self.doc_reader = DocReader()
        self.build_index()

    def build_index(self):
        #comments?
        cache = self.doc_reader.get_cache()
        docs = self.doc_reader.read_docs(cache)
        print "\nINVERTEDINDEX : Indexing %d documents..\n" % len(docs)
        for d in range(len(docs)):
            print "Indexing document '%s'" % (settings.PATH_DOCS + str(d))
            self.add_document(docs[d], d)

        print "Indexed total %d unique terms" % self.lexicon.size()

    def get_postinglist(self, lex_id):
        return self.invertedindex[lex_id]
            
    def add_document(self, doc, document_id):
        """FIXME: 
        -Needs doc 
        -Too slow?
        -Remove stop words
        -Reduce number of tokens
        """
        tokens = self.tokenizer.tokenize(doc)
        
        for t in tokens:
            lex_id = self.lexicon.lookup(t.get_value())

            if(lex_id == settings.INVALID):
                lex_id = self.lexicon.add_value(t.get_value())
                pl = PostingList()
                pl.append_posting(Posting(document_id, t.get_position()))
                self.invertedindex[lex_id] = pl
            else:
                pl = self.get_postinglist(lex_id)
    
            if pl.get_last_posting().get_document_id() != document_id:
                pl.append_posting(Posting(document_id, t.get_position()))
            else:
                p = pl.get_last_posting()
                p.append_position(t.get_position())
           
    def size(self):
        return len(self.invertedindex)

    def debugprint(self):
        voc = self.lexicon.get_vocabulary()
        for v in voc:
            lid = self.lexicon.lookup(v)
            pl = self.get_postinglist(lid)
            print "[%s]" % v
            pl.info()
    
class PostingList(object):

    def __init__(self):
        self.postings = []

    def append_posting(self, posting):
        if self.size() == 0:
            self.postings.append(posting)
        elif self.get_last_posting().get_document_id() >= posting.get_document_id():
            #raise execption if list isnt kept sorted
            raise ValueError()
        else:
            self.postings.append(posting)
        
    def get_last_posting(self):
        return self.postings[self.size() -1]
    
    def get_posting(self, i):
        return self.postings[i]

    def get_first_posting(self):
        return self.postings[0]

    def size(self):
        return len(self.postings)

    def debugprint(self):
        for p in self.postings:
            print "{%d}" % self.size()
            p.debugprint()

    def info(self):
        print "pl len = %d " % self.size()
        total = 0
        for p in self.postings:
            p.debugprint()
            total += p.get_occurance_count()
        print "total : ", total
        
    
class Posting(object):
    
    def __init__(self, document_id, position):
        self.positions = [] 
        self.document_id = document_id
        self.append_position(position)

    def __repr__(self):
        return self.document_id
    
    def append_position(self, position):
        #FIXME: this is a workaround, real problem
        #is in add_document(), append position is called two times
        if position not in self.positions:
            self.positions.append(position)

    def get_occurance_count(self):
        return len(self.positions)
    
    def get_document_id(self):
        return self.document_id

    def debugprint(self):
        print self.positions
