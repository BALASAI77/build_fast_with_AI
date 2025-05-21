from RAG_ChatBot import ChatBot
import streamlit as st
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Cache the chatbot to speed up loading
@st.cache_resource
def load_chatbot():
    logger.debug("Initializing ChatBot")
    data_file = './materials/data_source_1.txt'
    if not os.path.exists(data_file):
        logger.error(f"Data file {data_file} not found")
        st.error(f"Data file {data_file} not found. Please ensure it exists.")
        st.stop()
    return ChatBot()

try:
    bot = load_chatbot()
except Exception as e:
    st.error(f"Error initializing chatbot: {str(e)}")
    st.stop()

st.title('Nutrition Assistant Bot')

# Function for generating LLM response
def generate_response(input_text):
    try:
        logger.debug(f"Processing input: {input_text}")
        result = bot.rag_chain.invoke(input_text)
        logger.debug(f"RAG chain result: {result}")
        # Handle different return types from invoke
        if isinstance(result, dict) and "result" in result:
            response = result["result"]
        elif isinstance(result, str):
            response = result
        else:
            raise ValueError(f"Unexpected response type from rag_chain.invoke: {type(result)}")
        # Check if response is empty or whitespace
        if not response or response.strip() == "":
            logger.warning("Generated response is empty")
            return "No relevant information found. Please check if the data source contains nutrition information or try a different question."
        return response.strip()
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return f"Error generating response: {str(e)}"

# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm NutritionBot. How can I assist you today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input_text := st.chat_input(placeholder="Ask about nutrition (e.g., 'practical tips on healthy eating')..."):
    logger.debug(f"User input received: {input_text}")
    st.session_state.messages.append({"role": "user", "content": input_text})
    with st.chat_message("user"):
        st.write(input_text)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Getting your answer..."):
                response = generate_response(input_text)
                logger.debug(f"Response to display: {response}")
                st.write(response)
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)