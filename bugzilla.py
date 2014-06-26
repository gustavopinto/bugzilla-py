import crawler
import argparse
from reporting import report

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
    output = []
    try:
      for bug in bugs:
        result = crawler.download(bug)
        output.append(result)
        report(output)
    except KeyboardInterrupt:
      print "\nInterupted!"
    except crawler.BugNotFound, e:
      print "\nAn error occurred while crawling bug: " + bug
      print e.message
    except:
      print "\nAn error occurred while crawling bug: " + bug
      raise


if __name__ == "__main__":
  main()
