# -*- coding: utf-8 -*-

import urllib2

"""A simple web crawler -- don't take it serious."""


def get(url):
  """Start an HTTP request.  Return an html."""

  try:
    usock = urllib2.urlopen(url)
    return usock.read()
  except URLError, e:
    print e.code
    print e.read()
  finally:
    usock.close()
