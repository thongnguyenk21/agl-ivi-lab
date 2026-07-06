import importlib
import unittest


class PackageTests(unittest.TestCase):
    # Brief: Verifies that the package exposes its initial version.
    # Params:
    #   self: Current test case instance.
    def test_exposes_version(self) -> None:
        try:
            package = importlib.import_module("agl_ivi_lab")
        except ModuleNotFoundError as error:
            self.fail(str(error))

        self.assertEqual(package.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
