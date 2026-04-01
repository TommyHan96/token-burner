# Token Burner

一个支持多个主流大模型API的Token消耗工具，可最大化消耗各平台的API token。纯属恶搞，代码没有运行过，后果自负。

## 支持的模型

| 提供商 | 模型 | 配置名称 |
|--------|------|----------|
| Anthropic | Claude Opus 4 | `anthropic` |
| OpenAI | GPT-4 Turbo | `openai` |
| Google | Gemini Pro | `google` |
| Cohere | Command | `cohere` |
| 百度 | 文心一言 ERNIE-Bot-4 | `baidu` |
| 阿里云 | 通义千问 Qwen-Max | `aliyun` |
| 智谱AI | ChatGLM-4 | `zhipu` |
| Moonshot | Kimi (128k) | `moonshot` |

## 功能特性

### 8种消耗策略

**基础策略 (main.py):**
1. **重复提问策略**: 使用超长文本反复提问相同问题
2. **上下文累积策略**: 不断累积对话历史，让每次请求都携带所有历史内容
3. **代码分析策略**: 提交大量代码要求详细分析和多版本重写
4. **多文档分析策略**: 同时提交多个长文档要求综合分析
5. **翻译链策略**: 在多种语言间反复翻译长文本

**高级策略 (advanced.py):**
6. **视觉分析策略**: 复杂数据可视化场景描述
7. **推理链策略**: 深度推理和多假设论证
8. **创意写作策略**: 长篇小说创作

## 安装

```bash
cd token_burner
pip install -r requirements.txt
```

## 配置

1. 复制配置模板:
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你要使用的模型API配置:

```bash
# 选择模型提供商
MODEL_PROVIDER=anthropic  # 可选: anthropic, openai, google, cohere, baidu, aliyun, zhipu, moonshot

# 填入对应的API Key
ANTHROPIC_API_KEY=your-key-here
# 或
OPENAI_API_KEY=your-key-here
# 或其他模型的配置...

# 通用配置
MAX_TOKENS=8000
```

## 使用方法

### 运行所有基础策略
```bash
python main.py
```

### 运行高级策略
```bash
python advanced.py
```

### 单独使用某个策略
```python
from main import TokenBurner

# 使用默认配置（从.env读取）
burner = TokenBurner()

# 或指定提供商
burner = TokenBurner(provider="openai")

# 运行特定策略
burner.strategy_repetitive_questions(rounds=10)
```

### 切换模型提供商
```python
# 方式1: 修改 .env 文件中的 MODEL_PROVIDER
# 方式2: 代码中指定
burner = TokenBurner(provider="google")
```

## 工作原理

- 生成超长输入文本(每次3000-10000 tokens)
- 要求详细输出(max_tokens=8000)
- 累积对话上下文
- 重复执行多轮
- 实时统计token消耗
- 统一的适配器接口支持多个模型

## 注意事项

⚠️ **此工具会产生大量API费用，请谨慎使用！**

- 不同模型的定价不同，请查看各平台的价格
- 建议先小规模测试（减少rounds参数）
- 注意API速率限制
- 某些模型可能不支持超长上下文
- 本项目由AI生成，纯属恶搞，本人不对任何行为的使用负任何责任

## 预估消耗

运行所有策略一次约消耗: **500,000+ tokens**

不同模型的费用参考（以Claude Opus 4为例）:
- 输入: $15/1M tokens
- 输出: $75/1M tokens
- 预估总费用: ~$30-50/次完整运行

## 项目结构

```
token_burner/
├── main.py              # 核心逻辑和基础策略
├── advanced.py          # 高级消耗策略
├── model_adapter.py     # 多模型适配器
├── requirements.txt     # 依赖包
├── .env.example         # 配置模板
└── README.md            # 说明文档
```
