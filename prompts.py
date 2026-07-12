"""
Prompt templates for AI short drama generation.
All prompts are in Chinese for Chinese-market short drama production.
"""

SYSTEM_PROMPT = """你是一位资深的短剧编剧和制片人，拥有丰富的爆款短剧制作经验。
你擅长：
1. 设计高冲突、强情绪、快节奏的短剧剧本（80-100集体量）
2. 创造具有辨识度的角色人设
3. 设计吸引眼球的分镜和视觉表达
4. 分析不同海外市场的受众偏好

回复要求：
- 结构清晰，使用Markdown格式
- 内容具体可执行，不要空泛概念
- 每个角色、每场戏都要有明确的视觉化描述
- 考虑"黄金3秒"钩子设计——每集开头必须有强冲突或悬念"""


def script_generation_prompt(story_idea: str, target_market: str = "多市场适配") -> str:
    """Generate full short drama script from a one-sentence idea."""
    return f"""根据以下故事灵感，创作一部完整的短剧制作方案。

故事灵感：{story_idea}
目标市场：{target_market}

请按以下结构输出：

## 一、剧本定位
- 类型/题材
- 核心情绪钩子（3秒内抓住观众的点）
- 目标受众画像
- 总集数建议及每集时长

## 二、主要角色设定（3-5个）
每个角色包含：
- 姓名、年龄、身份
- 性格关键词（3个）
- 外貌特征（适合AI图像生成的描述）
- 核心欲望/冲突

## 三、故事大纲
- 第一幕（开局冲突，第1-15集）
- 第二幕（冲突升级，第16-50集）
- 第三幕（高潮反转，第51-80集）
- 第四幕（结局收官，第81-100集）

## 四、前3集完整剧本
每集包含：
- 场景描述（时间、地点、氛围）
- 人物对白（注明说话人）
- 情绪和节奏提示
- 结尾钩子（驱动下一集）

## 五、爆款要素分析
- 为什么这个剧本有爆款潜力
- 关键的情绪节奏设计
- 付费节点建议（在哪几集设置付费墙）"""


def character_visual_prompt(character_profile: str) -> str:
    """Generate visual description suitable for AI image generation."""
    return f"""为以下角色生成一段英文视觉描述（用于AI图像生成工具如即梦/可灵）：

角色信息：{character_profile}

要求：
- 风格：写实电影质感，符合短剧审美
- 格式：一段连续的英文描述，50-100词
- 包含：年龄、发型、面部特征、服装风格、表情、光线氛围
- 同时提供中文版本供参考"""


def storyboard_prompt(scene_description: str) -> str:
    """Generate detailed storyboard from a scene description."""
    return f"""为以下场景设计详细的分镜方案：

场景描述：{scene_description}

请按以下格式输出：

## 分镜脚本
| 镜号 | 景别 | 画面描述 | 运镜方式 | 对白/旁白 | 时长 |

同时提供：
- 每个镜头的色彩基调建议（暖/冷/中性）
- 关键帧的AI生成提示词（英文，适配即梦/可灵）
- 转场方式建议"""


def market_analysis_prompt(story_idea: str) -> str:
    """Analyze which overseas market fits the story best."""
    return f"""分析这个故事灵感在不同海外市场的适配度和爆款潜力。

故事灵感：{story_idea}

请按以下维度分析三个核心市场：

## 北美市场
- 适配度评分（1-10）
- 建议改编方向
- 对标成功案例
- 受众付费意愿

## 东南亚市场
- 适配度评分（1-10）
- 建议改编方向
- 对标成功案例
- 受众付费意愿

## 拉美市场
- 适配度评分（1-10）
- 建议改编方向
- 对标成功案例
- 受众付费意愿

## 综合建议
- 首选市场及理由
- 文化适配注意事项
- 预算分配建议"""
