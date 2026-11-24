import unittest

from entities.source import Source


class TestSource(unittest.TestCase):
    def test_parse_content_returns_property_and_value_pairs(self):
        content = "Title: A Study\nAuthor: Ada Lovelace\n"

        self.assertEqual(
            Source.parse_content(content),
            [("Title", "A Study"), ("Author", "Ada Lovelace")],
        )

    def test_parse_content_splits_only_at_first_colon(self):
        content = "URL: https://example.test/a:b\n"

        self.assertEqual(
            Source.parse_content(content),
            [("URL", "https://example.test/a:b")],
        )


if __name__ == "__main__":
    unittest.main()
