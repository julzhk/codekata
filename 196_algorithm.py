
def reverse_digits(n):
    return int(str(n)[::-1])

def is_palindromic(n):
    return n == reverse_digits(n)

def alg_196(n):
    #
    n +=reverse_digits(n)
    for i in xrange(0, 261):
        if is_palindromic(n):
            return n
        n +=reverse_digits(n)
    else:
        return -1


import unittest
class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.expect
        Test.assert_equals = Test.expect
        Test.it= lambda x:x
        test.it= lambda x:x

        Test.expect( alg_196(59), 1111 )
        Test.expect( alg_196(23), 55 )
        Test.expect( alg_196(55), 121 )
        Test.expect( alg_196(1), 2 )
        # Test.expect( alg_196(1186060307891929990), 2 )
        self.assertNotEquals(alg_196(1186060307891929990), -1 )

Test.it("Shared examples")
numbers   = [59, 23, 55, 1]
solutions = [1111, 55, 121, 2]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing smaller numbers")
numbers   = [73, 33, 32, 260, 680, 464]
solutions = [121, 66, 55, 545, 4774, 88555588]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing bigger numbers")
numbers   = [3895, 1340, 2483, 3598, 7631, 7130, 6620, 9877]
solutions = [133697796331, 1771, 1136311, 1136311, 8998, 7447, 6886, 1771331771]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing Lychrel number candidates")
numbers   = [ 196, 879, 887, 1497, 1675, 3943, 5493, 6347, 8238, 9078, 9898 ]
for n in numbers:
    Test.expect(alg_196(n),-1)



Test.it("Shared examples")
numbers   = [59, 23, 55, 1]
solutions = [1111, 55, 121, 2]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing smaller numbers")
numbers   = [73, 33, 32, 260, 680, 464]
solutions = [121, 66, 55, 545, 4774, 88555588]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing bigger numbers")
numbers   = [3895, 1340, 2483, 3598, 7631, 7130, 6620, 9877]
solutions = [133697796331, 1771, 1136311, 1136311, 8998, 7447, 6886, 1771331771]
for n, s in zip(numbers,solutions):
    Test.expect(alg_196(n),s)

Test.it("Testing Lychrel number candidates")
numbers   = [ 196, 879, 887, 1497, 1675, 3943, 5493, 6347, 8238, 9078, 9898 ]
for n in numbers:
    Test.expect(alg_196(n),-1)


def reverse_digits(n):
    return int(str(n)[::-1])

def is_palindromic(n):
    return n == reverse_digits(n)

def alg_196(n):
    n +=reverse_digits(n)
    for i in xrange(0, 261):
        if is_palindromic(n):
            return n
        n +=reverse_digits(n)
    else:
        return -1

