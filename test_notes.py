import unittest
from note import Note

class TestNote(unittest.TestCase):
    def test_link(self):
        n = Note("Test", "Content")
        n.add_link("Another")
        self.assertIn("Another", n.links)

if __name__ == "__main__":
    unittest.main()
