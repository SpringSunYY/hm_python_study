import base64

# 读取音频文件
with open("D:/音乐/解锁/蝴蝶少女.flac", "rb") as audio_file:
    encoded_string = base64.b64encode(audio_file.read()).decode()

# 将 Base64 编码的内容写入 txt 文件
with open("encoded_audio.txt", "w") as output_file:
    output_file.write(encoded_string)

print("Base64 编码已写入 'encoded_audio.txt' 文件")
