from AcceptanceTests import AcceptanceTestsModel
import unittest


def my_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(AcceptanceTestsModel))
    return the_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)