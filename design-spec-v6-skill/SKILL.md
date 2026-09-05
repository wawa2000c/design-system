---
name: design-spec-v6
slug: design-spec-v6
display_name: wawa2000c 设计规范 v6（琥珀主色）
display_name_en: wawa2000c Design Spec v6 (Amber Primary)
description: |
  生成任何 HTML 页面、UI 组件、网页报告、看板、可视化、演示、文档排版等视觉产出物时，
  强制遵循 wawa2000c 设计规范 v6。核心风格：纸本美学 × Apple HIG × Material Design 3；
  琥珀主色 (#C67E2E) + 墨蓝辅色 (#4A7BB5) + paper-50 暖纸基底 (#FBF7F0，绝不用纯白)。
  包含完整 Design Tokens、组件库、间距/字体/图标/动效/响应式/深色模式规范，
  以及每产出必检的移动端 8 项清单。
version: 1.0.0
license: MIT
description_zh: 生成 HTML/UI 视觉产出物时强制遵循的 wawa2000c 设计规范 v6（纸本美学·琥珀主色·墨蓝辅色·paper-50 暖纸基底）
description_en: Mandatory design system v6 for all HTML/UI outputs (paper aesthetic, amber primary, ink-blue accent, paper-50 base)
visibility: public
agent_created: true
disable-model-invocation: false
---

# wawa2000c 设计规范 v6（琥珀主色）

## 定位

一份**强制遵循的视觉产出基线**。当你要生成任何网页类交付物（HTML 报告、看板、仪表盘、
组件、卡片、表单、弹窗、演示页、长文排版）时，先加载本规范，使所有产物在色彩、字体、
间距、组件、图标、动效、响应式、深色模式上保持统一、专业、有"纸本编辑"气质。

> **版本要点**：v6 把主色从「墨蓝」切换为「琥珀」，形成 **金纸合一**（琥珀主色 × paper-50 暖基底）
> 与 **纸上有墨**（墨蓝辅色提供冷静对比）的新体系。任何以"主色"填充的元素用琥珀，墨蓝退为辅色/冷静对比。

---

## 何时使用

- 用户要求生成 HTML 页面 / 网页报告 / 看板 / 仪表盘 / 可视化 / 演示
- 用户要求生成 UI 组件、卡片、表单、弹窗、按钮、徽章等
- 任何网页类视觉产出（含 Markdown 转网页、文档排版）
- 用户提到关键词：设计规范 / 纸本美学 / 琥珀 / paper-50 / 暖纸 / 墨蓝

**不要用它**：纯文本分析、不涉及视觉排版的对话、代码逻辑实现（除非该代码本身产出 UI）。

---

## 核心风格：纸本美学·编辑风格

- **根基**：纸本美学 × Apple HIG（清晰·顺从·深度）× Material Design 3
- **基底**：纸本美学暖纸色系，**绝不用纯白 `#FFFFFF`**，5 级纸色谱
- **字体**：标题衬线（Noto Serif SC）+ 正文无衬线（系统原生字体栈）
- **主色**：琥珀 `#C67E2E`（温暖金纸），辅色墨蓝 `#4A7BB5`（沉稳对比）
- **装饰**：三点横排 SVG ornament、细线分隔、留白节奏
- **作者署名**：wawa2000c

---

## Design Tokens 完整清单（直接复制进 `<style>`）

生成 HTML 时，把下面这段 `:root` 变量注入样式表，所有颜色/间距/字号统一用 `var(--xxx)`，
**禁止硬编码色值**（除非 token 未覆盖的罕见场景）。

```css
:root {
  /* Paper Spectrum — 背景基底 paper-50，逐级加深 */
  --paper-50:    #FBF7F0;   /* 全局背景、护眼基底（禁用纯白） */
  --paper-100:   #F4F0E6;   /* 卡片、面板、次要背景 */
  --paper-200:   #EDE8DB;   /* 边框、分隔线、次要边框 */
  --paper-300:   #DDD6C5;   /* 禁用态、hover 辅助 */
  --paper-400:   #D0C8B4;   /* 深色分割 */
  --paper-500:   #B8AE9A;   /* 极深背景辅助 */

  /* Ink Spectrum — 文字墨色，从深到浅 */
  --ink-900:     #2B2520;   /* 主标题、核心文字 */
  --ink-800:     #3D3631;
  --ink-700:     #5E5853;   /* 正文、导航、图标 */
  --ink-600:     #6E665F;
  --ink-500:     #8A837A;   /* 辅助文字、元数据 */
  --ink-300:     #AEA89F;   /* 禁用态 */
  --ink-100:     #DDD6C5;   /* 极浅辅助 */

  /* Primary: 琥珀 — 温暖金纸，主色（v6 核心变更） */
  --amber-900:   #7A4E1A;
  --amber-700:   #9A6820;   /* hover 态、深色文字 */
  --amber-500:   #C67E2E;   /* 主色、链接、按钮填充、核心操作 */
  --amber-300:   #D4A04E;
  --amber-200:   #E8C47A;   /* 背景、标签背景 */
  --amber-100:   #F5E0B0;
  --amber-50:    #FBF1E4;   /* 主题卡片背景、浅色填充 */

  /* Accent: 墨蓝 — 沉稳辅色，冷静对比（v6 退为辅色） */
  --blue-900:    #1A3A5C;
  --blue-700:    #355C8A;
  --blue-500:    #4A7BB5;   /* 辅色、次要操作、冷静对比 */
  --blue-300:    #7BA4CF;
  --blue-200:    #B8D0E8;
  --blue-100:    #D8E6F2;
  --blue-50:     #E8F0F8;   /* 辅色卡片背景 */

  /* Semantic */
  --crimson-500: #C44B4B;   /* 错误、危险、上涨（红涨） */
  --crimson-700: #9A3636;
  --crimson-100: #F0D0D0;
  --crimson-50:  #FBE8E8;
  --green-500:   #5B8C5A;   /* 成功、下跌（绿跌） */
  --green-700:   #3E6B3D;
  --green-100:   #D4EAD3;
  --green-50:    #EDF4EC;
  --orange-500:  #C88B3A;   /* 警告、提示 */

  /* Typography */
  --font-display: 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', Georgia, serif;
  --font-body:    -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-mono:    'SF Mono', 'JetBrains Mono', 'Menlo', 'Consolas', monospace;

  /* Dynamic Type 11 级 */
  --fs-caption2: 11px;  --fs-caption1: 12px;  --fs-footnote: 13px;
  --fs-subhead:  14px;  --fs-callout:  16px;  --fs-body:    16px;
  --fs-headline: 17px;  --fs-title3:   20px;  --fs-title2:  22px;
  --fs-title1:   28px;  --fs-large:    32px;

  /* Spacing — 4px 基础网格 */
  --sp-xxs: 4px;  --sp-xs: 8px;  --sp-sm: 12px;  --sp-md: 16px;
  --sp-lg: 24px;  --sp-xl: 32px;  --sp-xxl: 48px;  --sp-xxxl: 64px;

  /* Touch */
  --touch-min: 44px;

  /* Radius */
  --r-xs: 3px;  --r-sm: 6px;  --r-md: 10px;  --r-lg: 14px;  --r-xl: 20px;  --r-full: 9999px;

  /* Shadows — 暖色调阴影 */
  --sh-xs: 0 0 0 1px rgba(43,37,32,0.04), 0 1px 2px rgba(43,37,32,0.06);
  --sh-sm: 0 0 0 1px rgba(43,37,32,0.06), 0 2px 8px rgba(43,37,32,0.10);
  --sh-md: 0 0 0 1px rgba(43,37,32,0.06), 0 4px 16px rgba(43,37,32,0.14);
  --sh-lg: 0 0 0 1px rgba(43,37,32,0.06), 0 12px 36px rgba(43,37,32,0.18);

  /* Motion — iOS 弹簧曲线 */
  --spring-smooth:   cubic-bezier(0.25,0.1,0.25,1);
  --spring-ease-out: cubic-bezier(0,0,0.58,1);
  --spring-ease-in:  cubic-bezier(0.42,0,1,1);
  --spring-bouncy:   cubic-bezier(0.175,0.885,0.32,1.275);
  --dur-tap: 75ms;  --dur-micro: 150ms;  --dur-standard: 250ms;  --dur-reveal: 350ms;  --dur-page: 500ms;
}
```

### 深色模式覆盖（暖光阅读室）

深色模式模拟暖光阅读室：纸色基底变暖暗，墨色文字变暖浅。在 `:root` 之外加：

```css
[data-theme="dark"] {
  --paper-50: #2C241E; --paper-100: #342D26; --paper-200: #3D352D;
  --paper-300: #4A4036; --paper-400: #5C5044; --paper-500: #706358;
  --ink-900: #E5DFD3; --ink-700: #B8AE9A; --ink-500: #8A7E70;
  --amber-500: #E8C47A; --amber-200: #9A6820; --amber-50: #4A3520;
  --blue-500: #7BA4CF; --blue-200: #355C8A; --blue-50: #2A3540;
}
```

---

## 布局与容器

- **页面容器**：`max-width: 1120px`（列表/卡片类）/ `680px`（长文类），左右纸边 `20px`
- **多栏优先**：信息流/日报/卡片列表默认 `grid: repeat(2, 1fr)` 双栏，不要单列长卷轴
- **移动端**：≤768px 自动回退单列，≤480px 进一步收紧间距

---

## 字号阶梯（Dynamic Type 对齐）

- 正文基线 16px，最小不小于 14px
- 11 级语义：caption2(11) → caption1(12) → footnote(13) → subhead(14) → callout(16) → body(16) → headline(17) → title3(20) → title2(22) → title1(28) → largeTitle(32)
- 标题用 `--font-display`（衬线），正文用 `--font-body`（无衬线）

---

## 间距规范（正文与卡片/表格呼吸空间）

| 关系 | 间距 Token | 尺寸 | 说明 |
|------|-----------|------|------|
| section-desc → 内容块 | `--sp-lg` | 24px | 正文描述到卡片的呼吸空间 |
| h3 子标题 → 内容块 | `--sp-lg` | 24px | 标题到内容的节奏 |
| card-desc → 卡片内容 | `--sp-md` | 16px | 卡片内描述到内容的间距 |
| 内容块之间 | `--sp-xl` | 32px | 同一章节内不同区块之间 |
| 章节之间 | `--sp-xxxl` | 64px | 大章节分割 |

**间距只用 token**：统一用 `var(--sp-*)`，禁止裸像素混用；区块间距与字段内 label→控件间距分开管理。

---

## 组件库（在 paper-50 上）

### 按钮 · Buttons
| 类型 | 背景 | 边框 | 文字 |
|------|------|------|------|
| 主要 primary | `var(--amber-500)` | `var(--amber-700)` | white（hover→`var(--amber-700)`） |
| 次要 secondary | `var(--paper-100)` | `var(--paper-300)` → hover `var(--amber-200)` | `var(--amber-700)` |
| 辅色 accent | `var(--blue-500)` | `var(--blue-700)` | white |
| 危险 danger | `var(--crimson-500)` | `var(--crimson-700)` | white |
| 幽灵 ghost | transparent | `var(--paper-300)` | `var(--ink-700)` |

- 圆角 `--r-lg` (14px)，最小宽度 80px，高度 ≥44px；hover 加 `var(--sh-md)`

### 卡片 · Cards
- 背景 `var(--paper-100)`，边框 `1px solid var(--paper-200)`，圆角 `--r-lg` (14px)，内间距 `--sp-xl` (32px)
- hover：`var(--sh-md)` + `border var(--paper-300)`
- 琥珀主题卡片：`bg: var(--amber-50), border: var(--amber-200)`

### 输入框 · Inputs
- 背景 `var(--paper-50)`，边框 `1px solid var(--paper-300)`，圆角 `--r-md` (10px)，高度 44px
- focus：`border-color: var(--amber-500)`，阴影 `0 0 0 3px rgba(198,126,46,0.15)`
- 错误态：`border var(--crimson-500)`

### 开关 · Toggle
- OFF 轨道 `var(--paper-300)`；ON 轨道 `var(--amber-500)`（与琥珀主色一致）；旋钮 `var(--paper-50)`（不用纯白）

### 徽章 · Badges
- Primary：`bg: var(--amber-50), text: var(--amber-700)`
- Accent：`bg: var(--blue-50), text: var(--blue-700)`
- Danger：`bg: var(--crimson-50), text: var(--crimson-700)`；Success：`bg: var(--green-50), text: var(--green-700)`
- 圆角 `--r-full`，内间距 3px 8px

### 标签 · Tags
- 背景 `var(--paper-100)`，边框 `var(--paper-200)`，圆角 `--r-sm` (6px)，文字 `var(--ink-700)`
- hover：`border var(--amber-200), bg var(--amber-50), text var(--amber-700)`

### 进度条 · Progress
- 默认进度 `var(--amber-500)`；辅色进度 `var(--blue-500)`

---

## 图标体系

- **禁止使用 emoji**，全部使用手绘线稿风 SVG 图标
- 标准：`viewBox="0 0 24 24"`，`stroke-width="1.8"`，`stroke-linecap="round"`，`stroke-linejoin="round"`，`fill="none"`，`stroke="currentColor"`
- 尺寸梯度：sm(16) → md(24) → lg(32) → xl(40) → 2xl(56)
- 默认琥珀 `#C67E2E` 描边，若需继承文字色改 `stroke="currentColor"`

---

## 动效 · iOS 弹簧曲线

- 4 条曲线：`smooth (0.25,0.1,0.25,1)` / `ease-out (0,0,0.58,1)` / `ease-in (0.42,0,1,1)` / `bouncy (0.175,0.885,0.32,1.275)`
- 5 档时长：tap 75ms / micro 150ms / standard 250ms / reveal 350ms / page 500ms
- CSS 变量全继承，深色/浅色主题一键切换
- 金融数据：红涨绿跌（中国习惯）

---

## 响应式设计 · 三断点

| 断点 | 宽度 | 布局策略 |
|------|------|---------|
| ≥768px | 平板+桌面 | 双栏 Grid / 多栏自适应 / 纸边 20px |
| ≤768px | 大手机 | 单列堆叠 / 纸边 16px / 字号 ≥ 14px |
| ≤480px | 小手机 | 紧凑间距 / 纸边 12px / 标题降级 |

### 移动端必检清单（8 项硬性检查，每产出必查）

1. `<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">`
2. 三断点覆盖（≥768 / ≤768 / ≤480）
3. 字号 ≥ 14px（移动端全文最小）
4. 触控 ≥ 44px（所有交互元素最小区域）
5. 无水平溢出（`max-width:100%` + `overflow-x:hidden`）
6. 图片自适应（`max-width:100%; height:auto`）
7. 多栏 → 单列退降
8. Safe Area（`env(safe-area-inset-*)`，配合 `viewport-fit=cover`）

---

## 深色模式 · 暖光阅读室

- 浅色纸基底 `var(--paper-50)`；深色暖暗基底 `var(--d-paper-50)` #2C241E
- 墨色文字浅色化：d-ink-900 #E5DFD3 / d-ink-700 #B8AE9A / d-ink-500 #8A7E70
- 主色琥珀深色化：d-amber-500 #E8C47A / d-amber-200 #9A6820 / d-amber-50 #4A3520
- 辅色墨蓝深色化：d-blue-500 #7BA4CF / d-blue-200 #355C8A / d-blue-50 #2A3540
- 保持纸本美学的温度感，不要纯黑基底

---

## 平台适配 · iOS HIG × MD3

- **清晰 (Clarity)**：内容优先、装饰克制；paper-50 空背景、高对比文字、衬线标题
- **顺从 (Deference)**：内容主导、UI 辅助；无边框卡片、hover 才显 shadow、微动效
- **深度 (Depth)**：层级通过视觉传达；阴影分级 xs→lg、圆角分级、深色模式层次
- 8 维度选择：圆角分级 r-xs→r-xl / 温暖色调阴影 / 触控 44px / 11 级 Dynamic Type / 4 弹簧曲线 / 暖暗纸基底 / 手绘线稿 SVG / 4px 间距系统

---

## 反模式（禁止项）

- ❌ 纯白 `#FFFFFF` 作背景（必须用 `var(--paper-50)`）
- ❌ 墨蓝 `var(--blue-500)` 作主色填充（v6 起墨蓝仅作辅色/冷静对比）
- ❌ emoji 图标（必须手绘线稿 SVG）
- ❌ 硬编码色值、裸像素间距（用 `--token`）
- ❌ 单列长卷轴信息流（默认双栏）
- ❌ 移动端无 viewport / 无三断点 / 字号 < 14px / 触控 < 44px
- ❌ 内容紧贴无呼吸空间（遵循上方间距规范表）

---

## 快速自检（交付前过一遍）

- [ ] 背景是 `var(--paper-50)` 而非纯白
- [ ] 主色用琥珀 `var(--amber-500)`，墨蓝 `var(--blue-500)` 仅作辅色
- [ ] 标题衬线 + 正文无衬线，字号符合 Dynamic Type
- [ ] 所有间距用 `--sp-*` token，区块有呼吸空间
- [ ] 图标全是手绘线稿 SVG，无 emoji
- [ ] 移动端 8 项清单全过
- [ ] 含深色模式变量覆盖
- [ ] 作者署名 wawa2000c

---

*完整可视化版见 `design-spec-v6.html`（GitHub `wawa2000c/design-system`）。本 skill 为可操作基线，与 HTML 版同步。*
