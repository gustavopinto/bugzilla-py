"""Salving the results in a csv file."""


columns = ["status",
          "reported",
          "modified",
          "component",
          "version",
          "platform",
          "importance",
          "flags",
          "cc_list",
          "comments",
          "url",
          "category",
          "reporter",
          "depends",
          "blocks",
          "attempts",
          "loc_per_attempt",
          "reopened"]


def report(bugs):
  """ Write to a csv file """

  with open("output.csv", 'w') as output:
    output.write(",".join(columns) + "\n")
    for bug in bugs:
      output.write(str(bug) + "\n")
