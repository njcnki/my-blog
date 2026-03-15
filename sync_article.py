import os
import sys
from datetime import datetime

# Simple tool to convert raw text to blog format
def convert_to_blog_post(raw_file, title, author="说不得", tags=None):
    if tags is None:
        tags = ["随笔"]
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    with open(raw_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Template
    md_content = f"""---
title: '{title}'
pubDate: '{date_str}'
description: '由公众号文章同步。'
author: '{author}'
tags: {tags}
---

{content}
"""
    
    # Save to blog folder
    output_filename = f"{title.replace(' ', '-').lower()}.md"
    output_path = os.path.join(os.path.expanduser('~'), 'Desktop/Douzi_Workspace/src/content/posts', output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"✅ Post created: {output_path}")

if __name__ == "__main__":
    # Usage example
    if len(sys.argv) < 2:
        print("Usage: python sync_article.py <title>")
    else:
        title = sys.argv[1]
        convert_to_blog_post('raw_content.txt', title)
