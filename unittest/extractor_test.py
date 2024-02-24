import unittest
from unittest.mock import patch
import sys
import os

# Ajuste o sys.path para garantir que o módulo extractor pode ser importado
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extractor import ArticlesExtractor

class TestArticlesExtractor(unittest.TestCase):
    
    @patch('requests.get')
    def test_extract_articles(self, mock_get):
        html_content = '''
            <div class="c-storiesLatest_content">
                <a href="/deals/save-big-on-top-tech-during-best-buys-member-exclusive-weekend-sale/" class="c-storiesLatest_story">
                    <h3>Save Big on Top Tech During Best Buy's Member-Exclusive Weekend Sale</h3>
                </a>
                <a href="/personal-finance/banking/cds/cd-rates-today-feb-23-2024/" class="c-storiesLatest_story">
                    <h3>CD Rates Today, Feb. 23, 2024: APYs as High as 5.5% Wont Last Forever</h3>
                </a>
            </div>
        '''
        mock_get.return_value.ok = True
        mock_get.return_value.content = html_content.encode('utf-8')  
        mock_get.return_value.text = html_content  

        urls = ["https://www.cnet.com/"]

        extractor = ArticlesExtractor(urls)
        result = extractor.extract_articles()
        
        print("result: ", result)

        self.assertEqual(len(result['artigos']), 2)

        self.assertIn("Save Big on Top Tech During Best Buy's Member-Exclusive Weekend Sale", result['artigos'][0]['title'])
        self.assertEqual(result['artigos'][0]['link'], 'https://www.cnet.com/deals/save-big-on-top-tech-during-best-buys-member-exclusive-weekend-sale/')
        self.assertIn("CD Rates Today, Feb. 23, 2024: APYs as High as 5.5% Won't Last Forever", result['artigos'][1]['title'])
        self.assertEqual(result['artigos'][1]['link'], 'https://www.cnet.com/personal-finance/banking/cds/cd-rates-today-feb-23-2024/')

if __name__ == '__main__':
    unittest.main()
