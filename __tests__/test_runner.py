import unittest
from __tests__.html_conversor import TestHTMLConversor
from robocorp.tasks import task

@task
def run_test():
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHTMLConversor)
    
    # Create a test runner
    runner = unittest.TextTestRunner()
    
    # Run the tests
    result = runner.run(suite)
