# 🎬 一人剧场 · AI短剧生成器

> **2026 AI先锋未来人才大赛** — 山海星辰命题参赛原型
> 赛道：一人剧组，爆款出海

## 这是什么

"HitLens"策略的技术验证原型。输入一句话故事灵感，AI自动生成短剧全链路制作方案，证明**"一人决策，AI执行"**可行性。

## 功能

| 功能 | 说明 |
|------|------|
| 📖 剧本方案 | 完整80-100集故事大纲 + 前3集剧本 + 角色设定 |
| 👤 角色设计 | 包含AI图像生成提示词的角色视觉描述 |
| 🎬 分镜设计 | 场景级分镜脚本 + 运镜建议 + 色彩基调 |
| 📊 市场分析 | 北美/东南亚/拉美三市场适配度评分 + 改编建议 |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env，填入 DeepSeek API Key
```

获取 API Key: [platform.deepseek.com](https://platform.deepseek.com)

### 3. 启动

```bash
streamlit run app.py
```

浏览器自动打开 `http://localhost:8501`

## 与竞赛方案的对应关系

| 原型功能 | 对应「HitLens」策略模块 |
|----------|------------------------|
| 输入故事 → 市场分析 | 模块一：IP解构与市场匹配 |
| 生成本土化剧本方案 | 模块二：文化转译引擎 |
| 角色+分镜+AI提示词 | 模块三：AI快速出片编排 |
| 市场适配度评分 | 模块四：多渠道小额测试（前置） |

## 技术栈

- **前端**: Streamlit
- **LLM**: DeepSeek Chat API
- **语言**: Python 3.10+

## 项目结构

```
ai-drama-generator/
├── app.py              # Streamlit 主应用
├── prompts.py           # Prompt 模板
├── requirements.txt     # Python 依赖
├── .env.example         # API Key 配置模板
├── docs/
│   └── 开题报告-山海星辰.md   # 完整开题报告
└── README.md
```
