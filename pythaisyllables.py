# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals,print_function
from builtins import dict,str
import os,codecs
from pythainlp.tokenize import word_tokenize,dict_word_tokenize
fileDir = os.path.dirname(__file__)
filename = os.path.join(fileDir, 'data.txt')
filename2 = os.path.join(fileDir, 'word_not_syllables_cut.txt')
def get_data(file):
    with codecs.open(file, 'r',encoding='utf8') as f:
        lines = f.read().splitlines()
    f.close()
    return lines
def segment(txt):
    return dict_word_tokenize(text=txt,data=get_data(filename)+get_data(filename2),data_type="list",engine="newmm")
def segment_sentence(data):
    list1=word_tokenize(data,'newmm')
    list2=[]
    for data in list1:
        list2.extend(segment(data))
    return list2
if __name__ == "__main__":
	s = 'วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้'
	print(segment_sentence(s))