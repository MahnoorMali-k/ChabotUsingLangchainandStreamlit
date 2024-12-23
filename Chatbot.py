import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import PyPDF2  # For PDF processing

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = ""

# Streamlit App Title
st.title("College and University Chatbot with Document Retrieval")

# Sidebar for Language Selection
selected_language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Urdu"]
)

# Initialize OpenAI Model
model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=256
)

# Memory for Conversation
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# Define Prompt Templates
college_info_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""You are a knowledgeable assistant specialized in providing information exclusively about colleges and universities. 
    You are NOT allowed to provide any information on other topics.
    You must always maintain the context of the conversation to help the user.

    Previous Conversation: {history}
    
    User's current question: {input}
    """
)

# Initialize College Info Chain
college_info_chain = LLMChain(llm=model, prompt=college_info_prompt, memory=st.session_state.memory)

# File Upload
uploaded_file = st.file_uploader("Upload a document for Q&A (TXT, PDF, etc.):", type=["txt", "pdf"])

retrieval_qa_chain = None
if uploaded_file:
    try:
        if uploaded_file.type == "text/plain":
            # Decode TXT file
            file_content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            # Extract text from PDF
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            file_content = ""
            for page in pdf_reader.pages:
                file_content += page.extract_text()

        # Split text into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        documents = text_splitter.split_text(file_content)

        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(documents, embeddings)

        # Create a retriever
        retriever = vector_store.as_retriever()

        # Initialize Retrieval QA chain
        retrieval_qa_chain = RetrievalQA.from_chain_type(llm=model, retriever=retriever)

        st.success("File uploaded and processed successfully!")

    except Exception as e:
        st.error(f"Error processing file: {e}")

# Chat UI
user_input = st.text_input("Ask your question:", key="input")

if st.button("Send"):
    if user_input:
        # Get the chatbot's response
        if retrieval_qa_chain:
            # If a document is uploaded, use Retrieval QA chain
            response = retrieval_qa_chain.run(user_input)
        else:
            # Otherwise, use the college info chain
            response = college_info_chain.run(input=user_input)

        # Display Chat Interface
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Chatbot:** {response}")
