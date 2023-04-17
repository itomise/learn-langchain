from langchain import OpenAI, ConversationChain

# LLM ラッパーを初期化します
llm = OpenAI(temperature=0)

# `ConversationChain` を初期化します
conversation = ConversationChain(llm=llm)

# ユーザーからの入力を受け付けます
command = input("You: ")

while True: 
  # ユーザーの入力を `ConversationChain` に渡して、AIの返答を取得します
  response = conversation.predict(input=command)
  print(f"AI: {response}")
  
  # 新しい入力を受け付けます
  command = input("You: ")

  # 入力が "exit" ならば、終了します
  if command == "exit":
    break