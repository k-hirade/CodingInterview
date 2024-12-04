import unittest

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    char_counter = {}
    for s in str1:
        if s in char_counter:
            char_counter[s] += 1
        else:
            char_counter[s] = 1
    for c in str2:
        if c in char_counter:
            char_counter[c] -= 1
            if char_counter[c] < 0:
                return False
        else:
            return False
    return True
    
class Test(unittest.TestCase):
    dataT = (("bacdd", "acdbd"), ("1234", "3241"), ("i987", "78i9"))
    dataF = (("cdsav", "vfdbdrb"), ("cdsv", "vdsa"), ("poon", "235v"))

    def test_cp(self):
        for test_strings in self.dataT:
            # タプルのアンパック
            result = check_permutation(*test_strings)
            actual = self.assertTrue(result)
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            actual = self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()