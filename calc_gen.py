#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019年7月7日

@author: loryu
'''
import random
def gen():
    operator=['+','-']
    op_no=random.randint(3,5)
    op_nu=[]
    for i in range(op_no -1):
        op_nu.append(random.randint(1,99))
        op_nu.append(operator[random.randint(0,1)])
    op_nu.append(random.randint(1,99))

    i=random.randint(3,len(op_nu))
    if i%2 == 0:
        op_nu.insert(i-2,"(")
        op_nu.insert(i+2,")")
    str_calc=''
    for i in range(len(op_nu)):
        str_calc +=str(op_nu[i])
    str_calc+='='
    print(str_calc)
    
if __name__ == '__main__':
    for i in range(100):
        gen()
