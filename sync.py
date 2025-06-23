import requests
import os
from datetime import datetime

def fetch_source(url):
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        return response.text
    except:
        return ""

def merge_sources():
    output = []
    seen = set()
    
    with open("sources.txt", "r") as f:
        sources = f.read().splitlines()
    
    for url in sources:
        content = fetch_source(url)
        if content:
            for line in content.splitlines():
                line = line.strip()
                if line and not line.startswith("#") and line not in seen:
                    output.append(line)
                    seen.add(line)
    
    # 添加更新时间标记
    output.insert(0, f"# Auto-Updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    with open("live.txt", "w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    merge_sources()
