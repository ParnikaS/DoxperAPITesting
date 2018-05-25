# tests/runner.py
import unittest

# import your test modules
import TestLoginApi
import TestValidatePasswordApi
import TestUpdatePasswordApi
import TestAccountCreationApi
import TestEditDoctorProfileApi



# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestLoginApi))
suite.addTests(loader.loadTestsFromModule(TestValidatePasswordApi))
suite.addTests(loader.loadTestsFromModule(TestUpdatePasswordApi))
suite.addTests(loader.loadTestsFromModule(TestAccountCreationApi))
suite.addTests(loader.loadTestsFromModule(TestEditDoctorProfileApi))
#suite.addTests(loader.loadTestsFromModule())

print(suite.countTestCases())

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)