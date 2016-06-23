# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:58:07 2016

@author: Leaf
"""

import xml.etree.cElementTree as ET
from collections import defaultdict

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    if element.tag in ["node", "way", "relation"]:
        return element.attrib["uid"]
    else:
        return None

def get_all_users(filename):
    users = defaultdict(int)
    for _, element in ET.iterparse(filename):
        uid = get_user(element)
        if(uid):
            users[uid] += 1
    return users
    
    
    
    