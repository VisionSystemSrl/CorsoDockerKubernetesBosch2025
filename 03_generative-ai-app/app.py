from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load a Hugging Face text generation model
generator = pipeline("text-generation", model="gpt2")

@app.route('/generate', methods=['POST'])
def generate_text():
    # Get input data from request
    input_data = request.json.get('text', '')
    if not input_data:
        return jsonify({"error": "No input text provided"}), 400
    
    # Generate text
    result = generator(input_data, max_length=50, num_return_sequences=1)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
