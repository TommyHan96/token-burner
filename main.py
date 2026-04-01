#!/usr/bin/env python3
"""
Token Burner - 一个专门用于消耗大量token的工具
支持多种策略来最大化token消耗
支持��个主流大模型API
"""

import os
from typing import List, Dict
import time
from dotenv import load_dotenv
from model_adapter import get_adapter

# 加载.env文件中的环境变量
load_dotenv()


class TokenBurner:
    def __init__(self, provider: str = None):
        self.provider = provider or os.environ.get("MODEL_PROVIDER", "anthropic")
        self.adapter = get_adapter(self.provider)
        self.max_tokens = int(os.environ.get("MAX_TOKENS", "8000"))
        self.total_tokens = 0
        print(f"使用模型提供商: {self.provider}")

    def generate_long_text(self, length: int = 10000) -> str:
        """生成超长文本内容"""
        base = "这是一段用于消耗token的文本。" * 100
        return base * (length // len(base) + 1)

    def create_nested_context(self, depth: int = 50) -> str:
        """创建深度嵌套的上下文"""
        context = ""
        for i in range(depth):
            context += f"\n{'  ' * i}层级 {i}: " + "内容 " * 50
        return context

    def strategy_repetitive_questions(self, rounds: int = 10):
        """策略1: 重复提问相同问题"""
        question = self.generate_long_text(5000) + "\n请详细分析这段文本的每一个细节。"

        for i in range(rounds):
            print(f"\n=== 第 {i+1} 轮 ===")
            text, input_tokens, output_tokens = self.adapter.chat(
                messages=[{"role": "user", "content": question}],
                max_tokens=self.max_tokens
            )
            tokens = input_tokens + output_tokens
            self.total_tokens += tokens
            print(f"本轮消耗: {tokens} tokens (输入: {input_tokens}, 输出: {output_tokens})")
            print(f"累计消耗: {self.total_tokens} tokens")

    def strategy_context_accumulation(self, rounds: int = 20):
        """策略2: 上下文累积"""
        messages = []
        base_content = self.generate_long_text(3000)

        for i in range(rounds):
            messages.append({
                "role": "user",
                "content": f"第{i+1}轮: {base_content}\n请总结以上所有内容。"
            })

            text, input_tokens, output_tokens = self.adapter.chat(
                messages=messages,
                max_tokens=self.max_tokens
            )

            messages.append({
                "role": "assistant",
                "content": text
            })

            tokens = input_tokens + output_tokens
            self.total_tokens += tokens
            print(f"第 {i+1} 轮 - 消耗: {tokens} tokens, 累计: {self.total_tokens}")

    def strategy_code_analysis(self):
        """策略3: 复杂代码分析"""
        code = self.generate_complex_code()
        prompt = f"""
请对以下代码进行详细分析:
1. 逐行解释每一行代码的作用
2. 分析时间复杂度和空间复杂度
3. 提出至少20个优化建议
4. 重写代码并提供5个不同版本
5. 对比每个版本的优缺点

{code}
"""
        text, input_tokens, output_tokens = self.adapter.chat(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens
        )
        tokens = input_tokens + output_tokens
        self.total_tokens += tokens
        print(f"代码分析消耗: {tokens} tokens")

    def generate_complex_code(self) -> str:
        """生成复杂代码"""
        return '''
def complex_function(data):
    result = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            if data[i][j] > 0:
                temp.append(data[i][j] * 2)
            else:
                temp.append(data[i][j] / 2)
        result.append(temp)
    return result
''' * 50

    def strategy_multi_document_analysis(self):
        """策略4: 多文档分析"""
        documents = [self.generate_long_text(4000) for _ in range(5)]
        prompt = f"""
我有以下5个文档，请进行全面分析:

文档1: {documents[0]}
文档2: {documents[1]}
文档3: {documents[2]}
文档4: {documents[3]}
文档5: {documents[4]}

请:
1. 总结每个文档的核心内容
2. 找出文档之间的关联
3. 提取所有关键信息
4. 生成综合报告
"""
        text, input_tokens, output_tokens = self.adapter.chat(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens
        )
        tokens = input_tokens + output_tokens
        self.total_tokens += tokens
        print(f"多文档分析消耗: {tokens} tokens")

    def strategy_translation_chain(self, rounds: int = 10):
        """策略5: 翻译链"""
        text = self.generate_long_text(3000)
        languages = ["英语", "日语", "法语", "德语", "西班牙语", "中文"]

        for i in range(rounds):
            lang = languages[i % len(languages)]
            prompt = f"请将以下文本翻译成{lang}，并详细解释翻译过程:\n\n{text}"

            response_text, input_tokens, output_tokens = self.adapter.chat(
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.max_tokens
            )
            text = response_text
            tokens = input_tokens + output_tokens
            self.total_tokens += tokens
            print(f"翻译轮次 {i+1} 消耗: {tokens} tokens")

    def run_all_strategies(self):
        """运行所有策略"""
        print("开始Token消耗测试...\n")

        print("策略1: 重复提问")
        self.strategy_repetitive_questions(rounds=5)

        print("\n策略2: 上下文累积")
        self.strategy_context_accumulation(rounds=10)

        print("\n策略3: 代码分析")
        self.strategy_code_analysis()

        print("\n策略4: 多文档分析")
        self.strategy_multi_document_analysis()

        print("\n策略5: 翻译链")
        self.strategy_translation_chain(rounds=8)

        print(f"\n总计消耗: {self.total_tokens} tokens")


if __name__ == "__main__":
    burner = TokenBurner()
    burner.run_all_strategies()
