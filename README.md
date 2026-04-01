# Token Burner

一个专门用于最大化消耗Claude API token的Python工具。

## 功能特性

### 5种消耗策略

1. **重复提问策略**: 使用超长文本反复提问相同问题
2. **上下文累积策略**: 不断累积对话历史，让每次请求都携带所有历史内容
3. **代码分析策略**: 提交大量代码要求详细分析和多版本重写
4. **多文档分析策略**: 同时提交多个长文档要求综合分析
5. **翻译链策略**: 在多种语言间反复翻译长文本

## 安装

```bash
cd token_burner
pip install -r requirements.txt
```

## 配置

设置环境变量:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

或在代码中直接传入API key。

## 使用方法

### 运行所有策略
```bash
python main.py
```

### 单独使用某个策略
```python
from main import TokenBurner

burner = TokenBurner()
burner.strategy_repetitive_questions(rounds=10)
```

## 工作原理

- 生成超长输入文本(每次3000-10000 tokens)
- 要求详细输出(max_tokens=8000)
- 累积对话上下文
- 重复执行多轮
- 实时统计token消耗

## 注意事项

⚠️ 此工具会产生大量API费用，请谨慎使用！

## 预估消耗

运行所有策略一次约消耗: 500,000+ tokens
