# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from urllib import request
import time
from extract_source import ParseNavigation
import os


def request_url(add:str,patch_name:str = "", localize=False):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    req=request.Request(url=add,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    if localize:
        filename=os.getcwd()+'\\'+patch_name+'.html'
        print(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
    res.close()
    time.sleep(1)
    return html


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_list=sys.argv[1]
    list_f=open(add_list)
    p_add=list_f.readline()
    while p_add:
        cur=request_url(p_add)
        pn=ParseNavigation()
        pn.feed(cur)
        sources=pn.get_source()
        patch_name=pn.get_patch_name()
        index=0
        for source in sources:
            #  print(source)
            index=index+1
            title=patch_name+'_'+str(index)
            request_url(source,title,True)
        print('-----------------')
        p_add=list_f.readline()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
