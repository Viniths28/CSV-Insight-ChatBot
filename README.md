# CSV-Insight-Chatbot

CSV-Insight-Chatbot is an AI-powered conversational assistant designed to answer questions about the CSV contents. 
It utilizes **Retrieval-Augmented Generation (RAG)** with **ChromaDB** as a vector database and **OpenAI's GPT model** for intelligent responses.

## **Features**
- Uses **ChromaDB** for vector storage.
- **Retrieval-Augmented Generation (RAG)** for enhanced responses.
- Supports **CSV file ingestion** for knowledge base creation.
- **Streamlit UI** for an interactive chatbot experience.

---

## Installation
To run this project locally, follow these steps:

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/ovations-chatbot.git
cd ovations-chatbot
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root directory and add the following:
```
OPENAI_API_KEY=your_openai_api_key_here
```
Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key.

### 5. Run the Python File 
Data Ingestion (Run Once)

Before starting the chatbot, load the CSV data into ChromaDB (only once):

```sh
python csv_data.py
```
Debugging and Managing ChromaDB Collections
List Collections: Use `listcollections` to view all collections in the ChromaDB database.

```sh
python listcollections.py  
```
Verify Collection Contents: Use `verifycollections.py` to inspect the metadata and contents of a specific collection.

```sh
python verifycollections.py  
```
Remove Unwanted Collections: Use removecollections.py `removecollections.py`  to delete any unwanted collections from the ChromaDB database.

```sh
python removecollections.py  
```
Start the Chatbot

After running csv_data.py, start the chatbot with:
```sh
streamlit run chatbot.py
```

This will launch the chatbot in your browser.

## Project Structure
```
├── Ovations_Chatbot/
│   ├── csv_files/           # Folder containing CSV data for vector storage
│   ├── chroma_db/           # ChromaDB persistent storage
│   ├── chatbot.py           # Main Streamlit app
│   ├── CSV_data.py          # Script to load CSV data into ChromaDB
│   ├── requirements.txt     # List of dependencies
│   ├── listcollections.py   # Script to list all collections in ChromaDB
│   ├── verifycollections.py # Script to verify metadata and contents of a collection
│   ├── removecollections.py # Script to remove unwanted collections from ChromaDB
│   ├── requirements.txt     # List of dependencies
│   ├── .env                 # Environment variables (not tracked in Git)
│   ├── README.md            # Project documentation
```

## Requirements
All required dependencies are listed in `requirements.txt`. If you need to install them manually, use:
```sh
pip install streamlit chromadb openai langchain python-dotenv pandas
```

## Usage
- Open the chatbot in your browser and type your queries related to Ovations Speakers Bureau.
- The chatbot retrieves relevant data from the ChromaDB vector store and generates responses using OpenAI's GPT model.
- Responses are displayed in a chat-like interface.



