# 二次函数大厦

二次函数推导总图的全部文件。后续编辑、修改、生成都在本目录内进行。

## 目录

| 路径 | 内容 |
|---|---|
| `二次函数大厦-节点清单.md` | 节点清单（出图依据）：定位与受众、主题补充、分区与节点、入口、输出 |
| `生成/data.py` | 图的数据：节点、连线、题型入口、分区；三层——工具（TOOLS 工具箱、TOOL_SIGNALS 常用节点速查、TOOL_LABEL 线上引用工具的标签）、方法（METHODS 12 类）、题型入口里的工具与方向（ENTRY_HOW）；公式写 Unicode，由 `texify.py` 转成 MathJax |
| `生成/build.py` | 排版并写出 drawio，导出高清 PDF（矢量、单页；不再导出 PNG） |
| `生成/texify.py` | Unicode 数学式 → LaTeX（MathJax 显示） |
| `工具/check.py` | 自动检查：数据结构（连入、可达、▼、分区）与成图（重叠、分区、坐标引用、PDF 单页） |
| `工具/tiles.py` | 逐节点裁图拼成总览，查文字溢出、公式折行 |
| `工具/keep.py` | 只留指定节点及其连线，单独检查一条推导路径 |
| `工具/sync_list.py` | 按 `生成/data.py` 重写节点清单里的节点表、入口表和规模（改数据后运行） |
| `outputs/` | 成图 `quadratic-tree-v2.drawio` 与同名高清 `.pdf`。v2：参照不等式大厦的分区块排版（地基在上，各分区成块，跨块推导线走块间空隙） |
| `二次函数推导视频/` | 视频任务书（暂不制作，备用）；`_generator/gen.py` 从 `生成/data.py` 和成图生成 |

通用出图要求见 `数学/数学知识大厦-出图通用要求.md`。

## 工作流程

1. 先改 `二次函数大厦-节点清单.md`，确认后再动数据。
2. 按清单改 `生成/data.py`（排版、样式改 `生成/build.py`）。
3. 生成与检查（在本目录下运行）：

```bash
python3 生成/build.py v2                          # 写出 outputs/quadratic-tree-v2.drawio 和高清 .pdf
python3 工具/check.py outputs/quadratic-tree-v2.drawio
```

4. 放大检查：

```bash
python3 工具/tiles.py outputs/quadratic-tree-v2.drawio /tmp/tiles            # 全部节点
python3 工具/tiles.py outputs/quadratic-tree-v2.drawio /tmp/tiles R07,P09    # 指定节点
python3 工具/keep.py outputs/quadratic-tree-v2.drawio /tmp/路径.drawio S02,R01,R18,P02
drawio -x -f pdf --crop -o /tmp/路径.pdf /tmp/路径.drawio
```

5. 需要视频任务书时：`python3 二次函数推导视频/_generator/gen.py`（读 `outputs/quadratic-tree-v2.drawio` 的坐标；改版本号时同步改 gen.py 里的 `DRAWIO`）。

自动检查只说明结构没有问题，不能证明数学内容正确；知识点仍要按出图通用要求逐条核对。

## 依赖

- Python 3，`Pillow`（检查 PNG、裁图）
- Graphviz `dot`（排版）
- draw.io 桌面版命令行 `drawio`（导出 PDF）；`pdfinfo`（检查 PDF）
