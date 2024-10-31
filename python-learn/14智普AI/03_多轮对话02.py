# -*- coding: utf-8 -*-

from time import sleep
from zhipuai import ZhipuAI

url = "https://open.bigmodel.cn/api/paas/v4"
client = ZhipuAI(api_key="69df9fa65a23796fb7fd885784eb2457.eHw4dWQU1Z1XtLDI", base_url=url)
assistant_id = "65a265419d72d299a9230616a"
conversation_id= None
while True:
    # 获取用户输入
    user_input = input("user: ")
    generate = client.assistant.conversation(
        assistant_id="65a265419d72d299a9230616",
        conversation_id=conversation_id,
        model="glm-4-assistant",
        messages=[
            {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": user_input
                }]
            }
        ],
        stream=True,
        attachments=None,
        metadata=None
    )
    sleep(1)  # 调整 sleep 时间
    # 获取并输出模型响应
    # assistant_response = generate.choices[0].message.content
    # print("ZhipuAI:", generate.data.choices[0].message.content)
    # 累积 content 内容
    full_response = ""
    for resp in generate:
        if conversation_id is None:
            conversation_id = resp.conversation_id
        if resp.choices[0].delta.type == "content":
            full_response+=resp.choices[0].delta.content
        print(resp)
    print("ZhipuAI:", full_response)
