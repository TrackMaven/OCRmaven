from flask import request, jsonify 
from .ocr import process_image
from . import app


@app.route('/', methods=["POST"])
def ocr():
    try:
        urls = request.json.get('image_urls')
        output = [process_image(url) for url in urls]
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})
