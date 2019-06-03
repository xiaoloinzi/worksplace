# coding=utf-8
import unittest
import os
import requests

class getIntfTest(unittest.TestCase):
    def test_getIntf_normal0(self):
        url = 'http://httpbin.org/get'
        r = requests.get(url,params={'key1': '123.0'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('123.0' in r.text)
    def test_getIntf_fault0(self):
        url = 'http://httpbin.org/get'
        r = requests.get(url,params={'key1': '456.0'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('456.0' in r.text)
