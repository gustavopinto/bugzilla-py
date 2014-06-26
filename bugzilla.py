# -*- coding: utf-8 -*-

import codecs
import re, os
import sys
from bs4 import BeautifulSoup

import http

class Bug:
  def __init__(self, id, status, reported_date, modified, component, version, platform, importance, flags, cc_list, comments, reporter, depends, blocks, attachment, reopened):
    self.id = id
    self.status = " ".join(status.split())
    self.reported_date = " ".join(reported_date.split())
    self.modified = " ".join(modified.split())
    self.component = " ".join(component.split())
    self.version = " ".join(version.split())
    self.platform = " ".join(platform.split())
    self.importance = " ".join(importance.split())
    self.flags = " ".join(flags.split())
    self.cc_list = " ".join(cc_list.split())
    self.comments = comments
    self.reporter = reporter
    self.depends = " ".join(depends.split())
    self.blocks = blocks
    self.attachment = attachment
    self.reopened = reopened

  def __str__(self):
    return self.id + "," + self.status + "," + self.reported_date  + "," + self.modified + "," + self.component + "," + self.version + "," + self.platform + "," + self.importance + "," + self.flags + "," + self.cc_list + "," + str(self.comments) +"," + "https://bugzilla.mozilla.org/show_bug.cgi?id=" + self.id + "," + "," + self.reporter + "," + to_bin(self.depends) + "," + to_bin(self.blocks) + "," + self.attachment.attempts + "," + self.reopened

class Attachment:

  def __init__(self, attempts, locs_per_attempt):
    self.attempts = str(attempts)
    self.locs_per_attempt = locs_per_attempt

  def size(self):
    return self.locs_per_attempt

class Comment:
  def __init__(self, comment):
    self.comment = comment

  def __str__(self):
    return " ".join(self.comment.split()).split("#c")[1].replace("\"","")


def download_bug(bug_id):
  url = 'https://bugzilla.mozilla.org/show_bug.cgi?id=' + str(bug_id)

  data = http.get(url)

  status = get_element(data, "id=\"static_bug_status\">", "<")
  reported = get_element(data, "Reported:", "P")
  modified = get_element(data, "Modified:", "P")
  importance = get_element(data, "mportance</a></label>:", "<script")
  component = get_element(data, "id=\"field_container_component\" >", "(")
  version = get_element(data, "Version</label>:", "</td>")
  platform = get_element(data, "Platform</label>:", "</td>")
  flags = get_element(data, "class=\"tracking_flags\">", "</table>")
  cc_list = get_element(data, "CC List:", "user")
  comments = Comment(get_element(data, "last_comment_link\">", "accesskey"))
  depends = get_element(data, "dependson_input_area\">", "</td>")
  blocks = get_element(data, "blocked_input_area\">", "</td>")
  reporter = get_element(data, "by <span class=\"vcard\">", "</span")

  attachment = get_attachments(data)
  reopened = get_reopened(bug_id)

  return Bug(bug_id, remove_html(status), remove_html(reported), remove_html(modified), remove_html(component), remove_html(version), remove_html(platform), remove_html(importance), remove_html(flags), remove_html(cc_list), comments, remove_html(reporter), depends, remove_html(blocks), attachment, reopened)

def get_element(data, start, stop):
  begin = data.find(start) + len(start)
  partial = data[begin:]
  end = partial.find(stop)
  return partial[:end]

def get_attachments(data):
  attach_table = get_element(data, "id=\"attachment_table\"", "</table>")
  attempts = attach_table.count("class=\"bz_contenttype_text_plain bz_patch\"")

  loc_per_attempt = []

  return Attachment(attempts, loc_per_attempt)

def get_reopened(bug_id):
  url = "https://bugzilla.mozilla.org/show_activity.cgi?id=" + bug_id
  data = http.get(url)

  soup = BeautifulSoup(data)
  table = soup.find("table", cellpadding="4")
  rows = table.findChildren('tr')

  last_cells = []

  for row in rows:
    cells = row.findChildren('td')
    if len(cells) > 0:
      item = remove_html(cells[-1]).replace("\n", "").strip()
      last_cells.append(item)

  return str(last_cells.count("REOPENED"))

def remove_html(e):
  p = re.compile(r'<.*?>')
  return p.sub('', str(e))

def read(file):
  path = os.getcwd()
  f = open(path + file, "r")
  lines = f.readlines()
  f.close()
  return lines


def to_bin(e):
  e = e.replace("\"","").replace("</span>", "").strip()
  return "0" if e == "" else "1"

bugs = read("/energy-bugs-ids.txt")

def main():
  print "id,status,reported,modified,component,version,platform,importance,flags,cc_list,comments,url,category,reporter,depends,blocks,attempts,reopened"
  try:
    for bug in bugs:
      print download_bug(bug.replace("\n",""))
  except:
    raise
    print "opss"

def sample():
  #907155 738529
  print "running sample"
  print download_bug("966841")

if __name__ == '__main__':
  #main()
  sample()
