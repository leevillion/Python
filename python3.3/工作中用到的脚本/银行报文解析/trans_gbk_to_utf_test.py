import codecs,re
from strip import Tripspace

class Trans_g_to_u(Tripspace):

    def trans_xml(self,file_path,target_file):
        'GBK格式编码转为UTF-8'
        f = codecs.open(file_path, 'rb', 'mbcs')
        text = f.read().encode('utf-8')
        text = re.sub(b'encoding="GBK"',b'encoding="UTF-8"',text)
        f.close()
        f = open(target_file, 'wb')
        f.write(text)
        f.close()

    def trans_txt(self,file_path,target_file):
        '先去除空格再将GBK格式编码转为UTF-8'
        Tripspace.main(self,file_path,target_file)
        f = codecs.open(target_file, 'rb', 'mbcs')
        text = f.read().encode('utf-8')
        text = re.sub(b'encoding="GBK"',b'encoding="UTF-8"',text)
        f.close()
        f = open(target_file, 'wb')
        f.write(text)
        f.close()



