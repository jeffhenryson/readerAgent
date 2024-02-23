from pydantic import BaseModel

class ReaderToolInput(BaseModel):
    category: str
    include_body: bool
    cursor: int

class CategoryURLMapper:
        
    def __init__(self):
        # Este dicionário armazena as categorias e suas respectivas URLs
        self.category_to_urls = {
            'Esportes': ['http://exemplo1.com', 'http://exemplo2.com'],
            'Economia': ['http://exemplo3.com', 'http://exemplo4.com'],
            'Tecnologia': ['https://www.cnet.com/', 'http://exemplo4.com'],
            'Política': ['https://jovempan.com.br/noticias/politica', 'https://noticias.r7.com/brasilia/noticias'],
        }

    def get_urls_by_category(self, category):
        """
        Dada uma categoria, retorna a lista de URLs associadas.
        Retorna uma lista vazia se a categoria não for encontrada.
        """
        return self.category_to_urls.get(category, [])
