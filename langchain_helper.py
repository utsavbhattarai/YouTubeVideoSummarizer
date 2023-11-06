import os

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import GooglePalm
from langchain.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

def summarizeYTVideo(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
    result = loader.load()

    title = result[0].metadata['title']
    author = result[0].metadata['author']
    lengthOfVideo = result[0].metadata['length']

    # Init LLM using the API KEY
    # either create a .env file with GOOGLE_API_KEY = '' 
    # or remove os.environ['GOOGLE_API_KEY'] and replace with the API_KEY
    llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.5)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap=0)
    texts = text_splitter.split_documents(result)

    chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=False)
    summary = chain.run(texts)

    return summary, title, author, lengthOfVideo