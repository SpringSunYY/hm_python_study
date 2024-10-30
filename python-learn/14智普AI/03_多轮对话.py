from zhipuai import ZhipuAI

client = ZhipuAI(api_key="69df9fa65a23796fb7fd885784eb2457.eHw4dWQU1Z1XtLDI")  # 填写您自己的APIKey
while True:
    prompt = input("user:")
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    answer = response.choices[0].message.content
    print("ZhipuAI:", answer)