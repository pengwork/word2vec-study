# -*- coding: utf-8 -*-
import os
import re
import codecs
 
def replace_func(input_file):
    p1 = re.compile(r'-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    p2 = re.compile(r'[（][，；。？！\s]∗[）][，；。？！\s]∗[）]')
    p3 = re.compile(r'[「『]')
    p4 = re.compile(r'[」』]')
    outfile = codecs.open(input_file + "_updated.txt", 'w', 'utf-8')
    with codecs.open(input_file, 'rw', encoding='utf-8') as myfile:
        for line in myfile:
            line = p1.sub(r'\2', line)
            line = p2.sub(r'', line)
            line = p3.sub(r'“', line)
            line = p4.sub(r'”', line)
            outfile.write(line)
    outfile.close()
 
 
def run():
    data_path = 'E:\\Wiki\\wiki\\extracted1\\AA\\'
    data_names = ['a.txt']
    for data_name in data_names:
        replace_func(data_path + data_name)
        print('{0} has been processed !'.format(data_name))
 
 
if __name__ == '__main__':
    run()

