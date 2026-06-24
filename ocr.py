import google.generativeai as genai
import sys
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro-latest')

prompt = """
请将我提供的历史文献图片转换成标准的 Markdown。
要求：
1. **严格留真**：必须完整保留原文中的所有特殊符号、音标、连字符、问号、星号以及脚注角标（例如：ě、ĕ、ê、ssŭ、*、¹、²、—、?、ṭ、ī 等），不得擅自简化或忽略。
2. **格式与换行**：包含表格部分和普通文本段落部分。如果单格内容在原文中存在换行或分层，请在 Markdown 中使用 `<br>` 标签换行。
3. **表格规范**：提取所有的表格内容，使用以下统一表头：
   `| 序号 | 中文 | Meaning (英文释义) | Sound Equivalent (汉字拟音) | Romanization (拟音罗马字) | Malay (马来语) |`
4. **语言对齐**：仔细辨识繁体印刷体汉字、外语罗马字和英文释义，确保列与列之间的对应关系完全正确。
5. **疑难字考证**：对于难以辨认或特殊的汉字（如异体字、变体、俗字），请在 Markdown 后面附上 `> **疑难字拆解与分析**` 的引用块，包含：
   - **逐笔构型拆解**
   - **辨析异体与变体**
   - **数字化建议**（包含 Unicode编码，宽式转录，严式转录，对音/语义逻辑）
   注意：只要发现生僻字、异体字或容易混淆的字（比如 剌、梹、蔞、垻 等），必须进行考证。
6. 如果图片中包含大段的英文段落或注释（例如脚注和解析），请作为普通的 Markdown 文本保留在表格下方。
"""

for i in range(11, 16):
    img_path = f"images_output/page_{i}.png"
    img = genai.upload_file(img_path)
    response = model.generate_content([prompt, img])
    with open(f"page_{i}_result.md", "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Processed page_{i}.png")
