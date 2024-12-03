import unittest

class TestHelloWorldPage(unittest.TestCase):
    def test_heading(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
        self.assertIn('<h1>¡Hola Mundo!</h1>', content)

if __name__ == '__main__':
    unittest.main()
