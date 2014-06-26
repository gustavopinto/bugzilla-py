Bugzilla-py
===========

This is an experimental library used to crawl meta-data information of bugs at [Bugzilla](http://bugzilla.mozilla.org/).

Usage
-----

If you want to crawl a particular bug, use

```python bugzilla.py <bug-id>```

Or, if you have a list of bugs that you want to crawl, use

```python bugzilla.py -l <file>```

The results are exported as a csv file named ``output.csv``.

Use --help to see all options.

Requirements
------------

* python 2.7 or above
* BeautifulSoup
* urllib2
