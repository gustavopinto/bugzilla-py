Bugzilla-py
===========

This is an experimental library used to crawl meta-data information of bugs at [Bugzilla](http://bugzilla.mozilla.org/).

Usage
-----

If you want to crawl a sigle bug report, use

```
python bugzilla.py -b <bug-id>
```

Or, if you have a list of bugs reports, you might want to use

```
python bugzilla.py -l <file>
```

The results are saved in a csv file named ``output.csv`` in the root dir.

Use --help to see all options.

Requirements
------------

* python 2.7 or above
* BeautifulSoup
* urllib2
