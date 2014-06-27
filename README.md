Bugzilla-py
===========

This is an experimental library used to crawl meta-data information of bugs reports at [Bugzilla](http://bugzilla.mozilla.org/).

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

Where file is a .txt file with one bug report id per line (such as [this one](energy-bugs-id.txt)). The results are saved in a csv file named ``output.csv`` in the root dir.

Use --help to see all options.


Usage: Source code
------------------

Download the source code

```
git clone git@github.com:gustavopinto/bugzilla-py.git
```

In the root dir, open a python shell and try to download a bug:

```python
>>> import crawler
>>> url = "https://bugzilla.mozilla.org/show_bug.cgi?id=738529"
>>> bug = crawler.download(url)
>>> bug.status
'RESOLVED FIXED'
>>> bug.version
'unspecified'
>>> bug.reported
'2013-05-15 01:22'
>>> bug.reporter
'"leo.bugzilla.gecko"'
>>> dir(bug)
['__doc__', '__init__', '__module__', '__str__', 'attachment', 'blocks', 'cc_list',
'comments', 'component', 'depends', 'flags', 'importance', 'modified', 'platform',
'reopened', 'reported_date', 'reporter', 'status', 'url', 'version']
```

Requirements
------------

* python 2.7 or above
* BeautifulSoup
* urllib2


License
-------

Bugzilla-py is released under GPL 2.
