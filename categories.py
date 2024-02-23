from pydantic import BaseModel

class CategoriesReaderToolInput(BaseModel):
    category: str
class CategoryURLMapper:
    def __init__(self):
        
        self.category_to_urls = {
            'Tecnologia': ['https://www.cnet.com/', 'https://www.tecmundo.com.br/'],
            'Política': ['https://jovempan.com.br/noticias/politica', 'https://noticias.r7.com/brasilia/noticias'],
        }

    def get_urls_by_category(self, category):
        """
        Dada uma categoria, retorna a lista de URLs associadas.
        Retorna uma lista vazia se a categoria não for encontrada.
        """
        return self.category_to_urls.get(category, [])
