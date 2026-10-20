# 恒等式大厦

恒等式推导总图的全部文件。后续编辑、修改、生成都在本目录内进行。

## 目录

| 路径 | 内容 |
|---|---|
| `恒等式大厦-设计.md` | 设计文档：范围、组织方式、条件三类、规范映射、三层（工具 / 方法 / 题型入口） |
| `恒等式大厦-节点清单.md` | 节点清单（出图依据）：节点、连线、用法层、题型入口、城市划分 |
| `恒等式素材-待单独成篇.md` | 最初从不等式大厦移出的恒等式素材 |
| `生成/data.py` | 图的数据：节点、连线、工具箱、方法箱 `METHODS`（13 种方法）、问题节点（公式写成 `$LaTeX$`） |
| `生成/steps.py` | 推导线一步一行的写法（照不等式大厦 v48）：每行【动作】+ 这一步的式子，工具写「工具名」；169 条推导线全覆盖，build.py 用它替换线上文字，`data.py` 里的原文不动 |
| `生成/build.py` | 排版并写出 drawio，导出 PNG |
| `工具/check.py` | 自动检查成图 |
| `工具/sub.py`、`工具/keep.py` | 截取局部区域、只留指定节点，用于放大检查 |
| `教材核对/` | 新教材七册逐章核对报告、老教材目录对照（v4 补充的依据） |
| `outputs/` | 成图 `identity-tree-v<版本>.drawio` 与同名成图；v1～v3 为 `.png`，v4 起只出矢量 `.pdf`（任意放大都清晰）。各版本都保留 |

## 修改规则：只增不删

原有的推导、条件、反例、用于、入口只能补充或修正；任何删除或改写，先列出来经用户确认。

## 工作流程

1. 先改 `恒等式大厦-节点清单.md`，确认后再动数据。
2. 按清单改 `生成/data.py`（排版、样式改 `生成/build.py`）。
3. 生成与检查（在本目录下运行）：

```bash
python3 生成/build.py v4                        # 写出 outputs/identity-tree-v4.drawio 和 .pdf
python3 工具/check.py outputs/identity-tree-v4.drawio
```

4. 放大检查局部：

```bash
python3 工具/sub.py outputs/identity-tree-v4.drawio /tmp/局部.drawio 0 0 3000 2000
python3 工具/keep.py outputs/identity-tree-v4.drawio /tmp/干道.drawio R01,R15,P49
/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -s 0.6 -o /tmp/局部.png /tmp/局部.drawio
```

## 依赖

- Python 3，`markdown-it-py`（检查清单表格用，可选），`Pillow`（检查 PNG）
- Graphviz `dot`（排版）
- draw.io 桌面版：v4 起导出矢量 PDF（`-x -f pdf --crop`，与不等式大厦相同），整图一页；check.py 检查是否单页。
- `pdfinfo`（poppler，check.py 读 PDF 页数、尺寸）
