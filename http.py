# -*- coding: utf-8 -*-

import urllib2

"""A simple web crawler -- don't take it serious."""


def get(url):
  """ download page source """
  usock = urllib2.urlopen(url)
  data = usock.read()
  usock.close()
  return data
