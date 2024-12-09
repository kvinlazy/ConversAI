# ConversAI

ConversAI is a dynamic and user-friendly chatbot application built with Streamlit. It leverages the power of Hugging Face's API to facilitate natural language conversations, making it adaptable to various use cases. The underlying model can easily be replaced with other Hugging Face models, providing flexibility for tailored chatbot behavior.

## Features
- **Interactive Conversations:** Enables users to interact naturally with an AI chatbot.
- **Customizable AI Model:** Replaceable Hugging Face model for different use cases.
- **Session-based Chat History:** Maintains chat context throughout the conversation.
- **Streamlit Framework:** Simplifies development and deployment.

## Installation

### Prerequisites
- Python 3.8 or higher installed on your system.
- Hugging Face API token. You can get one by signing up at [Hugging Face](https://huggingface.co/).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ConversAI.git
   cd ConversAI
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (Streamlit will display a local URL).
2. Type your query into the input field and press enter.
3. ConversAI will respond using the configured Hugging Face model.
4. To replace the model, update the following lines in the code:
   ```python
   API_URL = "https://api-inference.huggingface.co/models/<your-model-name>"
   headers = {"Authorization": f"Bearer <your-hugging-face-api-token>"}
   ```

## Customization

- **Dynamic Model Selection:** Implement a dropdown to select models within the app.
- **Additional Features:** Add functionalities like keyword extraction, text summarization, or other NLP tasks.

## Requirements

Create a `requirements.txt` file with the following content:
```plaintext
streamlit==1.26.0
requests==2.31.0
```

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Disclaimer

ConversAI is a tool for experimentation and **not a substitute for professional advice** in any domain. The quality of the responses depends on the AI model used.


## Contributing
We welcome contributions to improve ConversAI. If you have ideas, please:
1. Fork this repository.
2. Make your changes.
3. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [Hugging Face](https://huggingface.co/) for their robust AI models.
- [Streamlit](https://streamlit.io/) for enabling simple and effective web app development.
