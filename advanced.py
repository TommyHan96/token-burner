#!/usr/bin/env python3
"""
高级Token消耗策略
"""

from main import TokenBurner
import anthropic
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class AdvancedTokenBurner(TokenBurner):
    def strategy_vision_analysis(self):
        """策略6: 图像分析(如果有图像)"""
        prompt = """
请详细描述一个复杂的数据可视化场景:
1. 包含至少50个数据点
2. 多维度分析
3. 趋势预测
4. 异常检测
5. 详细的统计分析
""" + self.generate_long_text(4000)

        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        tokens = response.usage.input_tokens + response.usage.output_tokens
        self.total_tokens += tokens
        print(f"视觉分析消耗: {tokens} tokens")

    def strategy_reasoning_chain(self):
        """策略7: 推理链"""
        prompt = f"""
{self.generate_long_text(5000)}

基于以上信息，请进行深度推理:
1. 列出所有可能的假设(至少30个)
2. 对每个假设进行论证
3. 建立因果关系图
4. 进行反事实推理
5. 提供详细的逻辑链条
6. 分析每个推理步骤的置信度
"""
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        tokens = response.usage.input_tokens + response.usage.output_tokens
        self.total_tokens += tokens
        print(f"推理链消耗: {tokens} tokens")

    def strategy_creative_writing(self):
        """策略8: 创意写作"""
        prompt = f"""
{self.generate_long_text(3000)}

基于以上素材，请创作:
1. 一部10章的小说大纲，每章详细情节
2. 50个角色的详细背景
3. 世界观设定文档
4. 时间线梳理
5. 每个章节的详细对话
"""
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        tokens = response.usage.input_tokens + response.usage.output_tokens
        self.total_tokens += tokens
        print(f"创意写作消耗: {tokens} tokens")


if __name__ == "__main__":
    burner = AdvancedTokenBurner()
    burner.strategy_vision_analysis()
    burner.strategy_reasoning_chain()
    burner.strategy_creative_writing()
    print(f"\n高级策略总消耗: {burner.total_tokens} tokens")
