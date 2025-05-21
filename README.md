Nutrition Assistant Bot
A simple Streamlit-based chatbot that answers nutrition questions using a custom knowledge base and the gemma:2b model from Ollama.
Features

Provides answers to nutrition questions with sentences tailored to the query.
Uses data_source_1.txt for nutrition information.
Runs locally with Ollama for easy testing.
User-friendly chat interface via Streamlit.

Prerequisites

Python: 3.8 or higher
Ollama: Download from ollama.ai
Pinecone Account: Get an API key from pinecone.io

Project Structure
build_fast_with_ai/
├── StreamlitMain.py    # Streamlit interface
├── RAG_ChatBot.py      # Chatbot logic
├── data_source_1.txt   # Nutrition data
├── requirements.txt    # Python dependencies
└── README.md           # Project guide

Local Setup

Clone the Repository:
git clone https://github.com/BALASAI77/build_fast_with_ai.git
cd build_fast_with_ai


Install Python Dependencies:
pip install -r requirements.txt

Dependencies:

streamlit
langchain
langchain-community
langchain-ollama
langchain-pinecone
pinecone-client
python-dotenv
sentence-transformers


Install Ollama:

Download and install Ollama from ollama.ai.
Pull the gemma:2b model:ollama pull gemma:2b


Start the Ollama server:ollama serve




Set Up Environment Variables:

Create a .env file in the project root:PINECONE_API_KEY=your_pinecone_api_key




Run the App:
streamlit run StreamlitMain.py


Open http://localhost:8501 in a browser.
Ask nutrition questions (e.g., “What foods are high in protein?”).



Usage

Run the app locally and use the Streamlit interface to chat.
The bot uses data_source_1.txt to provide accurate nutrition answers tailored to your question.

Troubleshooting

Ollama Issues: Ensure ollama serve is running and gemma:2b is listed (ollama list).
Pinecone Issues: Check PINECONE_API_KEY and verify the langchain-demo index exists (dimension: 768) in Pinecone.
File Errors: Confirm data_source_1.txt is in the root directory.

