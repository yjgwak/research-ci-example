class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("Test")
        self.assertEqual(ret, "Hello World!")


if __name__ == "__main__":
    unittest.main()
