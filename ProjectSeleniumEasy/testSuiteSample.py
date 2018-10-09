import unittest
import SC1_SingleInputField
import SC2_TwoInputForm

loader=unittest.TestLoader()
suite=unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(SC1_SingleInputField))
suite.addTest(loader.loadTestsFromModule(SC2_TwoInputForm))
unittest.TextTestRunner(verbosity=105).run(suite)