import os
from openai import OpenAI

def llm_answer(user_text,user_key):
    client = OpenAI(
        api_key=user_key,
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是一个把中文翻译成英文的大师，请你把我输入的中文文本翻译成英文文本."
            },
            {"role": "user", "content": user_text},
        ],
        stream=False
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    # 测试
    print(llm_answer("1大于2吗"))  # 应该输出英文回答
    print(llm_answer("今天的天气怎么样"))  # 应该输出英文回答