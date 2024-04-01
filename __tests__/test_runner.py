import unittest
from __tests__.html_conversor import TestHTMLConversor
from robocorp.tasks import task


class TestRunner():
    def __init__(self):
        pass
    
    def test_html_conversor(self):
        # Create a test suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestHTMLConversor)
        
        # Create a test runner
        runner = unittest.TextTestRunner()
        
        # Run the tests
        runner.run(suite)


@task
def run_test():
    test_runner = TestRunner()
    test_runner.test_html_conversor()
    