import unittest

def string_compression(string):
    new_string = ""
    pre_s = string[0]
    count = 0

    for s in string:
        if pre_s == s:
            count += 1
        else:
            new_string = new_string + pre_s + str(count)
            count = 1
        pre_s = s
    new_string = new_string + pre_s + str(count)

    if len(new_string) > len(string):
        return string
    return new_string

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
        ('aAAABBfFFFFFFceEEEEE', 'a1A3B2f1F6c1e1E5')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()