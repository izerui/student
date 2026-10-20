"""逐块导出 m_* 小块，测文字实际占的高度，写入 /tmp/mm/h.json（给 split_methods.py 用）。
用法：/tmp/venv/bin/python 工具/measure_blocks.py outputs/inequality-tree-v48.drawio   （需要 numpy、pillow）"""
import json, os, subprocess, sys
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image

D = '/Applications/draw.io.app/Contents/MacOS/draw.io'
F = sys.argv[1]
os.makedirs('/tmp/mm', exist_ok=True)
ids = [e.get('id') for e in ET.parse(F).getroot().find('.//root') if (e.get('id') or '').startswith('m_')]
res = {}
for i in ids:
    t = ET.parse(F); r = t.getroot().find('.//root')
    for e in list(r):
        if e.get('id') not in {'0', '1', i}:
            r.remove(e)
    g = r.find(f".//*[@id='{i}']").find('mxGeometry'); g.set('height', '900'); g.set('x', '0'); g.set('y', '0')
    t.write(f'/tmp/mm/{i}.drawio', encoding='utf-8', xml_declaration=True)
    subprocess.run([D, '-x', '-f', 'png', '-s', '1', '-o', f'/tmp/mm/{i}.png', f'/tmp/mm/{i}.drawio'], capture_output=True)
    a = np.asarray(Image.open(f'/tmp/mm/{i}.png').convert('L')).astype(int)
    inner = a[6:a.shape[0] - 40, 30:a.shape[1] - 30]       # 去掉边框和圆角
    rows = np.where((inner < 170).any(axis=1))[0]
    res[i] = int(rows.max() + 6 + 14) if len(rows) else 60
    print(i, res[i])
json.dump(res, open('/tmp/mm/h.json', 'w'))
