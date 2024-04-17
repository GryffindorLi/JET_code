import unittest

from src.parser import build_parser, split_input


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.query1 = "--search EC4A1BY"
        self.query2 = "-s EC1A1CY"
        self.quit1 = "--quit"
        self.quit2 = "-q"

        self.priority1 = "--search EC4A1BY -q"

        self.parser = build_parser()

    def test_split_input(self):
        self.assertListEqual(['--search', 'EC4A1BY'], split_input(self.query1))
        self.assertListEqual(['-s', 'EC1A1CY'], split_input(self.query2))

        self.assertListEqual(['--quit'], split_input(self.quit1))
        self.assertListEqual(['-q'], split_input(self.quit2))

        self.assertListEqual(["--search", "EC4A1BY", "-q"],
                             split_input(self.priority1))

    def test_query_cmd(self):
        args = self.parser.parse_args(split_input(self.query1))
        self.assertEqual(args.search, "EC4A1BY")

        args = self.parser.parse_args(split_input(self.query2))
        self.assertEqual(args.search, "EC1A1CY")

    def test_quit_cmd(self):
        args = self.parser.parse_args(split_input(self.quit1))
        self.assertTrue(args.quit)

        args = self.parser.parse_args(split_input(self.quit2))
        self.assertTrue(args.quit)

    def test_cmd_priority(self):
        args = self.parser.parse_args(split_input(self.priority1))
        self.assertTrue(args.quit)
        self.assertEqual(args.search, "EC4A1BY")


if __name__ == "__main__":
    unittest.main()
