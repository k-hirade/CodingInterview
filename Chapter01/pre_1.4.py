import unittest

def pal_perm(string):
    counter = {}
    for char in string.lower():
        if char != " ":
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
    odd_count = 0
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    
    return True

class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            print(f"tring {test_string}")
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
