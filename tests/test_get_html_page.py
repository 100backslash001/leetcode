import sys
import unittest
sys.path.append('..')

from main import get_html_page


class TestGetHtmlMethod(unittest.TestCase):
    def test_valid_url(self):
        url = 'http://leetcode.com'
        html_content = get_html_page(url)
        self.assertIsNotNone(html_content)
    
    def test_invalid_url(self):
        url = 'http://notadomainname.com'
        html_content = get_html_page(url)
        self.assertIsNone(html_content)
    
    def test_empty_url(self):
        url = ''
        html_content = get_html_page(url)
        self.assertIsNone(html_content)

if __name__ == '__main__':
    unittest.main()