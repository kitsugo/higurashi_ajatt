#!/usr/bin/env python3
import unittest
import extractor


class TestExtractor(unittest.TestCase):
    def test_test(self):
        self.assertEqual(extractor.line_to_html_paragraph(["a", "A"]), "<p>A</p>", "a")

    def test_extra_section_found(self):
        e = extractor.EXTRA_SECTION_RE.search("if(GetGlobalFlag(GCensor) >= 3){ModCallScriptSection(\"zonik_004_vm0x_n01\",\"dialog005\");}")

        print("w")
        print(e)



if __name__ == "__main__":
    unittest.main()
