class Handler:
    def callback(self,pre,name,*arg):
        method=getattr(self,pre+name,None) #method=pre+name=start_title,鏄竴涓嚱鏁板悕
        if callable(method):
            return method(*arg)
    def start(self,name):
        self.callback('start_',name)
    def end(self,name):
        self.callback('end_',name)
    def sub(self,name):
        def subtitution(match):
            result=self.callback('sub_',name,match)
            if result is None:
                result=match.group(0)
            return result
        return subtitution

class HtmlPrinciple(Handler):
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def start_head(self):
        print('<h2>')
    def end_head(self):
        print('</h2>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1),match.group(1))
    def sub_em(self,match):
        return '<em>%s</em>' % match.group(1)
    def feed(self,data):
        print(data)
