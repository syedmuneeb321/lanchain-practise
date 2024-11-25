# QuickSum

🎉 Welcome to **QuickSum**! 🎉  
QuickSum is your personal content assistant, designed to help you quickly and easily summarize content from YouTube videos and websites. Whether it's a long article or a detailed video, QuickSum has you covered with concise, easy-to-understand summaries. 🚀

## 🚀 Project Overview
QuickSum is built with **Streamlit**, offering a seamless and interactive web interface that anyone can use. Using advanced AI models, QuickSum delivers essential information from any URL in seconds, helping you save time and focus on what really matters.

No more skimming through endless paragraphs or watching hour-long videos for key points - just let QuickSum do the work for you! 💡

## ✨ Features
- **📹 Summarize YouTube Videos**: Get the key points from YouTube content without needing to watch the entire video.
- **🌐 Summarize Websites**: Quickly summarize articles, blogs, and webpages to get straight to the valuable information.
- **🖱️ User-Friendly Interface**: QuickSum's interactive UI powered by Streamlit makes summarizing content as simple as a few clicks.
- **💾 Download Summaries**: Download generated summaries in text or PDF format to save for later.

## 📂 Directory Structure
Here's a quick look at what each file in this project does:

```
📦 QuickSum
├── 📜 app.py             # 🚀 Main file that runs the Streamlit app
├── 📝 logger.py          # 🛠️ Logger for tracking activities and errors
├── 🤖 summarizer.py      # ✨ Core functions for generating summaries
├── ⚙️ utils.py           # 🔗 Utility functions like fetching YouTube or website data
├── 📄 requirements.txt   # 📦 Dependencies needed to run QuickSum
├── 📦 Dockerfile         # 🐳 Containerizes the app for deployment
├── ⚙️ compose.yaml       # 🗂️ Configuration for Docker services
└── 📋 app.log            # 🧐 Application logs for monitoring and debugging
```

## 🛠️ Installation
Follow these steps to get QuickSum up and running:

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd QuickSum
   ```

2. **Install Dependencies**  
   Make sure you have Python installed. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

   Then open your browser and navigate to `http://localhost:8501` to start using QuickSum!

4. **Docker Setup (Optional)**  
   Prefer to use Docker? No problem! Build and run the Docker container with:
   ```bash
   docker-compose up --build
   ```

## 🎯 Usage
Using QuickSum is super easy! Here's how:

1. **🔑 Enter Your API Key**: In the sidebar, provide your Groq API Key for secure access to the summarization model.
2. **🌐 Input URL**: Paste a valid YouTube or website URL that you want summarized.
3. **📋 Click Summarize**: Hit the "Summarize" button and watch as QuickSum works its magic!
4. **💾 Download Summary**: Once your summary is ready, download it in either text or PDF format.

## 🤝 Contributions
We love contributions! If you have ideas to make QuickSum even better, feel free to create an issue or submit a pull request. Let’s make QuickSum awesome together! 💪

## 📜 License
QuickSum is licensed under the **MIT License**. Feel free to use, modify, and distribute it as per the terms of the license.

## 🙏 Acknowledgments
- **Streamlit**: For providing an incredible platform that makes building interactive web apps a breeze.
- **LangChain**: For powering the AI-based summarization behind QuickSum.

---
### ❤️ Thank You for Using QuickSum!  
We hope QuickSum makes your reading and viewing experience more productive. If you have any questions or encounter any issues, don't hesitate to reach out. Your feedback helps us improve!

Happy Summarizing! 😊

