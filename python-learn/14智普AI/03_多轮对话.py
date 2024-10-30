from zhipuai import ZhipuAI

# 实例化ZhipuAI客户端
client = ZhipuAI(api_key="69df9fa65a23796fb7fd885784eb2457.eHw4dWQU1Z1XtLDI")  # 填写您自己的APIKey

# 存储对话历史
chat_history = []

while True:
    try:
        # 获取用户输入
        user_input = input("user: ")

        # 将用户消息添加到对话历史中
        user_message = {
            "role": "user",
            "content": user_input,
            "imageUrl": "",
            "videoUrlList": [],
            "fileContentList": []
        }
        chat_history.append(user_message)

        # 发送请求并获取响应
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=chat_history
        )

        # 获取并输出模型响应
        assistant_response = response.choices[0].message.content
        print("ZhipuAI:", assistant_response)

        # 将助手响应添加到对话历史中
        assistant_message = {
            "role": "assistant",
            "content": assistant_response,
            "imageUrl": "",
            "videoUrlList": [],
            "fileContentList": []
        }
        chat_history.append(assistant_message)

    except Exception as e:
        print("请求出错：", e)
