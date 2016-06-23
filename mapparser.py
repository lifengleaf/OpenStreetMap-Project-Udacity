# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:48:12 2016

@author: Leaf
"""

"""
Your task is to use the iterative parsing to process the map file and find out not only what tags are there, but also how many, to get the feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the tag name as the key and number of times this tag can be encountered in the map as value.
"""
import xml.etree.cElementTree as ET
from collections import defaultdict

# return a dictionary of top level tags and their counts
def count_tags(filename):
        tags_dict = defaultdict(int)
        
        # iteratively parse the file
        for event, elem in ET.iterparse(filename):
            tags_dict[elem.tag] += 1
        return tags_dict

