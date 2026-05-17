from __future__ import annotations

import json
import shutil
from pathlib import Path


WORKSPACE = Path("/Users/wuyuhang/Documents/New project/codex-for-legal-CN")
UPSTREAM = Path("/Users/wuyuhang/.codex/vendor/claude-for-legal-ZH")
CODEX_SKILLS = Path("/Users/wuyuhang/.codex/skills")
LOCAL_VENDOR = Path("/Users/wuyuhang/.codex/vendor/codex-for-legal-CN")

PLUGINS = [
    ("commercial-legal", "商事合同审查、交易文件、合同风险分层与业务化摘要"),
    ("privacy-legal", "个人信息保护、数据合规、影响评估、隐私协议审查"),
    ("product-legal", "产品上线、营销宣传、广告法与业务场景快问快答"),
    ("corporate-legal", "公司治理、并购交易、尽调、决议与交割清单"),
    ("employment-legal", "劳动用工、解除审查、规章制度、调查与跨省用工"),
    ("regulatory-legal", "监管动态、政策差距、征求意见稿与合规跟踪"),
    ("ai-governance-legal", "AI 治理、算法评估、科技伦理与 AI 供应商审查"),
    ("litigation-legal", "诉讼仲裁、案件管理、证据三性、大事记与文书草拟"),
    ("law-student", "法考、IRAC、案例摘要、知识体系与训练"),
    ("legal-clinic", "法律诊所接待、备忘录、检索路线图与节点管理"),
    ("legal-builder-hub", "法律技能发现、能力路由、工具选择"),
    ("ip-legal", "商标、专利、著作权、FTO、警告函与组合管理"),
]


def build_domain_skill(name: str, desc: str) -> str:
    return f"""---
name: {name}
description: {desc}。封装自本地安装的 codex-for-legal-CN / claude-for-legal-ZH。
---

# {name}

## 何时使用

- 用户任务与 `{name}` 领域直接相关
- 需要参考中国法工作方法、输出结构、清单和提示模板

## 本地来源

- 上游模块：`/Users/wuyuhang/.codex/vendor/claude-for-legal-ZH/{name}`
- 说明文档：`/Users/wuyuhang/.codex/vendor/claude-for-legal-ZH/{name}/README.md`
- 主提示：`/Users/wuyuhang/.codex/vendor/claude-for-legal-ZH/{name}/CLAUDE.md`

## 使用步骤

1. 先读该模块 README，确认边界。
2. 再读 CLAUDE，按它的输出框架做事。
3. 只加载当前任务必要的 references。
4. 法源与案例必须另行核验。
"""


def main() -> None:
    CODEX_SKILLS.mkdir(parents=True, exist_ok=True)
    LOCAL_VENDOR.parent.mkdir(parents=True, exist_ok=True)

    if not UPSTREAM.exists():
        raise SystemExit(f"missing upstream repo: {UPSTREAM}")
    if LOCAL_VENDOR.exists():
        raise SystemExit(f"destination exists: {LOCAL_VENDOR}")

    shutil.copytree(WORKSPACE, LOCAL_VENDOR)

    root_skill = (WORKSPACE / "templates/root-skill.md.tpl").read_text(encoding="utf-8")
    root_dir = CODEX_SKILLS / "codex-for-legal-cn"
    root_dir.mkdir(parents=True, exist_ok=True)
    (root_dir / "SKILL.md").write_text(root_skill, encoding="utf-8")

    registry = []
    for name, desc in PLUGINS:
        d = CODEX_SKILLS / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(build_domain_skill(name, desc), encoding="utf-8")
        registry.append({"name": name, "description": desc})

    (root_dir / "installed-modules.json").write_text(
        json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("installed root skill:", root_dir)


if __name__ == "__main__":
    main()
