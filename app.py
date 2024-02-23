from flask import Flask, request, jsonify
from pydantic import ValidationError
from categories import CategoriesReaderToolInput, CategoryURLMapper

app = Flask(__name__)

mapper = CategoryURLMapper()

@app.route('/read-url', methods=['POST'])
def read_url():
    
    try:
        input_data = CategoriesReaderToolInput(**request.json)
        category = input_data.category
        urls = mapper.get_urls_by_category(category)
        return jsonify(urls)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
