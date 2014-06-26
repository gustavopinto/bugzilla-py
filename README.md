Bugzilla-py
===========

This is an experimental library used to crawl meta-data information of bugs at [Bugzilla](http://bugzilla.mozilla.org/).

Usage: Command line
-------------------

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


Usage: Source code
------------------

Download the source code

```
git clone git@github.com:gustavopinto/bugzilla-py.git
```

In the root dir, open a python shell and download a bug:

```
>>> import crawler
>>> url = "https://bugzilla.mozilla.org/show_bug.cgi?id=738529"
>>> report = crawler.download(url)
>>> print report
RESOLVED FIXED,2012-03-22 19:24,2012-03-24 23:53,General,unspecified,All All,-- normal,,1,7,https://bugzilla.mozilla.org/show_bug.cgi?id=738529,,"&lt;away until June 29&gt; Kan-Ru Chen [:kanru]",1,0,1,60,0
>>>
```

Requirements
------------

* python 2.7 or above
* BeautifulSoup
* urllib2
