import sys,re
from handler import *
from rules import *
from splitblock import *

class Parser:
    def __init__(self,handler):
        self.handler=handler
        self.rules=[]
        self.filters=[]
    def addrules(self,rule):
        self.rules.append(rule)
    def addfilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    def parse(self,file):
        for block in getblock(file):
            for filter in self.filters:
                block=filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last=rule.action(block,self.handler)
                    if last:
                        break
class BasicTP(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addrules(TitleRule())
        self.addrules(HeadRule())
        self.addrules(ListitemRule())
        self.addrules(ListRule())
        self.addrules(ParagraphRule())

        self.addfilter(r'\*(.+?)\*','em')
        self.addfilter(r'(www\.[a-zA-z/]+\.com)','url')

handler=HtmlPrinciple()
parser=BasicTP(handler)

parser.parse(sys.stdin)
