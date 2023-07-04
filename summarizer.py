from GetNewsArticle import GetNewsArticle
# importing ChatOpenAI (Wrapper around OpenAI Chat large language models)
from langchain.chat_models import ChatOpenAI
# schema for formating users input for model
from langchain.schema import HumanMessage
# if a .env file, you've to pass OPENAI_API_KEY
from dotenv import load_dotenv
load_dotenv()


# Taking user news article url
article_url = input("Enter any article link: ")

# Fetch the article we will be summarizing from our
article = GetNewsArticle(article_url)

# Create a chatbot instance that will summarize the article
# verbose for more details to print along
# temperature is the randomness the model can play with
# 0.0 is only for real facts, 1.0 is for full creativity.
llm = ChatOpenAI(model_name="gpt-3.5-turbo", verbose=True, temperature=0.0)

# Create the template for the prompt
# Crafting prompt is main thing in LLM workings.
# using this template, we're asking the chat model to give us the summary of any long article.
template = """You are a smart assistant that summarizes online articles in 100 words.

Here's the article you want to summarize.

==================
Title: {article_title}

{article_text}
==================

Write a summary of the given article.
"""

# Format the prompt with the article details we've got
prompt = template.format(article_title=article.title,
                         article_text=article.text)

# Create a list of messages to send to the chatbot
# but we passing only one message in HumanMessage object form.
messages = [HumanMessage(content=prompt)]

# Send the messages to the chatbot and print the response
output = llm(messages)

# we can print our summary
print("\n" + output.content + "\n")
