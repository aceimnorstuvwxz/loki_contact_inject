#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

selected = []

with open('manual_data.txt', 'r') as fpin:
    for line in fpin.readlines():
        line = line.decode('utf-8')
        print line
        ww = line.split('	')
        print ww, len(ww), len(ww[1])
        if len(ww) > 1 and len(ww[0])> 10:
            selected.append(dict(name=ww[1][:-1],phone=ww[0]))
    

    ret = dict(data=selected)

    with open("manual_data.json",'w') as fpout:
        json.dump(ret, fpout)         
        

