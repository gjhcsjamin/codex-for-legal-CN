---
name: codex-for-legal-cn
description: 中国法律工作总入口技能。用于在律师、诉讼、合同、公司、劳动、隐私、知识产权等任务中自动识别并路由到对应法律模块。
---

# codex-for-legal-cn

## 何时使用

- 用户任务明显属于中国法律工作
- 需要先识别领域，再进入具体模块
- 用户没有明确说模块名称，但任务本身已经足够清楚

## 自动路由规则

- 诉讼、仲裁、执行、保全、再审、证据、代理词、答辩、起诉 -> `litigation-legal`
- 合同审查、补充协议、违约、函件、交易文本 -> `commercial-legal`
- 公司、股权、投资、尽调、并购、三会文件 -> `corporate-legal`
- 劳动、社保、解除、竞业、规章制度 -> `employment-legal`
- 隐私、个保法、数据、出境、影响评估 -> `privacy-legal`
- 产品上线、营销合规、广告法 -> `product-legal`
- 监管、合规追踪、政策变化 -> `regulatory-legal`
- AI 治理、算法、伦理审查 -> `ai-governance-legal`
- 商标、专利、著作权、侵权、FTO -> `ip-legal`

## 工作规则

1. 先判定任务是否属于法律工作流。
2. 再选择最匹配的领域模块。
3. 读取该模块 README、CLAUDE、references 的最小必要集合。
4. 如涉及具体法律依据、案例或时效规则，必须另行核验现行有效性与真实性。

## 本地来源

- 上游仓库：`/Users/wuyuhang/.codex/vendor/claude-for-legal-ZH`
- 兼容入口：`/Users/wuyuhang/.codex/skills/claude-for-legal-zh/SKILL.md`
