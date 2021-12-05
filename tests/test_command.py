from unittest import TestCase
from pyperclip import paste

import command


class MainTest(TestCase):

    def test_main(self):
        expected_text = 'copy_target'
        command.main(expected_text)
        self.assertEqual(expected_text, paste())
