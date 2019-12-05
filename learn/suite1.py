import unittest

class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param1=None,param2=None,param3=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    @staticmethod
    def parametrize_case(classname,casename, param1=None,param2=None,param3=None):
        suite = unittest.TestSuite()
        suite.addTest(classname(casename, param1=param1, param2=param2, param3=param3))
        return suite

    @staticmethod
    def parametrize_class(testcase_klass, param1=None,param2=None,param3=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param1=param1, param2=param2, param3=param3))
        return suite