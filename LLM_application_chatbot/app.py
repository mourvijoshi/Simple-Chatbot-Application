from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

# Serve the index.html page for the frontend
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Make sure index.html is in the "templates" folder

# Define the /chatbot route to handle chatbot prompts
@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    # Read the prompt from the HTTP request body
    data = request.get_json()  # This automatically parses JSON input
    input_text = data.get('prompt', '')

    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs, max_length=60)  # Limit max length to prevent crashing
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add the conversation to the history
    conversation_history.append(input_text)
    conversation_history.append(response)

    # Return response as a JSON object
    return jsonify({"response": response})

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for better error messages
