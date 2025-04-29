import requests

if __name__ == '__main__':
    # 定义请求的URL
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"

    # 定义请求头
    headers = {
        "Authorization": "Bearer NpqoXzRhGHtvzyoiQNFh:jfJNoiqPFeORDfBXiANv",  # 替换为您的API密码
        "Content-Type": "application/json"
    }

    # 定义请求体
    data = {
        "model": "lite",
        "user": "用户唯一id",
        "messages": [
            {
                "role": "system",
                "content": "你是知识渊博的助理"
            },
            {
                "role": "user",
                "content": "你好，讯飞星火"
            }
        ],
        # "stream": True
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, json=data, stream=True)
    print(response.text)
    # 输出响应内容
    print(f"Status Code: {response.status_code}")
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # 如果需要处理流式响应
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))
