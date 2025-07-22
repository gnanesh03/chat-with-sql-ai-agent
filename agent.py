from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType

llm = Ollama(model="llama3")

# Connecting my local mysql database
mysql_uri = 'mysql+mysqlconnector://root:cote34@localhost:3306/product_level2'
db = SQLDatabase.from_uri(mysql_uri)

# Create the LangChain SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_query(question: str) -> str:

   result=  agent_executor.invoke(question)
   return result["output"]