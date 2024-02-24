from pydantic import BaseModel

class CategoriesReaderToolInput(BaseModel):
    category: str
class CategoryURLMapper:
    
    def __init__(self):
        
        self.category_to_urls = {
            'Tecnologia': ['https://www.cnet.com/', 'https://g1.globo.com/tecnologia/?=erDh'],
            'Política': ['https://jovempan.com.br/noticias/politica', 'https://noticias.r7.com/brasilia/noticias'],
            'Esportes': ['https://www.gazetaesportiva.com', 'https://www.uol.com.br/esporte'],
            'Saúde': ['https://veja.abril.com.br', 'https://www.estadao.com.br'],
            'Economia': ['https://www.bloomberg.com', 'https://www.valor.com.br'],
            'Cultura e Entretenimento': ['https://www.rollingstone.com', 'https://www.timeout.com'],
            'Ciência': ['https://www.sciencemag.org', 'https://www.nature.com'],
            'Meio Ambiente': ['https://www.nationalgeographic.com/environment', 'https://www.greenpeace.org/international'],
            'Educação': ['https://www.edutopia.org', 'https://www.chronicle.com'],
        }

    def get_urls_by_category(self, category):
        """
        Dada uma categoria, retorna a lista de URLs associadas.
        Retorna uma lista vazia se a categoria não for encontrada.
        """
        return self.category_to_urls.get(category, [])
