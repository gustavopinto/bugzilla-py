# -*- coding: utf-8 -*-

import urllib2

"""A simple web crawler -- don't take it serious."""


def get(url):
  """Start an HTTP request.  Return an html."""

  try:
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    return data
  except urllib2.URLError, e:
    print e.code
    print e.read()
