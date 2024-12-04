import unittest

def urlify(url, length):
    new_string = ""
    for s in url:
        if s == "":
            add_s = "%20"
        new_string = "" + add_s

class Test(unittest.testCase):
    data = ""

    def test_urlify(self):
        return True