# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:51:36 2020

@author: Gerard
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:36:16 2020

@author: Gerard
"""


import unittest

import climbers


class TestClimbers(unittest.TestCase):

    def test_get_page_content(self):
       self.assertTrue(len(climbers.get_page_content()) >0)

    def test_create_soup(self):
        self.assertTrue(climbers.create_soup(climbers.get_page_content())) is not None
     
        
if __name__ == '__main__':
    unittest.main()
    
    
   