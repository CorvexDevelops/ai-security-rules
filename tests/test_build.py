# Author: CorvexDevelops
"""Tests for build.py: every format builds, the block is replaced in place, the rest of the file stays."""
import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class Build(unittest.TestCase):
    def test_every_format_and_language(self):
        for fmt in build.FORMATS:
            for lang in ("en", "it"):
                doc = build.document(fmt, list(build.DATA["stacks"]), lang)
                self.assertIn(build.START, doc)
                self.assertIn(build.END, doc)
                self.assertGreater(doc.count("\n- "), 20)

    def test_cursor_has_front_matter(self):
        self.assertTrue(build.document("cursor", ["next"]).startswith("---\ndescription:"))

    def test_regenerating_keeps_the_rest_of_the_file(self):
        mine = "# My project\n\nKeep this line.\n"
        first = build.document("claude", ["supabase"], "en", mine)
        second = build.document("claude", ["llm"], "en", first)
        self.assertIn("Keep this line.", second)
        self.assertEqual(second.count(build.START), 1)
        self.assertIn("dangerouslyAllowBrowser", second)
        self.assertNotIn("Row Level Security", second)

    def test_unknown_stack_is_refused(self):
        with self.assertRaises(ValueError):
            build.document("claude", ["cobol"])

    def test_ready_files_match_the_generator(self):
        for lang in ("en", "it"):
            for fmt, rel in build.FORMATS.items():
                with open(os.path.join(HERE, "ready", lang, rel), encoding="utf-8") as f:
                    text = f.read()
                self.assertIn(build.block(list(build.DATA["stacks"]), lang), text)


if __name__ == "__main__":
    unittest.main()
