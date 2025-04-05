from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

message = [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("Give a short tip to create engaging posts on Instagram")
]

result = llm.invoke(message) 
print(result.content)
