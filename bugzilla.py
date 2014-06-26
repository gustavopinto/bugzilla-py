import crawler
import argparse

ARGS = argparse.ArgumentParser(description="Bugzilla web crawler")
ARGS.add_argument(
    'bugid', nargs='*',
    default=[], help='A bug id (may be repeated)')


def fix_url(url):
  """Prefix a schema-less URL with http://."""
  if '://' not in url:
    url = 'https://bugzilla.mozilla.org/show_bug.cgi?id=' + url
  return url

def read(file):
  """ Read from a file. Returns a list of strings """

  path = os.getcwd()
  f = open(path + file, "r")
  lines = f.readlines()
  f.close()
  return lines


def main():
  """ Main program.

  Parse arguments, run crawler, print report
  """

  args = ARGS.parse_args()
  if not args.bugid:# or not args.list:
    print "Use --help for command line help"
    return

  if args.bugid:
    bugs = {fix_url(bug) for bug in args.bugid}
    for bug in bugs:
      crawler.download(bug)


if __name__ == "__main__":
  main()

"""
def main():
  bugs = read("/energy-bugs-ids.txt")
  print "id,status,reported,modified,component,version,platform,importance,flags,cc_list,comments,url,category,reporter,depends,blocks,attempts,loc_per_attempt,reopened"
  try:
    for bug in bugs:
      print download_bug(bug.replace("\n",""))
  except:
    print "\nAn error occurred while crawling bug: " + bug


def sample():
  #907155 738529
  print "running sample"
  print download_bug("995886")

if __name__ == '__main__':
  main()
  #sample()
"""
