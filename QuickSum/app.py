import streamlit as st 
from logger import get_logger
from utils import get_content_from_url
from summarizer import get_summary

# Initialize Logger
logger = get_logger(__name__)

# Streamlit Page Configuration
st.set_page_config(page_title="Summarize Text From YT or Website", page_icon="📜", layout="wide")

# Page Title and Tabs for Better Navigation
st.title("📜 Summarize Text From YouTube or Website")
st.markdown("Welcome! This tool helps you generate summaries for YouTube videos or websites. Let's get started!")

# Sidebar with Collapsible Section
with st.sidebar:
    st.header("Settings ⚙️")
    with st.expander("API Key Settings", expanded=True):
        groq_api_key = st.text_input("🔑 Enter Groq API Key", type="password", value="")
        st.caption("This key is needed to access the summarization model securely.")

# Interactive Tabs for URL Input and Instructions
tabs = st.tabs(["🔗 Summarize URL", "📖 How to Use"])
with tabs[0]:
    st.subheader("Summarize Your Content")
    st.write("Enter a YouTube or website URL to summarize it into key points.")

    url = st.text_input("Paste your URL here", placeholder="e.g., https://www.youtube.com/your-video or https://example.com/article")

    if st.button("🚀 Summarize Now!", help="Click to summarize the content from the given URL"):
        if not url.strip() or not groq_api_key.strip():
            st.error("❗ Please provide a valid URL and API Key to continue.")
        else:
            try:
                with st.spinner("⏳ Fetching and summarizing content... This may take a moment."):
                    # Fetch and summarize content
                    docs = get_content_from_url(url)
                    summary = get_summary(docs=docs, groq_api_key=groq_api_key.strip())

                    # Progress Bar for User Feedback
                    st.progress(100)
                    st.success("✅ Summary generated successfully!")

                    # Display Summary in a Stylish Box
                    st.markdown("### 📄 Summary:")
                    st.info(summary)

                    # Optional Download Button with File Type Selection
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="💾 Download Summary as Text",
                            data=summary,
                            file_name='summary.txt',
                            mime='text/plain'
                        )
                    with col2:
                        st.download_button(
                            label="📃 Download Summary as PDF",
                            data=summary,
                            file_name='summary.pdf',
                            mime='application/pdf'
                        )

                    # Logger message
                    logger.info("Summary successfully displayed.")

            except Exception as e:
                st.error("⚠️ Something went wrong while generating the summary. Please try again.")
                logger.error(f"Error in generated summary: {e}")
                raise e

with tabs[1]:
    st.subheader("How to Use the Tool")
    st.write("""
    1. **Enter API Key**: In the sidebar, provide your Groq API Key. It is required for secure access to the summarization model.
    2. **Paste URL**: Enter the URL of a YouTube video or website in the "Summarize Your Content" tab.
    3. **Click Summarize**: Press the '🚀 Summarize Now!' button and wait for the summary to be generated.
    4. **View and Download**: Once ready, the summary will appear below, and you can download it if needed.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Powered by Streamlit")

# Footer Section with Custom HTML for More Style
st.markdown(
    """
    <hr style='border:1px solid #F63366'>
    <div style='text-align:center;'>
        Made with ❤️ by <a href='https://streamlit.io/' target='_blank'>Streamlit</a> and LangChain
    </div>
    """,
    unsafe_allow_html=True
)
