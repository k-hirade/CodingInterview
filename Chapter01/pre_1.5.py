import unittest

def one_away(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 == len_s2:
        return replace_text(s1, s2)
    elif len_s1 + 1 == len_s2:
        return insert_text(s1, s2)
    elif len_s1 - 1 == len_s2:
        return insert_text(s2, s1)
    else:
        return False
        

def replace_text(s1, s2):
    replaced = False
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            if replaced:
                return False
            replaced = True
    return True

def insert_text(s1, s2):
    inserted = False
    i, j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if inserted:
                return False
            inserted = True
            j +=1
        else:
            i +=1
            j +=1
    return True

class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()