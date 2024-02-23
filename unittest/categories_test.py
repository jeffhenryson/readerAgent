import unittest
from pydantic import BaseModel

class ReaderToolInput(BaseModel):
    category: str
    include_body: bool
    cursor: int

class CategoryURLMapper:
    
    def __init__(self):
        self.category_to_urls = {
            'Tecnologia': ['https://www.cnet.com/', 'http://exemplo4.com'],
            'Política': ['https://jovempan.com.br/noticias/politica', 'https://noticias.r7.com/brasilia/noticias'],
        }

    def get_urls_by_category(self, category):
        """
        Dada uma categoria, retorna a lista de URLs associadas.
        Retorna uma lista vazia se a categoria não for encontrada.
        """
        return self.category_to_urls.get(category, [])

class TestCategoryURLMapper(unittest.TestCase):
    
    def setUp(self):
        self.mapper = CategoryURLMapper()
    
    def test_get_urls_by_category_found(self):
        # Corrigido para testar a categoria 'Política' com as URLs corretas
        category = 'Política'
        expected_urls = ['https://jovempan.com.br/noticias/politica', 'https://noticias.r7.com/brasilia/noticias']
        result = self.mapper.get_urls_by_category(category)
        # resultado da função
        print(result)
        self.assertEqual(result, expected_urls)
    
    def test_get_urls_by_category_not_found(self):
        category = 'Inexistente'
        expected_urls = []
        result = self.mapper.get_urls_by_category(category)
        # resultado da função
        print(result)
        self.assertEqual(result, expected_urls)

if __name__ == '__main__':
    unittest.main()
