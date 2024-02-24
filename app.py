from flask import Flask, request, jsonify
from pydantic import ValidationError
from categories import CategoriesReaderToolInput, CategoryURLMapper
from extractor import ArticlesExtractor

app = Flask(__name__)

mapper = CategoryURLMapper()

@app.route('/read-url', methods=['POST'])
def read_url():
    try:
        input_data = CategoriesReaderToolInput(**request.json)
        category = input_data.category
        
        urls = mapper.get_urls_by_category(category)
        
        if not urls:
            return jsonify({
                "success": False,
                "message": "Categoria não encontrada ou não possui URLs associadas.",
                "data": None
            }), 404

        extractor = ArticlesExtractor(urls, category.lower())
        
        articles = extractor.extract_articles()
        
        response = {
            "success": True,
            "message": "Informações processadas com sucesso.",
            "data": {
                "category": category,
                "articles": articles['artigos']
            }
        }
        
        return jsonify(response), 200
        
    except ValidationError as e:
        return jsonify({
            "success": False,
            "message": "Erro de validação nos dados de entrada.",
            "errors": e.errors()
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
