# 🧪 化学/化工实验工作总结生成技能 (`/summary`)

[![HanaAgent Skill](https://img.shields.io/badge/HanaAgent-Skill-blue.svg)](https://github.com/liliMozi/openhanako)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)](https://www.python.org/)

面向化学、化工、制药及材料合成领域的智能实验工作总结与报告排版技能。支持从碎片化、口语化的实验流水账或图谱 PDF 报告中自动提炼高水准学术总结，并通过底层 Python 引擎一键导出排版规范的 Word (`.docx`) 文档。

---

## ✨ 核心特性

- 🎯 **斜杠命令与多场景触发**：输入 `/summary`、或直接发送实验操作记录、实验日报/周报即可唤醒。
- 📊 **图谱 PDF 自动无损提取**：支持自动解析液相色谱 (HPLC)、气相色谱 (GC-MS)、核磁共振 (NMR) 等 PDF 报告，以 **300 DPI 超清分辨率** 提取图谱并自动嵌入 Word 正文对应图号位置。
- 📝 **五大标准学术模块**：
  1. **实验目的**（条理化列出本周期核心技术问题与解决目标）
  2. **实验过程与结果分析**（子章节拆分、学术三线投料表、TLC 点板/色谱数据追踪、产率计算）
  3. **问题与现状分析**（副反应机理、低级失误学术化归因、液相未知峰排查、工艺现状）
  4. **最优反应/检测条件汇总**（标准化加氢、酰化、色谱等工艺参数）
  5. **下一步改进方案**（可落地的具体实验改进步骤）
- 📄 **严苛排版契约 (Word .docx)**：
  - **中英双字体分离**：中文统一为 **宋体 (SimSun)**，英文与数字统一为 **Times New Roman**。
  - **规范字号层级**：大标题小二（18pt）加粗居中、一级标题小三（15pt）加粗、二级标题四号（14pt）加粗、正文小四（12pt）两端对齐、图题/表题五号（10.5pt）居中。
  - **标准学术三线表**：顶底线 1.5 磅，栏目线 0.75 磅，表头加粗居中。
- 🔄 **两阶段安全交付流**：先在对话中生成 Markdown 草案供用户审阅确认；待用户明确同意（“同意”/“生成word”）后方触发底层文件导出。

---

## 🛠️ 目录结构

```text
summary/
├── SKILL.md                          # 技能元数据、触发指令与两阶段工作流定义
├── README.md                         # 项目使用说明
├── LICENSE                           # MIT 开源协议
├── .gitignore                        # Git 忽略配置
├── scripts/
│   ├── extract_pdf_images.py         # PDF 实验报告图谱提取与高清渲染脚本 (PyMuPDF)
│   └── generate_docx.py              # Word 文档双字体、三线表自动排版生成引擎 (python-docx)
└── references/
    ├── structure_template.md         # 五大模块学术化转换范例与对照表
    ├── styling_spec.md               # Word 排版样式与 XML 属性规范
    └── example_data.json             # 真实合成实验数据结构示例
```

---

## 📦 安装与在另一台电脑上使用

### 方式一：在 HanaAgent 中一键安装 (推荐)

在另一台电脑的 HanaAgent 聊天框中输入：

```text
帮我安装技能：https://github.com/TheEarlyWinter/summary
```

或者 Agent 会自动调用 `install_skill` 完成安装。

### 方式二：手动克隆到技能目录

```bash
cd ~/.hanako/skills
git clone https://github.com/TheEarlyWinter/summary.git summary
```

### 环境依赖

Python 环境需安装以下基础库：

```bash
pip install python-docx pymupdf pillow
```

---

## 💡 使用示例

### 1. 纯文字实验记录转周报 / 日报

在会话中输入 `/summary` 并粘贴你的原始实验操作记录：
> “前面做的加氢实验转化率效果不好，在乙酸乙酯体系里加入了10%的甲醇溶剂，液相产率可达93%...做了酰化反应，-5℃加入4%乙酸酐滴加...”

### 2. 配合图谱 PDF / 图片

直接将仪器的 HPLC 液相色谱 PDF 报告、TLC 点板照片拖入会话中，助手将自动提取图谱并插入到最终生成的 Word 文档中！

---

## 📄 License

[MIT License](LICENSE) © 2026 TheEarlyWinter
