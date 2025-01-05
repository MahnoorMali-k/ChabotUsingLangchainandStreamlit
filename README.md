# Multilingual College and University Information Chatbot

This repository contains a **Multilingual Chatbot** built using **LangChain** and **Streamlit** in Python. The chatbot provides answers about colleges and universities, supports multiple languages, and allows users to upload documents for extracting and querying information.

## Screenshot
![Chatbot Screenshot](bot.png)

## Features
- **Multilingual Support**: Interact with the chatbot in various languages, making it accessible to a diverse user base.
- **College and University Information**: Get detailed answers about colleges, universities, courses, and other related queries.
- **Document Upload**: Upload documents (e.g., PDFs, Txt files) and query their content for specific information.
- **User-Friendly Interface**: Built using Streamlit, the chatbot features an intuitive and interactive UI.
- **Memory History**: The chatbot maintains conversation history using LangChain's **ConversationBuffer** functionality, allowing users to have a continuous and contextual conversation.


### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/MahnoorMali-k/ChabotUsingLangchainandStreamlit.git
   cd MultilingualChatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## How It Works

### Multilingual Support
The chatbot uses LangChain's language processing capabilities to interact in multiple languages. It identifies the user's language and responds accordingly.

### Document Upload
Users can upload documents in supported formats (PDF, TXT). The chatbot processes these documents, splits them into chunks, and indexes them for querying.

### Conversation History
The **ConversationBuffer** function in LangChain allows the chatbot to remember past interactions in a session. This feature enhances the user experience by enabling contextual and coherent conversations.

## Dependencies
The chatbot uses the following major libraries:
- **LangChain**: For natural language processing and conversational AI.
- **Streamlit**: For building the web-based user interface.
- **PyPDF2**: For processing PDF files.
  
## Future Enhancements
- Add support for more document formats.
- Improve multilingual capabilities for less common languages.
- Integrate with external APIs for live college and university data.

## Contribution
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

Enjoy using the Multilingual College and University Information Chatbot! If you have any questions or feedback, please open an issue or contact the repository owner.
