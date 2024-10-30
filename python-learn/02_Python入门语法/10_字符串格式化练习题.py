from zhipuai import ZhipuAI

# 使用你的API密钥实例化客户端
client = ZhipuAI(api_key="69df9fa65a23796fb7fd885784eb2457.eHw4dWQU1Z1XtLDI")

# 调用API请求聊天生成健康报告
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[
        {
            "role": "system",
            "content": (
                "你是一个关于养老与养生的专家，深究智慧养老领域且认真负责，"
                "作为一个医生，我会你某一位老人的身体情况和一段时间数据，"
                "身体情况包括sex(性别)、age（年龄）、living_condition（居住情况）、"
                "disability_status（失能情况）、disability_condition（残疾情况）data(时间)，"
                "数据包括这段时间最大数据（max）、最低数据（lowe）、平均数据（avg），数据众数（mode）"
                "每种数据包括heartRate（心率）、dbp（低压）、sdp（高压）、oxygen（血氧）、"
                "bloodSugar（血糖）、str_temperature（温度）。你根据这些他的身体情况和数据认真且专业的分析数据"
                "在他这个年龄段是否正常，有什么潜在危险并给一些建议，建议在饮食饮食方面推荐吃什么食物，"
                "运动方面建议他做什么运动或者怎么调整身体，建议内容每种建议不少于两条且要根据他的身体情况做出更准确的建议，"
                "如果有较为严重的数据或者出现紧急情况，应该怎么做，并且总结生成一份健康报告，返回的内容为必须为Json，描述必须为中文。"
            )
        },
        {
            "role": "user",
            "content": (
                "{"
                "  \"name\": \"YY\","
                "  \"sex\": \"男\","
                "  \"age\": 76,"
                "  \"living_condition\": \"与配偶居住\","
                "  \"disability_status\": \"轻度\","
                "  \"disability_condition\": \"身体情况良好，不适合长跑，腿部有旧伤，不能跑步\","
                "  \"data\": \"2024-10-27\","
                "  \"avg\": {"
                "    \"heartRate\": 20,"
                "    \"dbp\": 60,"
                "    \"sdp\": 90,"
                "    \"oxygen\": 80,"
                "    \"bloodSugar\": \"7\","
                "    \"str_temperature\": \"37\""
                "  },"
                "  \"max\": {"
                "    \"heartRate\": 24,"
                "    \"dbp\": 65,"
                "    \"sdp\": 95,"
                "    \"oxygen\": 85,"
                "    \"bloodSugar\": \"9\","
                "    \"str_temperature\": \"37.5\""
                "  },"
                "  \"lower\": {"
                "    \"heartRate\": 18,"
                "    \"dbp\": 55,"
                "    \"sdp\": 85,"
                "    \"oxygen\": 75,"
                "    \"bloodSugar\": \"9\","
                "    \"str_temperature\": \"36.8\""
                "  },"
                "  \"mode\": {"
                "    \"heartRate\": 20,"
                "    \"dbp\": 59,"
                "    \"sdp\": 81,"
                "    \"oxygen\": 79,"
                "    \"bloodSugar\": \"7\","
                "    \"str_temperature\": \"37\""
                "  }"
                "}"
            )
        }
    ],
    top_p=0.7,
    temperature=0.5,
    max_tokens=2048,
    tools=[{"type": "web_search", "web_search": {"search_result": True}}],
    stream=True
)

# 输出响应内容
for chunk in response:
    print(chunk)
