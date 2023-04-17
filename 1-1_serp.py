from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# LLM ラッパーを導入します。これは、エージェントをコントロールするために使われます。
llm = OpenAI(temperature=0)

# ツールを導入します。 `llm-math` ツールを使うのに LLM を指定する必要があることに注意してください
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# エージェントを初期化します
# 初期化時には、使用するツールの一覧と、使用する LLM, エージェントの種類を指定します
# ここで指定している "zero-shot-react-description" というエージェントは、ツールの説明のみに基づいて、どのツールを使用するかを決定してくれます
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

#エージェントにタスクを実行してもらいます
agent.run("昨日の東京の最高気温は何度でしたか？摂氏温度でお答え下さい。また、その数値を x としたとき、x^0.23 は何ですか？")