---
name: skillhub-financial-business-icons
description: Find and reuse the user's 23 blue financial business icons from MasterGo file 205931991716288, covering performance, operations, A/H-share sentiment and funds, fund services, valuation, ETF arbitrage, compliance and investor relations. Use when the user requests this existing icon set for Skill Hub, MCP or financial business entry pages, adding or replacing these icons. Includes original SVGs and semantic lookup; does not define all XingZhi icons or authorize inventing missing icons.
---

# skillhub金融业务图标

这是用户选中的 23 枚业务图标资产技能。产品归属尚未明确；Skill Hub/MCP 是可用语境，不代表已确认全产品规范。原始画布为 60×60。不要套用其他图标体系的颜色、线宽或圆角。

## 按需使用

1. 按用户描述读取 [目录](references/catalog.md)，或运行 `python3 scripts/find_icon.py "港股资金面"`。查询可用中文名称、别名、业务词或节点 ID；自然语言需求先提取业务与市场限定词。再从 [机器索引](references/icon-index.json) 读取候选资产、原稿预览、实测属性。
2. 优先匹配业务、市场（A股/港股）、服务类型（查询MCP/分析）和具体名称。图形相似不能替代业务匹配；索引中的用途是检索建议，不代表业务授权或完整产品定义。
3. “A股资金面”唯一对应 `3:33` 钱袋；`3:069` 已更名为“市场每日复盘”，不得再使用旧名或旧关键词检索到它。“每日复盘” `3:120` 为双人造型，与日历造型的“市场每日复盘”分开匹配。仅说“复盘”时展示两项候选；按具体名称或造型确定。
4. 使用资产前读取 [视觉与复用规则](references/visual-rules.md)。21 项可复用完整 SVG；港股资金面、ETF套利监控是 SVG、文字及背景的组合，使用对应 composition 并连同 originals 目录复制。不要把组合中的单个局部 SVG 当成完整图标。
5. 原样使用默认尺寸、颜色及路径。用户指定其他尺寸时仅等比缩放整个60×60容器（含背景、文字、描边），不得只改外框造成组合错位。改变颜色、去背景、重画或添加状态属于衍生版本，只在本次用户明确要求时执行，保留原文件。
6. 找不到语义匹配时说明缺失；不要拿相似图案顶替，也不自行新建。用户另外明确要求扩展时，依据已证实特征设计，标注为新资产，不写成原始库图标。
7. 在目标环境预览并与索引中的原稿 PNG 对照，特别检查背景模糊、渐变、叠层、文字和裁切。浏览器渲染存在已知差异，详见视觉规则；不可声称 SVG 与原稿跨端像素一致。

## MasterGo 与来源

- 来源记录在 [原始节点数据](references/source-nodes.json) 和 [原始工具快照](references/mastergo-selection.md)。25 个原始 SVG 按 sha256 保持原字节。PNG 为视觉参考，不代替矢量原件。
- Skill 使用不意味着自动修改画布。用户要求修改已有图标时，先按精确节点读取当前快照，再遵循当前 MasterGo 工具路由；新页面请求走 design_page；图片替换按工具要求走 agent_replace_node。
- 不把旧节点ID、临时asset路径、原始snapshot中的data-node-id直接作为新页面目标。复制到新页面时删除旧节点身份，按当前工具生成/导入；已有节点修改则保留本次读取的真实身份。
- 页面工作可与相关页面 skill 配合；这里仅提供这一批图标，不能替代整个行知设计规范。

## 交付与检查

返回匹配的名称、节点ID、使用文件与必要的歧义说明。复用后确认资源路径有效、比例正确、状态没有编造。已验证的检索场景与限制见 [验证记录](references/validation.md)；未知项见 [待确认事项](references/open-questions.md)。
