import sys
import crawler
import argparse
from reporting import report
import time

ARGS = argparse.ArgumentParser(description="Bugzilla web crawler")

ARGS.add_argument('-b', nargs=1, help='A bug id')
ARGS.add_argument('-f', nargs=1, help='Uses a file with a list of bugs id')

def fix_url(url):
  """Prefix a schema-less URL with http://."""
  if '://' not in url:
    url = 'https://bugzilla.mozilla.org/show_bug.cgi?id=' + url
  return url.replace("\n", "")

def read(file):
  """ Read from a file. Returns a list of strings """

  try:
    f = open(file, "r")
  except IOError, e:
    print "No such file or directory: '%s'" % file
    sys.exit(0)

  lines = f.readlines()
  f.close()
  return lines


def main():
  """ Main program.

  Parse arguments, run crawler, print report
  """

  args = ARGS.parse_args()
  if not args.b and not args.f:
    print "Use --help for command line help"
    return

  if args.b:
    bugs = {fix_url(bug) for bug in args.b}
  else:
    bugs = [fix_url(bug) for bug in read(args.f[0])]

  try:
    output = []
    start_time = time.time()

    for bug in bugs:
      result = crawler.download(bug)
      output.append(result)

    total_time = round(time.time() - start_time, 2)
    print "It took %s seconds to download %s bug reports!" % (total_time, len(bugs))

    report(output)
  except KeyboardInterrupt:
    print "Interupted!"
  except crawler.BugNotFound, e:
    print "An error occurred while crawling bug: " + bug
    print e.message
  except:
    print "An error occurred while crawling bug: " + bug
    raise


if __name__ == "__main__":
  main()
