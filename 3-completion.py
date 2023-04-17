# チャットモデルのラッパーをインポート
from langchain.chat_models import ChatOpenAI
# チャットモデルで利用可能なメッセージの型をインポート
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# チャットモデルのラッパーを初期化
chat = ChatOpenAI(temperature=0.7)

# チャットモデルに渡すメッセージを作成する
messages = [
    SystemMessage(content="あなたは親切なアシスタントです。"),
    HumanMessage(content="春の季語を絡めた冗談を教えてください。"),
    AIMessage(content="「春眠（しゅんみん）暁（ぎょう）を覚（さ）えず」という言葉がありますが、「春は眠くても、アシスタントは覚えてるよ！」と言って、ツッコミを入れるのはいかがでしょうか？笑"),
    HumanMessage(content="面白くない。もう一度。"),
]

# チャットモデルにメッセージを渡して、予測を受け取る
result = chat(messages)
print(result.content)