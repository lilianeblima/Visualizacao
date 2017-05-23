#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:27:53 2017

@author: santos
"""
#%%
file = open('/home/santos/Documents/palavras.csv','r')
lista = []
for line in file:
    info = line.replace('\n','').split(',')
    dic = {}
    dic["text"] = info[0]
    dic["size"] = info[1]
    lista.append(dic)
    