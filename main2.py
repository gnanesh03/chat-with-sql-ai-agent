from langchain_community.llms import Ollama


llm = Ollama(model = "llama3")


# for chunk in llm.stream("hi"):
#    print(chunk, end = "")



from langchain_community.utilities import SQLDatabase



mysql_uri = 'mysql+mysqlconnector://root:cote34@localhost:3306/product_level2'

db = SQLDatabase.from_uri(mysql_uri)

db.get_usable_table_names()

print(db.table_info)


from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType



agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

#agent_executor.invoke("Which product had the highest CPC (Cost Per Click)?")
agent_executor.invoke("Calculate the RoAS (Return on Ad Spend).")