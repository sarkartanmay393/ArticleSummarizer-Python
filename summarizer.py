
from fetcher import Fetcher
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
load_dotenv()


# Fetch the article we will be summarizing
article = Fetcher("https://labs.hakaioffsec.com/nginx-alias-traversal/")

# Create a chatbot that will summarize the article
llm = ChatOpenAI(model_name="gpt-3.5-turbo", verbose=True, temperature=0.0)

# Create the template for the prompt
template = """You are a very good assistant that summarizes online articles.

Here's the article you want to summarize in 100 words.

==================
Title: {article_title}

{article_text}
==================

Write a summary of the previous article.
"""

# Format the prompt with the article details
prompt = template.format(article_title=article.title,
                         article_text=article.text)

# Create a list of messages to send to the chatbot
messages = [HumanMessage(content=prompt)]

# Send the messages to the chatbot and print the response
print(llm(messages))
