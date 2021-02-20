import pynlpir  # 引入依赖包
pynlpir.open()  # 打开分词器
from ctypes import c_char_p 



pynlpir.nlpir.ImportUserDict(b"userdict.txt")
#print(c)
s = '保时捷比保时泰好'  # 实验文本
# pynlpir.nlpir.AddUserWord(c_char_p("保时捷".encode()))
# pynlpir.nlpir.AddUserWord(c_char_p("保时泰".encode()))
segments = pynlpir.segment(s, pos_names=None)

for segment in segments:
	print (segment[0], '\t', segment[1])