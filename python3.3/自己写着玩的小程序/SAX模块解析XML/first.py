from xml.sax import ContentHandler
from xml.sax import parse
import os

class Dispath:
    def dis(self,pre,name,attrs=None):
        tname=pre+name.capitalize()
        dname='default'+name.capitalize()
        method=getattr(self,tname,None)
        if callable(method):
            a=[]
        else:
            method=getattr(self,dname,None)
            a=[]
            a.append(name)
        if pre=='start':
            a.append(attrs)

        if callable(method):
            method(*a)
    def startElement(self,name,attrs):
        self.dis('start',name,attrs)
    def endElement(self,name):
        self.dis('end',name)

class XML_to_Html(Dispath,ContentHandler):
    isinside=False
    def __init__(self,path):
        self.path=[path]
        self.isdirectory()

    def isdirectory(self):
        path=os.path.join(*self.path)
        if not os.path.isdir(path):
            os.makedirs(path)
    def characters(self,string):
        if self.isinside:
            self.out.write(string)
    def defaultStart(self,name,attrs):
        if self.isinside:
            self.out.write('<'+name)
            for key,val in attrs.items():
                self.out.write('%s=%s' % (key,val))
            self.out.write('>')
    def defaultEnd(self,name):
        if self.isinside:
            self.out.write('</%s>' % name)
    def startDirectory(self,attrs):
        self.path.append(attrs['name'])
        self.isdirectory()
    def endDirectory(self):
        self.path.pop()
    def startPage(self,attrs):
        filename=os.path.join(*self.path+[attrs['name']+'.html'])
        self.out=open(filename,'w')
        self.writeHeader(attrs['title'])
        self.isinside=True
    def endPage(self):
        self.isinside=False
        self.writeFooter()
        self.out.close()
    def writeHeader(self,title):
        self.out.write('</html>\n <head>\n   <title>')
        self.out.write(title)
        self.out.write('</title>\n </head>\n  <body>')
    def writeFooter(self):
        self.out.write('\n </body>\n</html>')
parse('website.xml',XML_to_Html('link'))


