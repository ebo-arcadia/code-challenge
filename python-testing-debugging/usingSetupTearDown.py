import unittest
import os

class CodeStatus:
    def __init__(self):
        self.deployed = False
        self.log_file = "code_status.log.txt"
        file_content = "code deployment status has been recorded"
        with open(self.log_file, "w") as file:
            file.write(file_content)

    def remove_file(self):
        os.remove(self.log_file)

    def deployCode(self):
        self.deployed = True


class TestCodeStatus(unittest.TestCase):
    def setUp(self) -> None:
        self.code_status = CodeStatus()

    def tearDown(self):
        self.code_status.remove_file()

    def test_initial_code_status(self):
        self.assertFalse(self.code_status.deployed, "code has not been deployed")

    def test_final_code_status(self):
        self.code_status.deployCode()
        self.assertTrue(self.code_status.deployed, "code has been deployed")

    def test_write_code_status_log_file(self):
        with open(self.code_status.log_file) as file:
            contents = file.read()
        self.assertEqual(contents, "code deployment status has been recorded")
