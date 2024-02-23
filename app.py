# app.py

from flask import Flask, request, jsonify
from pydantic import ValidationError
from reader import ReaderTool, ReaderToolInput

app = Flask(__name__)

@app.route('/read-url', methods=['POST'])
def read_url():
    input_data = ReaderToolInput(**request.json)
    reader_tool = ReaderTool()
    
    result = reader_tool._run(url=input_data.url, include_body=input_data.include_body, cursor=input_data.cursor)
    return result    

if __name__ == '__main__':
    app.run(debug=True)
