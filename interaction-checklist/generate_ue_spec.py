# -*- coding: utf-8 -*-
"""生成「交互设计自查规范.html」—— 基于原交互设计自查表增强优化，遵循纸本美学·编辑风格 v6。
模块图标取自 icon-library-v2.json（设计规范图标库）。
"""
import json

ICONS = {i["en"]: i["svg"] for i in json.load(open("icon-library-v2.json", encoding="utf-8"))["icons"]}

# 12 模块：name / icon(en) / principle(UE 导语) / items(检查点)
MODULES = [
    ("任务流程", "layers", "让用户顺畅抵达目标，每一步都可预期、可回退。",
     ["操作形成完整闭环，无中断、无死循环，用户始终知道「现在在哪、下一步去哪」",
      "关键操作可撤销 / 重置，随时可安全退出，不强迫用户提交",
      "长流程支持暂存（手动 / 自动），意外退出时提示保存，降低重做成本",
      "涉及权限或敏感操作时，不同角色走差异化流程，不套用同一模板",
      "有时限的操作明确倒计时与过期后果，不静默失效",
      "输入自动过滤空格 / 特殊字符、高危操作二次确认，把错误拦在提交前"]),
    ("框架布局", "layout", "结构清晰、信息有主次，导航即地图。",
     ["核心入口在拇指区 / 常驻区，层级不超过 3 层",
      "当前位置有标识，返回路径明确",
      "新增模块不破坏既有导航结构（可拓展）",
      "底部 Tab / 侧边栏 / 顶部栏的选择符合产品形态与用户习惯",
      "不同内容用差异化容器与间距区分类型",
      "关键信息与主操作视觉权重最高，不淹没在信息海",
      "长内容支持折叠 / 隐藏，超量时合理分页而非无限堆砌",
      "在合适节点给温度（鼓励 / 共情 / 彩蛋），降低机械感"]),
    ("页面交互", "refresh", "每一次状态变化都有反馈，等待不焦虑。",
     ["加载有品牌感的非阻塞动画，避免裸转圈",
      "弱网 / 关键路径提前预加载，减少空白等待",
      "加载失败明确原因，并提供一键重新加载入口",
      "自动 / 手动刷新方式明确，不静默偷偷刷新",
      "跨页 / 跨 Tab 是否刷新符合用户预期",
      "下拉刷新与点击刷新并存，反馈一致",
      "告知刷新了什么、刷新了多少，避免「刷新了个寂寞」",
      "转场 / 刷新有轻量动效缓冲，但提供关闭入口",
      "刷新结果（成功 / 失败 / 空）均有提示，不靠用户自己发现",
      "特殊页面（全屏 / 沉浸式）有清晰的进入与退出方式",
      "支持手势 / 快捷键快速往返，不必层层返回"]),
    ("页面元素", "text", "文案与元素为用户服务，不是为系统服务。",
     ["术语 / 格式 / 语气一致，不前后矛盾",
      "说人话，避免技术黑话与缩写",
      "一屏一重点，不堆长句",
      "在合适节点给温度（鼓励 / 共情 / 幽默）",
      "列表分页 / 无限滚动 / 步骤条的选择符合内容量与场景",
      "列表支持排序 / 筛选，默认排序与规则对用户可见",
      "图片支持大图 / 原图 / 缩放 / 保存，加载失败有占位与重试",
      "图片发送 / 编辑 / 删除的入口与边界清晰，误删可恢复"]),
    ("组件控件", "palette", "控件是用户与系统的契约，状态必须诚实可见。",
     ["按钮位置易触达且统一，主操作在视觉锚点",
      "按钮层级符合信息层级，主 / 次 / 文字按钮区分清楚",
      "按钮文案精准表达动作结果（「删除」而非「确定」）",
      "按钮默认 / 悬停 / 按下 / 禁用 / 加载态齐全且可辨",
      "点击有动效与结果反馈，符合预期不延迟",
      "操作前后状态与视觉变化匹配动作重要性（反馈强度）",
      "成功 / 失败 / 无数据 / 无权限均有明确文案与去向",
      "标签栏默认选项与数量合理，支持滑动 / 排序 / 组合",
      "特殊弹窗（活动 / 升级）有专属视觉但不喧宾夺主",
      "敏感 / 不可逆操作二次确认，不制造恐慌",
      "点击遮罩可关闭弹窗，不强制停留",
      "弹窗主操作突出、可取消，焦点管理正确",
      "区分不同 OS 的弹窗规范（iOS / Android / Web）",
      "输入框类型正确，调起对应键盘",
      "输入长度限制与计数可见，超长有提示",
      "输入方式（当前页 / 跳页、粘贴、换行、隐藏 / 语音）符合场景",
      "输入框默认值 / 预填值与非法输入指导清晰",
      "单选 / 复选有默认与必选规则，可清空 / 级联联动",
      "表单分步合理，长表单有进度",
      "表单标签与控件对应、对齐一致",
      "表单报错明显、定位准确、有消除方法",
      "报错提示强度（强 / 中 / 弱）匹配严重程度",
      "表单错误次数限制与超限处置明确"]),
    ("特殊场景", "alert", "异常环境不崩、不丢、不吓人。",
     ["横竖屏切换功能完整，不丢状态",
      "区分 iOS / Android，蓝牙 / GPS / 相机等权限申请时机合理、引导清晰",
      "夜间模式对比度与可读性达标，不刺眼",
      "WiFi 模式下自动下载 / 缓存策略明确，不偷跑流量",
      "沉浸（全屏）模式退出便捷，信息提示弱打断",
      "流量模式下耗费流量前提示或引导切 WiFi",
      "低电量模式减弱非必要动效与静默下载",
      "正常 / 弱网 / 无网 / 断网均有对应策略与自动恢复",
      "登录 / 未登录功能边界清晰",
      "未登录触发操作时平滑引导登录，不硬跳"]),
    ("跨端适配", "laptop", "同一产品，不同设备，一致体验。",
     ["断点适配（移动 / 平板 / 桌面），极端视口不溢出不塌陷",
      "长内容有合理的换行 / 滚动策略，不撑破布局",
      "鼠标与触控双支持，hover 态与 focus 态明确区分",
      "桌面端有 hover 预览，触屏有按压反馈",
      "全功能键盘可达，Tab 顺序符合视觉与逻辑",
      "可见焦点环，弹窗 / 抽屉焦点陷阱管理正确",
      "设定最小尺寸，缩放 / 最大化后布局与状态保持",
      "支持拖拽、右键菜单等桌面特有交互（如适用）",
      "页面切换或重开后保持状态（表单草稿、滚动位置、筛选条件）"]),
    ("无障碍设计", "user", "设计应服务所有人，包括临时与永久障碍者。",
     ["文字与背景对比度满足 WCAG AA（常规 4.5:1，大字 3:1）",
      "支持系统字体放大（至 200%）不破版、不遮挡关键信息",
      "所有交互元素可聚焦、可操作，焦点顺序符合逻辑",
      "语义标签 / ARIA 正确，读屏可理解元素顺序与状态变化",
      "尊重 prefers-reduced-motion，提供关闭动效入口",
      "可点击区域 ≥ 44×44px，间距避免误触",
      "图标 / 图片 / 图表有等效文本或 aria-label"]),
    ("数据可视化", "chart-bar", "让数据说话，但不说谎、不迷路。",
     ["图例、坐标轴、单位、精度标注明确，无歧义",
      "无数据时图表有占位说明，而非空白或报错",
      "极值 / 异常有标记与解释，不误导判断",
      "悬浮提示、下钻、筛选、缩放等行为符合预期",
      "数据刷新有指示，避免画面闪烁与数值跳变",
      "图表 / 数据可导出（图片 / CSV），权限与范围可控"]),
    ("状态体系", "info", "系统状态对用户透明，情绪稳定。",
     ["空结果有引导文案与操作入口，非纯空白",
      "错误有原因说明 + 解决路径（重试 / 返回），不暴露技术栈",
      "长加载用骨架屏 / 进度，短加载用局部反馈，不长时间白屏",
      "全局无网 / 弱网有明确提示与自动恢复机制",
      "Toast / Snackbar / 气泡等层级统一，不堆叠打扰"]),
    ("国际化", "globe", "让产品像本地人做的。",
     ["文案可配置替换，不硬编码在视图层",
      "RTL（右到左）语言适配，UI 镜像正确",
      "日期 / 数字 / 货币 / 时区按用户区域格式化",
      "长语言（德 / 俄等）文案不截断、不溢出、不换行破版"]),
    ("用户引导与留存", "rocket", "帮用户更快尝到甜头。",
     ["首次使用有明确指引（气泡 / 分步），可跳过且不频繁打扰",
      "新用户首屏有目标感与清晰的下一步动作",
      "注册 / 首次任务流程顺畅，降低中途放弃率",
      "关键操作有正反馈（成就 / 进度 / 激励），强化留存"]),
]

TODAY = "2026-07-06"

# ---------- 渲染 ----------
def mod_block(idx, name, icon_en, principle, items):
    svg = ICONS.get(icon_en, "")
    ic = '<span class="mod-ico">' + svg + '</span>'
    head = ('<header class="mod-head">'
            + ic
            + '<div class="mod-t"><h2>' + str(idx).zfill(2) + ' · ' + name + '</h2>'
            + '<p class="principle">' + principle + '</p></div>'
            + '<span class="mod-count" data-count="' + str(len(items)) + '">' + str(len(items)) + '</span>'
            + '</header>')
    its = []
    for it in items:
        its.append('<label class="item"><input type="checkbox"><span class="box"></span><span class="itext">' + it + '</span></label>')
    body = '<div class="items">' + ''.join(its) + '</div>'
    return '<section class="mod" id="m' + str(idx) + '">' + head + body + '</section>'

mods_html = ''.join(mod_block(i + 1, n, ic, p, its) for i, (n, ic, p, its) in enumerate(MODULES))
total = sum(len(m[3]) for m in MODULES)

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>交互设计自查规范 · 设计规范补充</title>
<style>
:root{
  --paper-50:#FBF7F0; --paper-100:#F4ECDD; --paper-200:#EADFC8; --paper-300:#E0D2B4; --paper-400:#D6C4A0;
  --ink:#2B2925; --ink-soft:#6B655C; --ink-faint:#9A938990;
  --amber:#C67E2E; --amber-soft:#E0A85C; --ink-blue:#4A7BB5;
  --line:#E0D2B4; --card:#FFFFFF; --radius:14px;
  --shadow:0 1px 2px rgba(43,41,37,.05),0 6px 20px rgba(43,41,37,.06);
  --sans:"Noto Sans SC",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;
  --serif:"Noto Serif SC",Georgia,"Songti SC",serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper-50);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased;overflow-x:hidden}
.wrap{max-width:1060px;margin:0 auto;padding:0 20px 96px}
/* header */
.hd{background:linear-gradient(180deg,var(--paper-100),var(--paper-50));border-bottom:1px solid var(--line);
  padding:56px 20px 40px;text-align:center}
.hd-in{max-width:760px;margin:0 auto}
.badge{display:inline-block;font-size:12px;letter-spacing:.14em;color:var(--amber);
  border:1px solid var(--amber-soft);border-radius:999px;padding:5px 14px;margin-bottom:18px}
.hd h1{font-family:var(--serif);font-size:32px;line-height:1.3;margin:0 0 12px;color:var(--ink)}
.hd .sub{color:var(--ink-soft);font-size:15px;margin:0}
.orn{display:flex;gap:7px;justify-content:center;margin:22px 0 0}
.orn i{width:7px;height:7px;border-radius:50%;background:var(--amber);display:block;opacity:.85}
.orn i:nth-child(2){background:var(--ink-blue);opacity:.7}
.orn i:nth-child(3){background:var(--paper-400)}
/* progress */
.prog{position:sticky;top:0;z-index:20;background:rgba(251,247,240,.92);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);padding:12px 20px}
.prog-in{max-width:1060px;margin:0 auto;display:flex;align-items:center;gap:14px}
.prog-bar{flex:1;height:8px;background:var(--paper-200);border-radius:999px;overflow:hidden}
.prog-fill{height:100%;width:0;background:linear-gradient(90deg,var(--amber),var(--amber-soft));
  border-radius:999px;transition:width .35s ease}
.prog-txt{font-size:13px;color:var(--ink-soft);white-space:nowrap;font-variant-numeric:tabular-nums}
/* intro */
.intro{max-width:760px;margin:34px auto 8px;color:var(--ink-soft);font-size:15px}
.intro b{color:var(--amber)}
/* module */
.mod{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);
  box-shadow:var(--shadow);padding:22px 24px;margin-top:18px}
.mod-head{display:flex;align-items:flex-start;gap:14px;padding-bottom:14px;border-bottom:1px dashed var(--line)}
.mod-ico{flex:0 0 auto;width:40px;height:40px;color:var(--amber);margin-top:2px}
.mod-ico svg{width:100%;height:100%}
.mod-t{flex:1}
.mod-t h2{font-family:var(--serif);font-size:20px;margin:0;color:var(--ink)}
.principle{margin:4px 0 0;font-size:13px;color:var(--ink-soft);line-height:1.55}
.mod-count{flex:0 0 auto;font-size:12px;color:var(--amber);background:var(--paper-100);
  border:1px solid var(--amber-soft);border-radius:999px;min-width:34px;height:24px;
  display:flex;align-items:center;justify-content:center;padding:0 8px;font-variant-numeric:tabular-nums}
.items{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;margin-top:16px}
.item{display:flex;align-items:flex-start;gap:10px;min-height:44px;padding:6px 4px;cursor:pointer;
  font-size:14px;line-height:1.55;color:var(--ink)}
.item input{position:absolute;opacity:0;width:0;height:0}
.box{flex:0 0 auto;width:20px;height:20px;margin-top:1px;border:1.6px solid var(--ink-faint);border-radius:6px;
  background:var(--paper-50);transition:all .18s ease;position:relative}
.item:hover .box{border-color:var(--amber)}
.item input:checked + .box{background:var(--amber);border-color:var(--amber)}
.item input:checked + .box::after{content:"";position:absolute;left:6px;top:2px;width:5px;height:10px;
  border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.item input:checked ~ .itext{color:var(--ink-soft);text-decoration:line-through;text-decoration-color:var(--amber-soft)}
.itext{flex:1}
/* footer */
.ft{text-align:center;color:var(--ink-faint);font-size:12px;margin-top:48px;line-height:1.8}
.ft .orn{margin-bottom:10px}
@media(max-width:768px){
  .items{grid-template-columns:1fr}
  .hd h1{font-size:26px}
  .wrap{padding:0 16px 80px}
  .mod{padding:18px 16px}
  .item{font-size:14px}
}
@media(max-width:480px){
  .hd{padding:40px 16px 30px}
  .hd h1{font-size:23px}
  .mod-ico{width:34px;height:34px}
  .mod-t h2{font-size:18px}
}
</style>
</head>
<body>
<header class="hd"><div class="hd-in">
  <span class="badge">设计规范 · 交互设计自查</span>
  <h1>交互设计自查规范</h1>
  <p class="sub">增强优化版 · 12 模块 / @TOTAL@ 检查点 · 以用户为中心（UE 精神）</p>
  <div class="orn"><i></i><i></i><i></i></div>
</div></header>

<div class="prog"><div class="prog-in">
  <div class="prog-bar"><div class="prog-fill" id="fill"></div></div>
  <div class="prog-txt" id="ptxt">已勾选 0 / @TOTAL@</div>
</div></div>

<main class="wrap">
  <p class="intro">本规范为「纸本美学·编辑风格 v6」设计体系的<b>交互设计自查补充</b>。未来所有界面 / 产品产出，应在交付前逐模块自检：状态是否诚实可见、异常是否不崩不丢不吓人、是否服务所有人。勾选即代表该项已满足。</p>
  @MODS@
  <footer class="ft">
    <div class="orn"><i></i><i></i><i></i></div>
    交互设计自查规范 · 基于原《交互设计自查表》增强优化<br>
    作者 wawa2000c · @TODAY@ · 设计规范补充（UE 准则）
  </footer>
</main>

<script>
var boxes=document.querySelectorAll('.item input');
var fill=document.getElementById('fill'),ptxt=document.getElementById('ptxt');
var total=boxes.length;
function upd(){var n=0;boxes.forEach(function(b){if(b.checked)n++;});
  fill.style.width=(total?n/total*100:0)+'%';
  ptxt.textContent='已勾选 '+n+' / '+total;}
boxes.forEach(function(b){b.addEventListener('change',upd);});
upd();
</script>
</body>
</html>"""

html = (TPL
        .replace("@TOTAL@", str(total))
        .replace("@MODS@", mods_html)
        .replace("@TODAY@", TODAY))

out = "交互设计自查规范.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("OK ->", out, "| modules:", len(MODULES), "| total:", total)
