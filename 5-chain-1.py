# llm ラッパーのインポート
from langchain.llms import AzureOpenAI
# プロンプトテンプレートのインポート
from langchain.prompts import PromptTemplate

# LLMChain に加えて SimpleSequentialChain もインポートする
# SimpleSequentialChain は、複数のチェーンを連続実行するためのチェーンで以下の特徴をもつ
# - 各ステップの入出力は一つ
# - 各ステップの出力が次のステップの入力になる
from langchain.chains import LLMChain, SimpleSequentialChain

# llm ラッパーの初期化
llm = AzureOpenAI(temperature=0, deployment_name="text-davinci-003")

# 最初のプロンプトテンプレートの作成
prompt_first = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)

# 最初に実行する LLM チェーンを定義
# 会社名を考えてもらう
chain_first = LLMChain(llm=llm, prompt=prompt_first)

# 次のプロンプトテンプレートの作成
prompt_second = PromptTemplate(
    input_variables=["company_name"],
    template="{company_name}という会社名の企業のキャッチコピーを考えてください。",
)

# 次に実行する LLM チェーンを定義
# キャッチコピーを考えてもらう
chain_second = LLMChain(llm=llm, prompt=prompt_second)

# 二つの LLM チェーンを連結
overall_chain = SimpleSequentialChain(chains=[chain_first, chain_second], verbose=True)

# 連結してできたチェーンを実行
catchphrase = overall_chain.run("カラフルな靴下")
print(catchphrase)