import unittest

def urlify(url, length):
    new_string = []
    for i in range(length):
        if url[i] == " ":
            new_string.extend(['%', '2', '0'])
        else:
            new_string.append(url[i])
    return new_string

class Test(unittest.TestCase):
    data = [(list("Mr John Smith    "), 13, list("Mr%20John%20Smith")), 
            (list("I like juice    "), 12, list("I%20like%20juice")), 
            (list('much ado about nothing      '), 22, list('much%20ado%20about%20nothing'))]

    def test_urlify(self):
        for [test_string, length, answer] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, answer)

if __name__ == "__main__":
    unittest.main()