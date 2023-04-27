# ドキュメントローダーをインポート
from langchain.document_loaders import TextLoader
from langchain.llms import AzureOpenAI
from pydantic import BaseModel, Extra, Field
from langchain.embeddings.openai import OpenAIEmbeddings
# ドキュメントローダーの初期化
loader = TextLoader(file_path='data/bocchan.txt', encoding='shift_jis')

# インデックスの作成に用いるクラスをインポート
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

# ベクターストアの作成
index: VectorStoreIndexWrapper = VectorstoreIndexCreator(
    embedding=OpenAIEmbeddings(chunk_size=1, embedding_ctx_length=6500)
    ).from_loaders([loader])

llm = AzureOpenAI(temperature=0, deployment_name="text-davinci-003")

query = "主人公の職業は？"
answer = index.query(query, llm=llm)

print(answer)