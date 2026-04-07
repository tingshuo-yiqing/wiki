import webbrowser
import random
import os

def open_daily_problem(file_path):
    try:
        # 1. 读取文件中的所有行
        if not os.path.exists(file_path):
            print(f"错误：找不到文件 {file_path}")
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            # 去掉每一行的空格和换行符，并过滤掉空行
            links = [line.strip() for line in f if line.strip()]

        if not links:
            print("文件是空的，没有找到任何链接。")
            return

        # 2. 随机抽取一个链接
        target_link = random.choice(links)
        
        print(f"今日抽取题目链接: {target_link}")

        # 3. 使用系统默认浏览器打开链接
        webbrowser.open(target_link)

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 这里填写你的 txt 文件路径
    file_name = "problems.txt" 
    open_daily_problem(file_name)