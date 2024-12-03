# T => 重複でない, F => 重複

import unittest

def unique(string):

    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for str in string:
        val = ord(str)
        if char_set[val]:
            return False

        char_set[val] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()