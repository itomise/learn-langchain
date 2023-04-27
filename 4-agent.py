from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI

# チャットモデルのラッパーを初期化
chat = AzureChatOpenAI(temperature=0.7, 
    deployment_name="gpt-35-turbo",
    openai_api_version="2023-03-15-preview"
)

# LLM ラッパーを初期化
llm = AzureOpenAI(temperature=0.7, deployment_name="text-davinci-003")

# ツールを導入します。 `llm-math` ツールを使うのに LLM を指定する必要があることに注意してください
tools = load_tools(["serpapi", "llm-math"], llm=llm)


# エージェントを初期化します
# 初期化時には、使用するツールの一覧と、使用する LLM, エージェントの種類を指定します
# ここで指定している "zero-shot-react-description" というエージェントは、ツールの説明のみに基づいて、どのツールを使用するかを決定してくれます
agent = initialize_agent(tools, chat, agent="chat-zero-shot-react-description", verbose=True)

#エージェントにタスクを実行してもらいます
agent.run("水卜アナウンサーの結婚相手は誰ですか？また、その人の年齢は何歳ですか？さらに、その値を x としたとき、x^0.23 は何ですか？")
