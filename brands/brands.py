# -*- coding: utf-8 -*-
class Brand():

    count = 1

    def __init__(self,name):
        self.name = name
        self.id = Brand.count
        Brand.count += 1
