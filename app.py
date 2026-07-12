"""
AI Short Drama Generator — "一人剧场" 原型
Demonstrates the AI execution layer from the "HitLens" strategy.
One person + AI = complete short drama production pipeline.
"""

import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import (
    SYSTEM_PROMPT,
    script_generation_prompt,
    market_analysis_prompt,
)

load_dotenv()

st.set_page_config(
    page_title="一人剧场 · AI短剧生成器",
    page_icon="🎬",
    layout="wide",
)


@st.cache_resource
def get_client():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
    if not api_key:
        return None
    return OpenAI(api_key=api_key, base_url=base_url)


def call_deepseek(prompt: str):
    """Call DeepSeek API and stream response chunks."""
    client = get_client()
    if client is None:
        yield "❌ 未配置 DEEPSEEK_API_KEY。请在 .env 文件中设置 API Key。"
        return

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=4096,
            stream=True,
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"\n\n❌ API 调用失败：{str(e)}"


# --- UI ---
st.title("🎬 一人剧场 · AI短剧生成器")
st.caption("「HitLens」策略原型 — 一人决策，AI执行")

with st.sidebar:
    st.header("⚙️ 关于本工具")
    st.markdown("""
    **"HitLens"策略的技术验证原型。**

    输入一句故事灵感，AI自动生成：
    - 📖 完整剧本方案
    - 👤 角色设定与视觉描述
    - 🎬 分镜设计
    - 📊 海外市场分析

    **对应方案模块：**
    - IP解构与市场匹配
    - 文化转译引擎
    - AI快速出片编排

    ---
    """)

    api_status = "✅ 已连接" if get_client() else "⚠️ 未配置"
    st.info(f"DeepSeek API: {api_status}")

    if not get_client():
        st.code("""# 复制 .env.example 为 .env 并填入 Key
DEEPSEEK_API_KEY=sk-your-key-here""")

    st.divider()
    st.caption("2026 AI先锋未来人才大赛 · 山海星辰命题")

# --- Input ---
col1, col2 = st.columns([3, 1])
with col1:
    story_input = st.text_area(
        "✍️ 输入你的故事灵感（一句话）",
        placeholder="例如：霸道总裁爱上咖啡店打工妹，发现她是身价百亿的隐形富豪...",
        height=80,
    )
with col2:
    target_market = st.selectbox(
        "🎯 目标市场",
        ["多市场适配", "北美", "东南亚", "拉美", "日韩", "中东"],
    )

btn_col1, btn_col2 = st.columns([1, 3])
with btn_col1:
    gen_script = st.button("🚀 生成剧本方案", type="primary", use_container_width=True)
with btn_col2:
    gen_market = st.button("📊 仅分析市场", use_container_width=True)

# --- Results ---
if gen_script and story_input.strip():
    st.divider()
    st.header("📖 剧本生成中...")
    result_container = st.empty()
    full_response = ""

    for chunk in call_deepseek(script_generation_prompt(story_input, target_market)):
        full_response += chunk
        result_container.markdown(full_response + "▌")

    result_container.markdown(full_response)
    st.success("✅ 生成完成")
    st.download_button(
        label="📥 下载完整方案",
        data=full_response,
        file_name=f"短剧方案_{story_input[:15]}.md",
        mime="text/markdown",
    )

elif gen_market and story_input.strip():
    st.divider()
    st.header("📊 市场分析中...")
    result_container = st.empty()
    full_response = ""

    for chunk in call_deepseek(market_analysis_prompt(story_input)):
        full_response += chunk
        result_container.markdown(full_response + "▌")

    result_container.markdown(full_response)
    st.success("✅ 分析完成")

elif (gen_script or gen_market) and not story_input.strip():
    st.warning("⚠️ 请先输入故事灵感")

# --- Footer ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.85em;">
Built for <strong>2026 AI先锋未来人才大赛</strong> · 山海星辰命题<br>
原型展示"一人决策，AI执行"的核心策略理念
</div>
""", unsafe_allow_html=True)
