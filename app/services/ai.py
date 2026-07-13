from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
   res = client.embeddings.create(
       model="text-embedding-3-small",
       input=text
   )
   return res.data[0].embedding

def chat_with_context(prompt):
   res = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role": "user", "content": prompt}]
   )
   return res.choices[0].message.content
