from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate

# LLM チェーンをインポート
from langchain.chains import LLMChain

# LLM ラッパーを初期化
llm = AzureOpenAI(temperature=0.7, deployment_name="text-davinci-003")

# プロンプトテンプレートの作成
prompt = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)

# LLM チェーンを作成（LLM ラッパーとプロンプトテンプレートから構成する）
chain = LLMChain(llm=llm, prompt=prompt)

# LLM　チェーンを実行
prediction = chain.run("カラフルな靴下")
print(prediction.strip())