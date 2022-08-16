from functionsToTest import exponent, multiplication, addition, subtraction, squareRoot
import unittest


class exponentUnitTest(unittest.TestCase):
    def testOne(self):
        assert exponent(2, 3) == 8, "Cannot take exponent of positive numbers"

    def testTwo(self):
        assert exponent(-2, -3) ==  -0.125, "Can't have negative exponent of a negative value"

    def testThree(self):
        assert exponent(-2, 3) ==  -8, "Can't take exponent of a negative number"
        
    def testFour(self):
        assert exponent(0, 3) ==  0, "Can't take exponent of a 0"

    def testFive(self):
        assert exponent(3, 0) ==  1, "Can't take 0 as an exponent"

    def testSix(self):
        assert exponent(2, -3) == 0.125, "Can't take a negative number as an exponent for a positive number"


class multiplicationUnitTest(unittest.TestCase):
    def testOne(self):
            assert multiplication(1, 2) == 2, "Can't multiply positive numbers"

    def testTwo(self):
            assert multiplication(-2, -3) == 6, "Can't multiply negative numbers"

    def testThree(self):
            assert multiplication(-4, 5) == -20, "Can't multiply positive and negative numbers"

    def testFour(self):
            assert multiplication(0, 8) == 0, "Can't multiply with a 0"


class additionUnitTest(unittest.TestCase):
    def testOne(self):
            assert addition(1, 2) == 3, "Can't add positive numbers"

    def testTwo(self):
            assert addition(-2, -3) == -5, "Can't add negative numbers"

    def testThree(self):
            assert addition(-4, 5) == 1, "Can't add negative and positive numbers"
    
    def testFour(self):
            assert addition(0, 8) == 8, "Can't add to 0"


class subtractionUnitTest(unittest.TestCase):
    def testOne(self):
            assert subtraction(1, 2) == -1, "Can't subtract positive numbers"

    def testTwo(self):
            assert subtraction(-3, -4) == 1, "Can't subtract negative numbers"

    def testThree(self):
            assert subtraction(-5, 6) == -11, "Can't subtract positive from a negative number"

    def testFour(self):
            assert subtraction(5, -6) == 11, "Can't subtract negative number from a positive number"

    def testFive(self):
            assert subtraction(0, 6) == -6, "Can't subtract any number from 0"

    def testSix(self):
            assert subtraction(6, 0) == 6, "Can't subtract 0 from anything"


class squareRootUnitTest(unittest.TestCase):
    def testOne(self):
            assert squareRoot(4) == 2.0, "Can't find square root of a positive number"

    def testTwo(self):
            assert squareRoot(-8) == (1.7319121124709868e-16+2.8284271247461903j), "Can't find square root of a negative number"

    def testThree(self):
            assert squareRoot(0) == 0.0, "Can't find square root of zero"



def exponentSuite():
        suite = unittest.TestSuite()
        suite.addTest(exponentUnitTest('testOne'))
        suite.addTest(exponentUnitTest('testTwo'))
        suite.addTest(exponentUnitTest('testThree'))
        suite.addTest(exponentUnitTest('testFour'))
        suite.addTest(exponentUnitTest('testFive'))
        suite.addTest(exponentUnitTest('testSix'))
        return suite

def multiplicationSuite():
        suite = unittest.TestSuite()
        suite.addTest(multiplicationUnitTest('testOne'))
        suite.addTest(multiplicationUnitTest('testTwo'))
        suite.addTest(multiplicationUnitTest('testThree'))
        suite.addTest(multiplicationUnitTest('testFour'))
        return suite

def additionSuite():
        suite = unittest.TestSuite()
        suite.addTest(additionUnitTest('testOne'))
        suite.addTest(additionUnitTest('testTwo'))
        suite.addTest(additionUnitTest('testThree'))
        suite.addTest(additionUnitTest('testFour'))
        return suite

def subtractionSuite():
        suite = unittest.TestSuite()
        suite.addTest(subtractionUnitTest('testOne'))
        suite.addTest(subtractionUnitTest('testTwo'))
        suite.addTest(subtractionUnitTest('testThree'))
        suite.addTest(subtractionUnitTest('testFour'))
        suite.addTest(subtractionUnitTest('testFive'))
        suite.addTest(subtractionUnitTest('testSix'))
        return suite

def squareRootSuite():
        suite = unittest.TestSuite()
        suite.addTest(squareRootUnitTest('testOne'))
        suite.addTest(squareRootUnitTest('testTwo'))
        suite.addTest(squareRootUnitTest('testThree'))
        return suite


def main():
    while True:
        inputOne = int(input("What unit test do you want to run?\n1) Exponent\n2) Multiplication\n"
        "3) Addition\n4) Subtraction\n5) Square Root\n6) All\n7) None\n"))

        if inputOne == 1:
            suiteToTest = exponentSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 2:
            suiteToTest = multiplicationSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 3:
            suiteToTest = additionSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 4:
            suiteToTest = subtractionSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 5:
            suiteToTest = squareRootSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 6:
            suiteToTest = unittest.TestSuite([exponentSuite(), multiplicationSuite(), additionSuite(), subtractionSuite(), 
            squareRootSuite()])
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 7:
            print("\nPROGRAM TERMINATED\n")
            break
        
main()
