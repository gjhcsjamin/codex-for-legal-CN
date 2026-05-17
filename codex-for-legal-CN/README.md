# codex-for-legal-CN

面向中国律师与中国法务工作流的 Codex 技能封装。

这个仓库不是对原始 `CSlawyer1985/claude-for-legal-ZH` 的简单镜像，而是做了两层处理：

1. 保留原仓库作为上游参考与方法论来源。
2. 为 Codex 生成可识别、可自动路由的本地技能包装层。

## 目标

- 让 Codex 在中国法律工作场景中自动判断是否应进入法律工作流
- 按任务类型自动路由到诉讼、合同、公司、劳动、隐私、知识产权等模块
- 保留“现行有效核验优先”的工作规则，避免把提示词材料误当作法源

## 结构

- `scripts/install.py`：安装到本机 Codex 目录
- `templates/`：技能模板
- `docs/`：说明文档

## 安装后能力

- 总入口技能：`codex-for-legal-cn`
- 兼容入口技能：`claude-for-legal-zh`
- 领域技能：
  - `litigation-legal`
  - `commercial-legal`
  - `corporate-legal`
  - `employment-legal`
  - `privacy-legal`
  - `product-legal`
  - `regulatory-legal`
  - `ai-governance-legal`
  - `ip-legal`
  - `legal-clinic`
  - `law-student`
  - `legal-builder-hub`

## 自动识别规则

安装后不要求用户记命令。

当任务明显属于以下任一情形时，Codex 应自动使用 `codex-for-legal-cn` 总入口，再路由到具体模块：

- 诉讼、仲裁、再审、执行、保全、质证、代理词、答辩状、起诉状
- 合同审查、违约责任、补充协议、函件、交易结构
- 公司治理、股权、尽调、并购、董事会/股东会文件
- 劳动用工、解除、竞业限制、规章制度
- 隐私合规、个保法、数据出境、影响评估
- 知识产权、商标、专利、著作权、侵权警告函

## 重要限制

- 所有输出仅作为律师审查草稿
- 引用法律法规、司法解释、案例时，必须另行核验真实性与现行有效性
- 仓库中的方法论、提示词、清单不能替代法源本身
