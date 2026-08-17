# Word 文档排版规范 (Styling Spec)

本规范用于指导化学/化工实验工作总结 `.docx` 文档的自动化排版与样式渲染。

## 1. 字体规范 (双字体配置)
在 Word 中必须同时设置西文字体和中文字体：
- **中文字体 (EastAsia)**：`宋体` (SimSun)
- **西文字体 (ASCII / HAnsi / CS)**：`Times New Roman`

### XML 属性参考 (python-docx / oxml)
```python
from docx.oxml.ns import qn

def set_run_font(run, font_name_cn="宋体", font_name_en="Times New Roman", size_pt=12, bold=False, italic=False):
    run.font.name = font_name_en
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name_en}" w:hAnsi="{font_name_en}" w:eastAsia="{font_name_cn}" w:cs="{font_name_en}"/>')
        rPr.append(rFonts)
    else:
        rFonts.set(qn('w:ascii'), font_name_en)
        rFonts.set(qn('w:hAnsi'), font_name_en)
        rFonts.set(qn('w:eastAsia'), font_name_cn)
        rFonts.set(qn('w:cs'), font_name_en)
```

## 2. 层级与字号对照表

| 层级 / 元素 | 中文字体 | 西文字体 | 字号 (pt) | 中文字号名称 | 加粗 | 对齐方式 | 段前/段后间距 | 行距 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **文档大标题** | 宋体 | Times New Roman | 18 pt | 小二 | 是 | 居中 | 12 pt / 6 pt | 1.25 倍 |
| **一级标题** (一、二、) | 宋体 | Times New Roman | 15 pt | 小三 | 是 | 左对齐 | 8 pt / 4 pt | 1.25 倍 |
| **二级标题** (（一）、1.) | 宋体 | Times New Roman | 14 pt | 四号 | 是 | 左对齐 | 4 pt / 2 pt | 1.25 倍 |
| **三级标题** ((1)、a.) | 宋体 | Times New Roman | 12 pt | 小四 | 是 | 左对齐 | 2 pt / 2 pt | 1.25 倍 |
| **正文段落** | 宋体 | Times New Roman | 12 pt | 小四 | 否 | 两端对齐 | 0 pt / 2 pt | 1.25 倍 |
| **表格表头** | 宋体 | Times New Roman | 10.5 pt | 五号 | 是 | 居中 | 2 pt / 2 pt | 1.15 倍 |
| **表格内容** | 宋体 | Times New Roman | 10.5 pt | 五号 | 否 | 居中/居左 | 1 pt / 1 pt | 1.15 倍 |
| **图题 / 表题** | 宋体 | Times New Roman | 10.5 pt | 五号 | 否 | 居中 | 4 pt / 4 pt | 1.15 倍 |
| **图占位说明** | 宋体 | Times New Roman | 10.5 pt | 五号 | 否 (斜体) | 居中 | 4 pt / 4 pt | 1.15 倍 |

## 3. 表格样式 (标准学术三线表)
- **顶线 (Top border)**：1.5 磅 (`w:sz="12"`)
- **底线 (Bottom border)**：1.5 磅 (`w:sz="12"`)
- **栏目线 / 表头底线 (Header bottom)**：0.75 磅 (`w:sz="6"`)
- **内部横线 (Inside horizontal)**：无或 0.5 磅 (`w:val="none"`)
- **竖线 (Left/Right/Inside vertical)**：无 (`w:val="none"`)

## 4. 图片与图题处理规范
- 若存在真实图片文件（.png, .jpg 等）：插入图片并居中，限制宽度适应页面（最大宽度 14~15 cm）。
- 若无真实图片：生成居中文本框或灰色居中提示文字 `【图 X：图名称/说明】`。
- 图下方紧跟居中图题：`图 X 图名称`。
