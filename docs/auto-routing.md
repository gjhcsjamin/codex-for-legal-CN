# 自动路由说明

`codex-for-legal-cn` 是总入口，不要求用户手动记忆指令。

## 设计原则

1. 先判断是不是法律工作
2. 再判断属于哪个领域
3. 最后读取对应模块的 README、CLAUDE、references

## 推荐路由

- 诉讼/仲裁/执行/保全/证据/文书起草 -> `litigation-legal`
- 合同审查/违约条款/谈判文本 -> `commercial-legal`
- 公司治理/股权/投资/尽调 -> `corporate-legal`
- 劳动用工/解除/规章制度 -> `employment-legal`
- 数据合规/个保法/隐私协议 -> `privacy-legal`
- 产品上线/营销宣传/业务场景快问快答 -> `product-legal`
- 监管追踪/政策差距/征求意见 -> `regulatory-legal`
- AI 合规/算法评估/科技伦理 -> `ai-governance-legal`
- 商标/专利/著作权/FTO/警告函 -> `ip-legal`

## 与法源核验的关系

路由只决定工作方法，不决定法律结论。

凡是引用：

- 法律
- 行政法规
- 司法解释
- 规范性文件
- 指导案例
- 裁判文书

都必须再走法源核验流程。
