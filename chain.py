# SETUP LANGCHAIN
import os
from main import get_article
from google.colab import userdata
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.tools import BraveSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatPerplexity
from langchain_community.document_loaders import NewsURLLoader
from langchain.tools import Tool
from prompts import summarizer_prompt, researcher_prompt, writer_prompt
from bs4 import BeautifulSoup


# Defininf Langchain Elements :
claude_model = ChatAnthropic(model="claude-3-sonnet-20240229", api_key=userdata.get('CLAUDE_API_KEY'))
perplexity_model = ChatPerplexity(model="llama-3-sonar-large-32k-online", temperature=0.7, api_key= userdata.get('PERPLEXITY_KEY'),)
gpt_model = ChatOpenAI(model='gpt-3.5-turbo', temperature = 0.6 , api_key = userdata.get('openai_key'))

parser = StrOutputParser()


#function to setup langsmith 
def setup_stuff():
  lc_key= userdata.get('langchain_key')
  os.environ["LANGCHAIN_TRACING_V2"] = "true"
  os.environ["LANGCHAIN_PROJECT"] = "Agentic"
  os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
  os.environ["LANGCHAIN_API_KEY"] = lc_key
  return


def writingpro_chain(url:str):
  input_text= get_article(url)
  # Summarizer Chain :
  summarizer_chain= {'article': RunnablePassthrough()}| summarizer_prompt | gpt_model | StrOutputParser()

  summary= summarizer_chain.invoke({"article": input_text})

  # Researcher Chain :
  researcher_chain = {'summary': RunnablePassthrough()}| researcher_prompt | perplexity_model | StrOutputParser() 

  outline = researcher_chain.invoke({"summary": summary})

  # Writer Chain :
  writer_chain = {'newsletter_outline': RunnablePassthrough()} | writer_prompt | claude_model | parser

  newsletter_raw = writer_chain.invoke({"newsletter_outline": outline})
  # Parse the HTML content using BeautifulSoup
  generated_newsletter = BeautifulSoup(newsletter_raw, 'html.parser')
  return summary, outline, generated_newsletter

