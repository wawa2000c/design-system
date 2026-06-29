# wawa2000c 设计规范 v6

> 纸本美学 × Apple HIG × Material Design 3  
> 基底: paper-50 #FBF7F0 — 护眼暖纸，绝非纯白  
> 主色: 琥珀 #C67E2E — 温暖金纸  
> 辅色: 墨蓝 #4A7BB5 — 沉稳对比  
> Author: wawa2000c | 2026.06.29

---

## S1 — 基底 · paper-50 护眼暖纸

全局背景色定于 **paper-50 #FBF7F0** — 温暖的米纸色，绝非纯白。所有色阶、墨色、主色均以此为基础协调搭配。

### 纸色谱 · Paper Spectrum

| Token | 色值 | 用途 |
|-------|------|------|
| paper-50 | `#FBF7F0` | 全局背景、护眼基底 |
| paper-100 | `#F4F0E6` | 卡片、面板、次要背景 |
| paper-200 | `#EDE8DB` | 边框、分隔线、次要边框 |
| paper-300 | `#DDD6C5` | 禁用态、hover态辅助 |
| paper-400 | `#D0C8B4` | 深色分割 |
| paper-500 | `#B8AE9A` | 极深背景辅助 |

### 墨色谱 · Ink Spectrum

与 paper-50 对比协调的文字色阶。

| Token | 色值 | 用途 | 对比度 (vs ink-900) |
|-------|------|------|-----|
| ink-900 | `#2B2520` | 主标题、核心文字 | — |
| ink-700 | `#5E5853` | 正文、导航、图标 | 5.2:1 ✓ |
| ink-500 | `#8A837A` | 辅助文字、元数据 | 3.1:1 ✗ (仅大文字) |
| ink-300 | `#AEA89F` | 禁用态 | 1.7:1 ✗ |
| ink-100 | `#DDD6C5` | 极浅辅助 | — |

---

## S2 — 色彩系统 · 与 paper-50 协调

### 琥珀 · Primary（主色）

温暖金纸——书页上的主角。与 paper-50 暖调天然合一，形成"金纸合一"的经典搭配。

| Token | 色值 | 用途 |
|-------|------|------|
| amber-500 | `#C67E2E` | 主色、链接、按钮填充、核心操作 |
| amber-700 | `#9A6820` | hover态、深色文字 |
| amber-900 | `#7A4E1A` | 极深、标题装饰 |
| amber-300 | `#D4A04E` | 次要、浅色填充 |
| amber-200 | `#E8C47A` | 背景、标签背景 |
| amber-100 | `#F5E0B0` | 极浅背景 |
| amber-50 | `#FBF1E4` | 主题卡片背景 |

### 墨蓝 · Accent（辅色）

沉稳辅色——油墨感的深蓝。为琥珀主色提供冷静对比，形成"纸上有墨"的层次感。

| Token | 色值 | 用途 |
|-------|------|------|
| blue-500 | `#4A7BB5` | 辅色、次要操作、冷静对比 |
| blue-700 | `#355C8A` | 辅色hover态 |
| blue-900 | `#1A3A5C` | 极深辅色 |
| blue-300 | `#7BA4CF` | 信息补充、数据标注 |
| blue-200 | `#B8D0E8` | 辅色标签背景 |
| blue-100 | `#D8E6F2` | 极浅蓝背景 |
| blue-50 | `#E8F0F8` | 辅色卡片背景 |

### 语义色 · Semantic

| Token | 色值 | 用途 |
|-------|------|------|
| crimson-500 | `#C44B4B` | 错误、危险、上涨（红涨） |
| crimson-700 | `#9A3636` | 深色错误态 |
| crimson-100 | `#F0D0D0` | 浅色错误背景 |
| crimson-50 | `#FBE8E8` | 极浅错误背景 |
| green-500 | `#5B8C5A` | 成功、下跌（绿跌） |
| green-700 | `#3E6B3D` | 深色成功态 |
| green-100 | `#D4EAD3` | 浅色成功背景 |
| green-50 | `#EDF4EC` | 极浅成功背景 |
| orange-500 | `#C88B3A` | 警告、提示 |

### 金融涨跌配色

中国市场习惯：**红涨绿跌**。朱红 `#C44B4B` 代表上涨，松绿 `#5B8C5A` 代表下跌。

---

## S3 — 字体排版 · Dynamic Type 11级

标题衬线（Noto Serif SC）+ 正文无衬线（系统字体栈）。字号对齐 iOS Dynamic Type 11级语义，基线 16px。

### 字号阶梯

| 语义名 | Token | 尺寸 | 用途 |
|--------|-------|------|------|
| caption2 | `--fs-caption2` | 11px | 极小标注、脚注编号 |
| caption1 | `--fs-caption1` | 12px | 小标注、标签 |
| footnote | `--fs-footnote` | 13px | 脚注、辅助说明 |
| subhead | `--fs-subhead` | 14px | 段落描述、次级文字 |
| callout | `--fs-callout` | 16px | 重点说明 |
| body | `--fs-body` | 16px | 正文基线 |
| headline | `--fs-headline` | 17px | 小标题 |
| title3 | `--fs-title3` | 20px | 三级标题 |
| title2 | `--fs-title2` | 22px | 二级标题 |
| title1 | `--fs-title1` | 28px | 一级标题 |
| largeTitle | `--fs-large` | 32px | 大标题、封面标题 |

### 字体栈

- **标题/衬线**: `'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', Georgia, serif`
- **正文/无衬线**: `-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', 'Microsoft YaHei', sans-serif`
- **代码/等宽**: `'SF Mono', 'JetBrains Mono', 'Menlo', 'Consolas', monospace`

---

## S4 — 间距 · 触控 · 网格

4px 基础网格，9级间距阶梯。iOS 44px 最小触控。页面容器分场景，双栏优先。

### 间距阶梯 · Spacing Scale

| Token | 尺寸 | 用途 |
|-------|------|------|
| `--sp-xxs` | 4px | 紧密内间距 |
| `--sp-xs` | 8px | 小间距 |
| `--sp-sm` | 12px | 中小间距 |
| `--sp-md` | 16px | 标准间距 |
| `--sp-lg` | 24px | 大间距（标题→内容） |
| `--sp-xl` | 32px | 特大间距（区块间距） |
| `--sp-xxl` | 48px | 超大间距 |
| `--sp-xxxl` | 64px | 最大间距（章节间距） |

### 触控区域 · Touch Targets

- 最小触控区域: **44×44px**（iOS 标准）
- 触控间距: ≥ 8px

### 页面容器 · Container Widths

| 场景 | 宽度 | 纸边 padding | 布局 |
|------|------|-------------|------|
| 列表/卡片 | 1120px | 20px | Grid 双栏 |
| 长文/详情 | 680px | 20px | 单栏 |

### 移动端断点

| 断点 | 宽度 | 布局策略 |
|------|------|---------|
| ≥768px | 平板+桌面 | 双栏 Grid / 多栏自适应 / 纸边 20px |
| ≤768px | 大手机 | 单列堆叠 / 纸边 16px / 字号 ≥ 14px |
| ≤480px | 小手机 | 紧凑间距 / 纸边 12px / 标题降级 |

---

## S5 — 组件库 · 在 paper-50 上

### 按钮 · Buttons

| 类型 | 背景 | 边框 | 文字 |
|------|------|------|------|
| 主要 primary | amber-500 | amber-700 | white |
| 次要 secondary | paper-100 | paper-300 → amber-200 | amber-700 |
| 辅色 accent | blue-500 | blue-700 | white |
| 危险 danger | crimson-500 | crimson-700 | white |
| 幽灵 ghost | transparent | paper-300 | ink-700 |

- 小按钮: `padding: sp-xs sp-md`, `font-size: fs-subhead`
- 大按钮: `padding: sp-md sp-xl`, `font-size: fs-callout`
- 圆角: `r-lg` (14px)
- 最小宽度: 80px
- hover: 加阴影 sh-md

### 卡片 · Cards

- 背景: `paper-100` (#F4F0E6)
- 边框: `1px solid paper-200`
- 圆角: `r-lg` (14px)
- 内间距: `sp-xl` (32px)
- hover: `shadow sh-md`, `border paper-300`
- 小卡片 (.card-sm): `padding: sp-md`, `radius: r-md`
- 琥珀主题卡片: `bg: amber-50, border: amber-200`

### 输入框 · Inputs

- 背景: `paper-50` (基底色)
- 边框: `1px solid paper-300`
- 圆角: `r-md` (10px)
- 高度: 44px (触控标准)
- focus: `border amber-500`, `shadow rgba(198,126,46,0.15)`
- 错误态: `border crimson-500`

### 开关 · Toggle

- OFF 轨道: `paper-300` (#DDD6C5)
- ON 轨道: `amber-500` (#C67E2E) — 与琥珀主色一致
- 旋钮: `paper-50` (#FBF7F0) — 不用纯白
- 尺寸: 轨道 44×24px, 旋钮 20px

### 徽章 · Badges

- Primary: `bg: amber-50, text: amber-700`
- Accent: `bg: blue-50, text: blue-700`
- Danger: `bg: crimson-50, text: crimson-700`
- Success: `bg: green-50, text: green-700`
- 圆角: `r-full` (9999px)
- 内间距: `3px 8px`

### 标签 · Tags

- 背景: `paper-100`
- 边框: `paper-200`
- 圆角: `r-sm` (6px)
- 文字: `ink-700`
- hover: `border amber-200, bg amber-50, text amber-700`

### 进度条 · Progress

- 默认进度: `bg: amber-500`
- 辅色进度: `bg: blue-500`

### 间距规范（正文与卡片/表格）

| 关系 | 间距 Token | 尺寸 | 说明 |
|------|-----------|------|------|
| section-desc → 内容块 | `--sp-lg` | 24px | 正文描述到卡片的呼吸空间 |
| h3 子标题 → 内容块 | `--sp-lg` | 24px | 标题到内容的节奏 |
| card-desc → 卡片内容 | `--sp-md` | 16px | 卡片内描述到内容的间距 |
| 内容块之间 | `--sp-xl` | 32px | 同一章节内不同区块之间 |
| 章节之间 | `--sp-xxxl` | 64px | 大章节分割 |

---

## S6 — 图标体系 · 手绘线稿 SVG

禁止 emoji。统一手绘线稿风格。

### 标准

| 属性 | 值 |
|------|-----|
| viewBox | `0 0 24 24` |
| stroke-width | `1.8` |
| stroke-linecap | `round` |
| stroke-linejoin | `round` |
| fill | `none` |
| stroke | `currentColor`（继承父元素颜色） |

### 尺寸梯度

| 级别 | 尺寸 | 用途 |
|------|------|------|
| sm | 16px | 内嵌标签、极小场景 |
| md | 24px | 标准导航、列表 |
| lg | 32px | 卡片标题、强调 |
| xl | 40px | 浮动按钮 |
| 2xl | 56px | 大型展示 |

---

## S7 — 动效 · iOS 弹簧曲线

4 条弹簧曲线 + 5 档时长。

### 弹簧曲线

| 名称 | cubic-bezier | 感觉 |
|------|-------------|------|
| smooth | `0.25, 0.1, 0.25, 1` | 丝滑顺畅 |
| ease-out | `0, 0, 0.58, 1` | 快出缓停 |
| ease-in | `0.42, 0, 1, 1` | 缓起快收 |
| bouncy | `0.175, 0.885, 0.32, 1.275` | 弹性回弹 |

### 时长档位

| 名称 | 毫秒 | 用途 |
|------|------|------|
| tap | 75ms | 点击反馈 |
| micro | 150ms | 微交互、hover |
| standard | 250ms | 常规过渡 |
| reveal | 350ms | 出现动画 |
| page | 500ms | 页面转场 |

---

## S8 — 响应式设计 · 三断点

### 移动端必配清单（8 项硬性检查）

1. `<meta viewport>` — width=device-width, initial-scale=1
2. 三断点覆盖 — ≥768 / ≤768 / ≤480
3. 字号 ≥ 14px — 移动端全文最小
4. 触控 ≥ 44px — 所有交互元素最小区域
5. 无水平溢出 — max-width:100% + overflow-x:hidden
6. 图片自适应 — max-width:100%; height:auto
7. 多栏 → 单列退降
8. Safe Area — env(safe-area-inset-*)

### CSS 模板

```css
/* ── 响应式断点 ── */
@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  .page-container { max-width: 100%; padding: 0 16px; }
}
@media (max-width: 480px) {
  body { font-size: 14px; }
  .page-container { padding: 0 12px; }
  h1 { font-size: 28px; }
  h2 { font-size: 22px; }
}
```

---

## S9 — 深色模式 · 暖光阅读室

深色模式模拟暖光阅读室氛围：纸色基底变为暖暗色，墨色文字变为暖浅色，保持纸本美学的温度感。

### 深色纸色谱

| Token | 色值 | 用途 |
|-------|------|------|
| d-paper-50 | `#2C241E` | 深色基底背景 |
| d-paper-100 | `#342D26` | 深色卡片背景 |
| d-paper-200 | `#3D352D` | 深色边框 |
| d-paper-300 | `#4A4036` | 深色禁用态 |
| d-paper-400 | `#5C5044` | 深色辅助 |
| d-paper-500 | `#706358` | 极深辅助 |

### 深色墨色谱

| Token | 色值 | 用途 |
|-------|------|------|
| d-ink-900 | `#E5DFD3` | 深色主文字 |
| d-ink-700 | `#B8AE9A` | 深色正文 |
| d-ink-500 | `#8A7E70` | 深色辅助文字 |

### 深色主色/辅色

| Token | 色值 | 用途 |
|-------|------|------|
| d-amber-500 | `#E8C47A` | 深色主色（琥珀） |
| d-amber-200 | `#9A6820` | 深色辅助琥珀 |
| d-amber-50 | `#4A3520` | 深色琥珀背景 |
| d-blue-500 | `#7BA4CF` | 深色辅色（墨蓝） |
| d-blue-200 | `#355C8A` | 深色辅助蓝 |
| d-blue-50 | `#2A3540` | 深色蓝背景 |

---

## S10 — 平台适配 · iOS HIG × MD3

### iOS HIG 三原则

| 原则 | 含义 | 规范体现 |
|------|------|---------|
| 清晰 (Clarity) | 内容优先，装饰克制 | paper-50 空背景、高对比文字、衬线标题 |
| 顺从 (Deference) | 内容主导，UI辅助 | 无边框卡片、hover才显shadow、微动效 |
| 深度 (Depth) | 层级通过视觉传达 | 阴影分级 xs→lg、圆角分级、深色模式层次 |

### 8 维度平台差异

| 维度 | iOS HIG | Material Design 3 | wawa2000c 选择 |
|------|---------|-------------------|---------------|
| 圆角 | 大圆角 (12-16px) | 按层级分级 | 分级 r-xs→r-xl |
| 阴影 | 极少阴影 | 层级阴影体系 | 温暖色调阴影 |
| 触控 | 44px | 48dp | 44px (iOS) |
| 字号 | Dynamic Type | M3 Type Scale | 11级 Dynamic Type |
| 动效 | 弹簧动画 | M3 Motion | 4弹簧曲线 |
| 深色 | 纯黑基底 | 灰色基底 | 暖暗纸基底 |
| 图标 | SF Symbols | Material Icons | 手绘线稿 SVG |
| 间距 | 8px 系统 | 4dp 系统 | 4px 系统 |

---

## CSS Design Tokens 完整清单

```css
:root {
  /* Paper Spectrum */
  --paper-50:    #FBF7F0;
  --paper-100:   #F4F0E6;
  --paper-200:   #EDE8DB;
  --paper-300:   #DDD6C5;
  --paper-400:   #D0C8B4;
  --paper-500:   #B8AE9A;

  /* Ink Spectrum */
  --ink-900:     #2B2520;
  --ink-700:     #5E5853;
  --ink-500:     #8A837A;
  --ink-300:     #AEA89F;
  --ink-100:     #DDD6C5;

  /* Primary: Amber — 温暖金纸，主色 */
  --amber-900:   #7A4E1A;
  --amber-700:   #9A6820;
  --amber-500:   #C67E2E;
  --amber-300:   #D4A04E;
  --amber-200:   #E8C47A;
  --amber-100:   #F5E0B0;
  --amber-50:    #FBF1E4;

  /* Accent: Blue — 沉稳辅色，冷静对比 */
  --blue-900:    #1A3A5C;
  --blue-700:    #355C8A;
  --blue-500:    #4A7BB5;
  --blue-300:    #7BA4CF;
  --blue-200:    #B8D0E8;
  --blue-100:    #D8E6F2;
  --blue-50:     #E8F0F8;

  /* Semantic */
  --crimson-500: #C44B4B;
  --crimson-700: #9A3636;
  --crimson-100: #F0D0D0;
  --crimson-50:  #FBE8E8;
  --green-500:   #5B8C5A;
  --green-700:   #3E6B3D;
  --green-100:   #D4EAD3;
  --green-50:    #EDF4EC;
  --orange-500:  #C88B3A;

  /* Typography */
  --font-display: 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', Georgia, serif;
  --font-body:    -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-mono:    'SF Mono', 'JetBrains Mono', 'Menlo', 'Consolas', monospace;

  /* Dynamic Type */
  --fs-caption2:  11px;
  --fs-caption1:  12px;
  --fs-footnote:  13px;
  --fs-subhead:   14px;
  --fs-callout:   16px;
  --fs-body:      16px;
  --fs-headline:  17px;
  --fs-title3:    20px;
  --fs-title2:    22px;
  --fs-title1:    28px;
  --fs-large:     32px;

  /* Spacing */
  --sp-xxs:   4px;
  --sp-xs:    8px;
  --sp-sm:    12px;
  --sp-md:    16px;
  --sp-lg:    24px;
  --sp-xl:    32px;
  --sp-xxl:   48px;
  --sp-xxxl:  64px;

  /* Touch */
  --touch-min: 44px;

  /* Radius */
  --r-xs:  3px;
  --r-sm:  6px;
  --r-md:  10px;
  --r-lg:  14px;
  --r-xl:  20px;
  --r-full: 9999px;

  /* Shadows */
  --sh-xs: 0 0 0 1px rgba(43,37,32,0.04), 0 1px 2px rgba(43,37,32,0.06);
  --sh-sm: 0 0 0 1px rgba(43,37,32,0.06), 0 2px 8px rgba(43,37,32,0.10);
  --sh-md: 0 0 0 1px rgba(43,37,32,0.06), 0 4px 16px rgba(43,37,32,0.14);
  --sh-lg: 0 0 0 1px rgba(43,37,32,0.06), 0 12px 36px rgba(43,37,32,0.18);

  /* Motion */
  --spring-smooth:    cubic-bezier(0.25,0.1,0.25,1);
  --spring-ease-out:  cubic-bezier(0,0,0.58,1);
  --spring-ease-in:   cubic-bezier(0.42,0,1,1);
  --spring-bouncy:    cubic-bezier(0.175,0.885,0.32,1.275);
  --dur-tap:      75ms;
  --dur-micro:    150ms;
  --dur-standard: 250ms;
  --dur-reveal:   350ms;
  --dur-page:     500ms;
}
```

---

## 间距规范规则（v5→v6 持续有效）

> 正文与卡片/表格之间必须有足够的呼吸空间，避免内容紧贴。

| CSS 类 | 间距 | 适用场景 |
|--------|------|---------|
| `.section-desc` | `margin-bottom: var(--sp-lg)` (24px) | 章节描述 → 首个卡片 |
| `.sub-heading` | `margin-bottom: var(--sp-lg)` (24px) | h3 子标题 → 内容块 |
| `.sub-desc` | `margin-bottom: var(--sp-lg)` (24px) | 子标题说明 → 内容 |
| `.card-desc` | `margin-bottom: var(--sp-md)` (16px) | 卡片描述 → 卡片内容 |
| `.content-block` | `margin-bottom: var(--sp-xl)` (32px) | 区块之间 |
| `.section` | `margin-bottom: var(--sp-xxxl)` (64px) | 大章节分割 |

---

## v6 变更记录

| 变更项 | v5 | v6 |
|--------|-----|-----|
| 主色角色 | 墨蓝 blue-500 (#4A7BB5) | **琥珀 amber-500 (#C67E2E)** |
| 辅色角色 | 琥珀 amber-500 (#C67E2E) | **墨蓝 blue-500 (#4A7BB5)** |
| 主色定位 | 沉稳信赖"墨纸对比" | **温暖金纸"金纸合一"** |
| 辅色定位 | 温暖点缀"书页金边" | **沉稳对比"纸上有墨"** |
| btn-primary | blue-500 填充 | **amber-500 填充** |
| badge-primary | blue-50/700 | **amber-50/700** |
| badge-accent | amber-50/700 | **blue-50/700** |
| toggle ON | blue-500 | **amber-500** |
| progress-fill | blue-500 | **amber-500** |
| input focus | blue-500 边框 | **amber-500 边框** |
| section-num | blue-500 透明度 | **amber-500 透明度** |
| nav active | blue-700/50 | **amber-700/50** |

---

*本文档为 wawa2000c 设计规范 Markdown 版，与 HTML 可视化版同步。  
如需查看交互式可视化效果，请打开 design-spec-v6.html。*
