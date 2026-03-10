import arxiv
from datetime import datetime, timedelta, timezone
from openai import OpenAI
import os
import time

# ================= 配置区 =================
# 读取你在 GitHub Secrets 里存的 API KEY
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = "https://api.deepseek.com/v1"
MODEL_NAME = "deepseek-chat"
client_llm = OpenAI(api_key=API_KEY, base_url=BASE_URL)
# ==========================================

def fetch_qkd_papers(days_back=7):
    query = 'all:"quantum key distribution" OR all:QKD'
    start_date = datetime.now(timezone.utc) - timedelta(days=days_back)
    client = arxiv.Client()
    search = arxiv.Search(
        query=query, max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate, sort_order=arxiv.SortOrder.Descending
    )
    return [p for p in client.results(search) if p.published > start_date]

def translate_and_summarize(abstract_text):
    prompt = f"""
    你是一个专业的量子物理和量子密码学学术助手。处理这篇英文摘要：
    1. 翻译成流畅的中文（保持学术术语准确，如QKD、Decoy-state等）。
    2. 用一句话（加粗）高度概括核心创新点或结论。
    
    原文：{abstract_text}
    
    严格按此格式输出：
    **【中文摘要】**：
    [翻译内容]
    
    **【核心创新点】**：
    [一句话总结]
    """
    try:
        response = client_llm.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3, timeout=60
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"**【英文原文】** (AI分析失败): {abstract_text}"

if __name__ == "__main__":
    papers = fetch_qkd_papers(7)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"QKD_Report_{date_str}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        if not papers:
            f.write(f"# 📭 本周无 QKD 论文更新 ({date_str})\n\n本周 arXiv 上没有找到相关论文。")
        else:
            f.write(f"# 🔐 arXiv 每周追踪：量子密钥分发 (QKD)\n\n")
            f.write(f"> **生成日期:** {date_str} | **本周更新:** {len(papers)} 篇\n\n---\n\n")
            
            for i, paper in enumerate(papers, 1):
                authors = ", ".join([a.name for a in paper.authors])
                ai_analysis = translate_and_summarize(paper.summary.replace('\n', ' '))
                
                f.write(f"### {i}. {paper.title}\n\n")
                f.write(f"- **👨‍🔬 作者:** {authors}\n")
                f.write(f"- **📅 时间:** {paper.published.strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n")
                f.write(f"- **🔗 链接:** [arXiv 页面]({paper.entry_id}) | [PDF直达]({paper.pdf_url})\n\n")
                f.write(f"{ai_analysis}\n\n---\n\n")
                time.sleep(1) # 防封禁延迟
                
    print(f"✅ 成功！已生成文件：{filename}")
