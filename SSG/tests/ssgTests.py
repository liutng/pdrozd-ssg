import unittest

from SSG.utils.input import parseInput
import os
import shutil
import warnings


class SSGTest(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    # Tests Parse Input Title
    def test_parseInput_Title(self):
        arg = os.path.join(os.path.abspath(os.getcwd()), "testFiles", "test1.txt")
        parseInput(arg)
        site = os.path.join(os.path.abspath(os.getcwd()), "dist", "Test Title.html")
        self.assertTrue(os.path.isfile(site))
        newDir = os.path.join(os.path.abspath(os.getcwd()), "dist")
        shutil.rmtree(newDir)

    # Tests Parse Input for body text
    def test_parseInput_Body(self):
        arg = os.path.join(os.path.abspath(os.getcwd()), "testFiles", "test1.txt")
        parseInput(arg)
        site = os.path.join(os.path.abspath(os.getcwd()), "dist", "Test Title.html")

        succsess = False
        with open(site, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

            for line in lines:
                if line == "<p>Test Body</p>":
                    succsess = True
                    break

        self.assertTrue(succsess)
        newDir = os.path.join(os.path.abspath(os.getcwd()), "dist")
        shutil.rmtree(newDir)

    def tearDown(self):
        warnings.simplefilter("default", ResourceWarning)


if __name__ == "__main__":
    unittest.main()
