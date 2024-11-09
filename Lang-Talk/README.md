# 🌟 LangTalk - Simple AI-Powered Chatbot in a Container

**LangTalk** is a lightweight, containerized Streamlit chatbot that simplifies AI-powered conversations with large language models (LLMs). Built with LangChain, LangTalk lets you chat with models like Google, OpenAI, and Groq in a straightforward setup using Docker and Docker Compose. Perfect for experimenting or building basic conversational applications!

---

## ✨ Key Features

- **🔧 Modular Design**: Organized code for prompts, LLM responses, and UI makes LangTalk easy to customize and maintain.
- **⚙️ Flexible Model Choices**: Switch effortlessly between Google, OpenAI, and Groq models.
- **💬 User-Friendly Interface**: Powered by Streamlit for a clean, interactive chat experience.
- **📦 Containerized Deployment**: Run it smoothly with Docker and Docker Compose—no fuss!

---

## 📁 Project Structure

```plaintext
├── app.py                  # Main Streamlit app
├── prompt.py               # Chat prompt template
├── response.py             # LLM response logic
├── Dockerfile              # Docker config
├── docker-compose.yml      # Docker Compose config
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (API keys, etc.)
```

---

## 🚀 Getting Started

### 📝 Prerequisites

1. **Docker**: [Download Docker here](https://www.docker.com/).
2. **API Keys**: Get API keys for Google, OpenAI, or Groq models.

### ⚙️ Installation

1. **Clone This Repository**:

   ```bash
   git clone https://github.com/yourusername/langtalk.git
   cd langtalk
   ```

2. **Set Up Your Environment Variables**:

   Add API key details in a `.env` file:

   ```plaintext
   LANGCHAIN_API_KEY=your_api_key_here
   LANGCHAIN_PROJECT=your_project_id_here
   LANGCHAIN_TRACING_V2=true
   ```

3. **Add Required Dependencies**:

   Make sure `requirements.txt` includes the following:

   ```plaintext
   streamlit
   langchain
   python-dotenv
   langchain-google-genai
   langchain-openai
   langchain-groq
   ```

4. **Run the App**:

   ```bash
   docker-compose up --build
   ```

   Once built, access LangTalk at [http://localhost:8501](http://localhost:8501).

---

## 🎯 Using LangTalk

1. **Configure Settings**: Enter the API key, choose a model, and adjust settings in the sidebar.
2. **Start Chatting**: Type in a message, and LangTalk will generate a response using the chosen model!

---

## 🛠️ Error Handling

LangTalk provides clear notifications for common issues:
- **Input Issues**: Alerts for input errors.
- **API Key Errors**: Warnings for missing/invalid API keys.
- **Network Issues**: Notifications if the API is unreachable.
- **Other Errors**: General notifications for unexpected issues.

---

## ⚙️ Customization Options

- **Customize Prompts**: Modify `prompt.py` for different prompt styles.
- **Update LLM Logic**: Adjust `llm.py` to add models or change response logic.

---

## 📜 License

LangTalk is available under the MIT License.


