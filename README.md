﻿# Youtube Video Summarizer
This project helps to summarize the content of a YouTube video into a text format.<br> 
Just copy and past the URL of youtube video and generate the summary using LangChain and Google's LLM. 
#
<b>Tech: LangChain + Google PaLM 2 + Streamlit</b>
#

# Startup 🚀
1. Create a virtual environment `python -m venv venvLangChain`
2. Activate it: 
   - Windows: `.\venvLangChain\Scripts\activate`
3. Clone this repo: `git clone https://github.com/utsavbhattarai/YouTubeVideoSummarizer.git`
4. Go into the directory: `cd YouTubeVideoSummarizer`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Either Add your Google PaLM API_KEY to the .env file into: `GOOGLE_API_KEY=''`<br> 
   or replace: `os.environ['GOOGLE_API_KEY']` with the API_KEY.
7. Start the app: `streamlit run main.py`

# Screenshot
<img src="image/summary.PNG" width="600" height="600">

#

# References

- <a href="https://www.langchain.com/">LangChain</a>
- <a href="https://ai.google/discover/palm2/">Google PaLM 2</a> 
- <a href="https://streamlit.io/">Streamlit</a>
