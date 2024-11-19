# **🤖 InsightBot**

**InsightBot** is a modular and interactive chatbot application built with **LangChain**, **Streamlit**, and integrated tools like Wikipedia, Arxiv, and DuckDuckGo. The bot can answer questions with real-time updates, leveraging external APIs and tools.

---

## **🌟 Features**

- **Interactive Chat**: Ask questions and receive intelligent responses in real time.
- **Tool Integration**: Uses Wikipedia, Arxiv, and DuckDuckGo for knowledge retrieval.
- **Streamlit UI**: A simple, intuitive interface for seamless interaction.
- **Logging**: Comprehensive logging for debugging and monitoring.
- **Dockerized Deployment**: Easily deploy the application using Docker.

---

## **📂 Project Structure**

Here’s how the project is organized:

```
INSIGHTBOT/
│
├── app.py                 # Main application file (Streamlit UI)
├── agent.py               # Handles agent setup and user input processing
├── tools.py               # Initializes LangChain tools (Wikipedia, Arxiv, etc.)
├── logger.py              # Sets up structured logging for the application
│
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration for containerized deployment
├── compose.yaml           # Docker Compose file for multi-container setup
│
├── logs/                  # Directory for storing logs
│   ├── app.log            # Log file for application activity
│
└── README.md              # Documentation for the project
```

---

## **🛠️ How It Works**

### **1. app.py**
This is the entry point of the application. It:
- Sets up the Streamlit interface.
- Collects user input and displays responses.
- Calls the `agent.py` functions to process user input.

#### **Sample Code:**
```python
if prompt := st.chat_input(placeholder="Ask your question here..."):
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = process_user_input(api_key, prompt, st.session_state["messages"], callbacks=[st_cb])
        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.write(response)
```

---

### **2. agent.py**
Handles all agent-related tasks:
- Initializes LangChain tools.
- Processes user queries.
- Maintains conversation history.

#### **Core Functionality:**
- **Tool Integration**: Uses the `tools.py` module for connecting to external APIs.
- **Error Handling**: Logs errors if tools or agents fail.

---

### **3. tools.py**
This module initializes external tools for the chatbot:
- **Wikipedia**: Retrieves general knowledge.
- **Arxiv**: Provides research paper summaries.
- **DuckDuckGo**: A search engine for diverse queries.

#### **Example Initialization:**
```python
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
search = DuckDuckGoSearchRun(name="Search")
```

---

### **4. logger.py**
Sets up structured logging for debugging and monitoring:
- Logs are stored in the `logs/app.log` file.
- Ensures that all major events (e.g., errors, API calls) are recorded.

#### **Sample Log Entry:**
```plaintext
2024-11-19 17:03:57,345 - INFO - Tools initialized successfully.
2024-11-19 17:04:22,123 - ERROR - Error processing user input: [Error Details]
```

---

## **🚀 Getting Started**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/syedmuneeb321/InsightBot.git
cd InsightBot
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Application**
```bash
streamlit run app.py
```

### **Step 4: Access the App**
- Open your browser at `http://localhost:8501`.
- Enter your API key in the sidebar to get started.

---

## **🐳 Docker Deployment**

To deploy the application using Docker, follow these steps:

### **Step 1: Build the Docker Image**
```bash
docker build -t insightbot .
```

### **Step 2: Run the Container**
```bash
docker run -p 8501:8501 insightbot
```

### **Step 3: Multi-Container Deployment**
Use the `compose.yaml` file to orchestrate the deployment:
```bash
docker-compose up
```

---

## **🛠️ Tools & Technology**

The project leverages the following technologies:

| **Component**       | **Technology**                |
|----------------------|-------------------------------|
| **Frontend**         | Streamlit                    |
| **Backend**          | LangChain                    |
| **AI Model**         | Groq Model (Llama3-8b-8192)  |
| **Search Tools**     | Wikipedia, Arxiv, DuckDuckGo |
| **Logging**          | Python Logging Module        |
| **Containerization** | Docker, Docker Compose       |

---

## **📜 Logging**

Logs are stored in the `logs/app.log` file. They include:
- Application start events.
- User queries.
- Tool initialization status.
- Errors and debugging information.

#### **Example Log:**
```plaintext
2024-11-19 17:10:45,345 - INFO - Application started successfully
2024-11-19 17:11:15,678 - INFO - User input received: What is AI?
2024-11-19 17:11:45,123 - INFO - Response generated successfully.
2024-11-19 17:12:00,456 - ERROR - Error initializing tools: [Error details]
```

---

## **🎯 Key Features**

- **Real-Time Updates**: Provides incremental responses using LangChain callbacks.
- **Tool Integration**: Combines knowledge from Wikipedia, Arxiv, and DuckDuckGo.
- **Modular Code**: Each functionality is handled in a separate file for maintainability.
- **Docker Support**: Easy deployment via Docker and Docker Compose.

---

## **📈 Future Enhancements**

- Add more tools like OpenWeather for weather data or NewsAPI for news updates.
- Implement user authentication for secure access.
- Enhance the UI for better user experience.

---

## **🤝 Contribution Guidelines**

We welcome contributions to improve **InsightBot**! Follow these steps to contribute:

1. **Fork the Repository**:
   - Click the "Fork" button at the top right.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/syedmuneeb321/InsightBot.git
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b feature-branch-name
   ```
4. **Make Changes**:
   - Modify files or add new features.
5. **Commit Changes**:
   ```bash
   git add .
   git commit -m "Added [feature]"
   ```
6. **Push Changes**:
   ```bash
   git push origin feature-branch-name
   ```
7. **Submit a Pull Request**:
   - Go to the original repository and click "New Pull Request".

---

## **📝 License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
