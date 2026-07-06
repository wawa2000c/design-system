# -*- coding: utf-8 -*-
"""
图标库生成器 · 全量 v2 (200 枚)
设计规范：纸本美学·编辑风格 (v6 琥珀主色版)
作者：wawa2000c
"""
import json, datetime, html

VERSION = "v2"
TOTAL_PLAN = 200

TOKENS = {
    "paper":   ["#FBF7F0", "#F4ECDD", "#E9DCC4", "#DCC9A8", "#CBB488"],
    "amber":   "#C67E2E",
    "inkblue": "#4A7BB5",
    "ink":     "#2B2B28",
}

# 20 大类 × 10 = 200
CATS = [
    ("general",   "通用界面",   "General UI"),
    ("media",     "文件与媒体", "Files & Media"),
    ("social",    "通讯与社交", "Communication"),
    ("nav",       "导航与方向", "Navigation"),
    ("time",      "时间与日历", "Time & Calendar"),
    ("biz",       "商业与数据", "Business & Data"),
    ("tools",     "编辑与工具", "Edit & Tools"),
    ("status",    "状态与提示", "Status & Alerts"),
    ("security",  "安全与隐私", "Security & Privacy"),
    ("device",    "设备与硬件", "Devices"),
    ("commerce",  "电商与支付", "Commerce & Payment"),
    ("map",       "位置与地图", "Location & Map"),
    ("weather",   "天气",       "Weather"),
    ("content",   "内容创作",   "Content & Creative"),
    ("health",    "医疗健康",   "Health & Medical"),
    ("food",      "餐饮美食",   "Food & Dining"),
    ("home",      "家居生活",   "Home & Life"),
    ("growth",    "增长运营",   "Growth & Ops"),
    ("transport", "交通出行",   "Transport"),
    ("nature",    "自然生物",   "Nature"),
]

def S(inner):
    return ("<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' "
            "viewBox='0 0 24 24' fill='none' stroke='currentColor' "
            "stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'>" +
            inner + "</svg>")

# ============ 通用界面 general (10) ============
general = [
    ("general","home","主页", S("<path d='M3 10.5 12 4l9 6.5'/><path d='M5 9.8V20h14V9.8'/><path d='M10 20v-6h4v6'/>")),
    ("general","search","搜索", S("<circle cx='11' cy='11' r='6.5'/><path d='M16 16l4.5 4.5'/>")),
    ("general","settings","设置", S("<circle cx='12' cy='12' r='3'/><path d='M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M16.9 16.9l2.1 2.1M19.1 4.9l-2.1 2.1M7.1 16.9l-2.1 2.1'/>")),
    ("general","user","用户", S("<circle cx='12' cy='8' r='3.5'/><path d='M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7'/>")),
    ("general","bell","通知", S("<path d='M5 18h14'/><path d='M6 9a6 6 0 0 1 12 0c0 4.5 1.5 6 2 7H4c.5-1 2-2.5 2-7Z'/><path d='M10 20.5a2 2 0 0 0 4 0'/>")),
    ("general","heart","收藏", S("<path d='M12 20.5C5 16 2.5 12 2.5 8.8 2.5 6.2 4.5 4.5 6.7 4.5c1.8 0 3.2 1 4.3 2.6C12 5.5 13.4 4.5 15.2 4.5c2.2 0 4.3 1.7 4.3 4.3 0 3.2-2.5 7.2-7.5 11.7Z'/>")),
    ("general","star","星标", S("<path d='M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 17l-5.2 2.6 1-5.8L3.5 9.7l5.9-.9z'/>")),
    ("general","menu","菜单", S("<path d='M4 7h16M4 12h16M4 17h16'/>")),
    ("general","grid","九宫格", S("<rect x='4' y='4' width='6' height='6' rx='1'/><rect x='14' y='4' width='6' height='6' rx='1'/><rect x='4' y='14' width='6' height='6' rx='1'/><rect x='14' y='14' width='6' height='6' rx='1'/>")),
    ("general","more","更多", S("<circle cx='6' cy='12' r='1.6'/><circle cx='12' cy='12' r='1.6'/><circle cx='18' cy='12' r='1.6'/>")),
]
# ============ 文件与媒体 media (10) ============
media = [
    ("media","file","文件", S("<path d='M6 3h8l4 4v14H6z'/><path d='M14 3v4h4'/>")),
    ("media","folder","文件夹", S("<path d='M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/>")),
    ("media","image","图片", S("<rect x='3' y='4' width='18' height='16' rx='2'/><circle cx='8.5' cy='9.5' r='1.8'/><path d='M4 17l5-4 4 3 3-2 4 3'/>")),
    ("media","document","文档", S("<rect x='5' y='3' width='14' height='18' rx='2'/><path d='M9 8h6M9 12h6M9 16h4'/>")),
    ("media","download","下载", S("<path d='M12 4v12'/><path d='M8 12l4 4 4-4'/><path d='M4 20h16'/>")),
    ("media","upload","上传", S("<path d='M12 16V4'/><path d='M8 8l4-4 4 4'/><path d='M4 20h16'/>")),
    ("media","clipboard","剪贴板", S("<rect x='5' y='4' width='14' height='17' rx='2'/><path d='M9 4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2'/><path d='M9 11h6M9 15h6'/>")),
    ("media","trash","删除", S("<path d='M4 7h16'/><path d='M9 7V4h6v3'/><path d='M6 7l1 13h10l1-13'/><path d='M10 11v6M14 11v6'/>")),
    ("media","audio","音频", S("<path d='M9 18V5l10-2v13'/><circle cx='6' cy='18' r='3'/><circle cx='16' cy='16' r='3'/>")),
    ("media","archive","压缩包", S("<path d='M3 8l2-3h14l2 3'/><rect x='3' y='8' width='18' height='12' rx='1.5'/><path d='M9 12v5M15 12v5'/>")),
]
# ============ 通讯与社交 social (10) ============
social = [
    ("social","mail","邮件", S("<rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3.5 6.5 12 13l8.5-6.5'/>")),
    ("social","message","消息", S("<path d='M5 5h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-4 3v-3H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z'/><path d='M8 10h8M8 13h5'/>")),
    ("social","phone","电话", S("<path d='M5 4h3l1.5 4.5L7 10a12 12 0 0 0 7 7l1.5-2.5L20 16v3a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1Z'/>")),
    ("social","video","视频", S("<rect x='3' y='6' width='13' height='12' rx='2'/><path d='M16 10l5-3v10l-5-3z'/>")),
    ("social","mic","麦克风", S("<rect x='9' y='3' width='6' height='11' rx='3'/><path d='M5 11a7 7 0 0 0 14 0'/><path d='M12 18v3'/>")),
    ("social","share","分享", S("<circle cx='6' cy='12' r='2.5'/><circle cx='18' cy='6' r='2.5'/><circle cx='18' cy='18' r='2.5'/><path d='M8.2 10.8 15.8 7.2M8.2 13.2l7.6 3.6'/>")),
    ("social","link","链接", S("<path d='M9 15l6-6'/><path d='M10.5 6.5 12 5a4 4 0 0 1 5.7 5.7l-1.5 1.5'/><path d='M13.5 17.5 12 19a4 4 0 0 1-5.7-5.7l1.5-1.5'/>")),
    ("social","wifi","无线", S("<path d='M3 8.5a13 13 0 0 1 18 0'/><path d='M6 12a8.5 8.5 0 0 1 12 0'/><path d='M9 15.5a4 4 0 0 1 6 0'/><path d='M12 19h.01'/>")),
    ("social","comment","评论", S("<path d='M5 5h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z'/><path d='M8 10h8M8 13h5'/>")),
    ("social","at","提及", S("<circle cx='12' cy='12' r='4'/><path d='M16 12v1.5a2.5 2.5 0 0 0 5 0V12a9 9 0 1 0-3.5 7.1'/>")),
]
# ============ 导航与方向 nav (10) ============
nav = [
    ("nav","arrow-right","右箭头", S("<path d='M4 12h15'/><path d='M13 6l6 6-6 6'/>")),
    ("nav","arrow-left","左箭头", S("<path d='M20 12H5'/><path d='M11 6l-6 6 6 6'/>")),
    ("nav","arrow-up","上箭头", S("<path d='M12 20V5'/><path d='M6 11l6-6 6 6'/>")),
    ("nav","arrow-down","下箭头", S("<path d='M12 4v15'/><path d='M6 13l6 6 6-6'/>")),
    ("nav","chevron-right","右chevron", S("<path d='M9 6l6 6-6 6'/>")),
    ("nav","chevron-down","下chevron", S("<path d='M6 9l6 6 6-6'/>")),
    ("nav","refresh","刷新", S("<path d='M20 12a8 8 0 1 1-3-6.2'/><path d='M20 5v4h-4'/>")),
    ("nav","external-link","外链", S("<path d='M14 4h6v6'/><path d='M20 4 10 14'/><path d='M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5'/>")),
    ("nav","chevron-left","左chevron", S("<path d='M15 6l-6 6 6 6'/>")),
    ("nav","chevron-up","上chevron", S("<path d='M6 15l6-6 6 6'/>")),
]
# ============ 时间与日历 time (10) ============
time = [
    ("time","calendar","日历", S("<rect x='3' y='5' width='18' height='16' rx='2'/><path d='M3 9h18M8 3v4M16 3v4'/>")),
    ("time","clock","时钟", S("<circle cx='12' cy='12' r='8'/><path d='M12 8v4l3 2'/>")),
    ("time","alarm","闹钟", S("<circle cx='12' cy='13' r='7'/><path d='M12 9v4l3 2'/><path d='M5 5 2.5 2.5M19 5l2.5-2.5'/>")),
    ("time","hourglass","沙漏", S("<path d='M6 4h12M6 20h12'/><path d='M7 4l5 7-5 7M17 4l-5 7 5 7'/>")),
    ("time","history","历史", S("<path d='M12 7v5l3.5 2'/><path d='M21 12a9 9 0 1 1-3-6.7'/><path d='M21 4v5h-5'/>")),
    ("time","timer","计时", S("<circle cx='12' cy='13' r='8'/><path d='M12 13V9'/><path d='M9 2h6'/><path d='M18.5 5.5 20 4'/>")),
    ("time","sun","太阳", S("<circle cx='12' cy='12' r='4'/><path d='M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M16.9 16.9l2.1 2.1M19.1 4.9l-2.1 2.1M7.1 16.9l-2.1 2.1'/>")),
    ("time","moon","月亮", S("<path d='M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5Z'/>")),
    ("time","week","周视图", S("<rect x='4' y='4' width='16' height='16' rx='2'/><path d='M4 9h16'/><path d='M9 4v16M14 4v16'/>")),
    ("time","event","日程", S("<rect x='3' y='5' width='18' height='16' rx='2'/><path d='M3 9h18M8 3v4M16 3v4'/><circle cx='12' cy='14' r='1.6'/>")),
]
# ============ 商业与数据 biz (10) ============
biz = [
    ("biz","chart-bar","柱状图", S("<path d='M4 20V4'/><path d='M4 20h16'/><path d='M8 20v-6M12 20v-10M16 20v-4'/>")),
    ("biz","chart-line","折线图", S("<path d='M4 4v16h16'/><path d='M7 14l3.5-4 3 2.5L20 7'/>")),
    ("biz","pie-chart","饼图", S("<circle cx='12' cy='12' r='9'/><path d='M12 3v9h9A9 9 0 0 0 12 3Z'/>")),
    ("biz","wallet","钱包", S("<path d='M4 8a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2v1h-13a2 2 0 0 0-2 2z'/><path d='M3 9v10a1 1 0 0 0 1 1h15a1 1 0 0 0 1-1v-3h-12a2 2 0 0 1-2-2z'/><circle cx='17' cy='14' r='1'/>")),
    ("biz","cart","购物车", S("<path d='M3 4h2l2.5 12h11L21 7H6'/><circle cx='9' cy='20' r='1.5'/><circle cx='17' cy='20' r='1.5'/>")),
    ("biz","tag","标签", S("<path d='M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z'/><circle cx='8' cy='8' r='1.6'/>")),
    ("biz","trending-up","增长", S("<path d='M3 17l6-6 4 4 8-8'/><path d='M15 7h6v6'/>")),
    ("biz","coins","金币", S("<ellipse cx='9' cy='7' rx='5' ry='2.3'/><path d='M4 7v5c0 1.3 2.2 2.3 5 2.3s5-1 5-2.3V7'/><path d='M4 12v5c0 1.3 2.2 2.3 5 2.3s5-1 5-2.3v-5'/>")),
    ("biz","building","楼宇", S("<rect x='5' y='3' width='14' height='18' rx='1'/><path d='M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2'/><path d='M10 21v-3h4v3'/>")),
    ("biz","briefcase","公文包", S("<rect x='3' y='7' width='18' height='12' rx='2'/><path d='M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2'/><path d='M3 12h18'/>")),
]
# ============ 编辑与工具 tools (10) ============
tools = [
    ("tools","edit","编辑", S("<path d='M4 20h4L19 9l-4-4L4 16z'/><path d='M14 6l4 4'/>")),
    ("tools","scissors","剪刀", S("<circle cx='6' cy='6' r='2.5'/><circle cx='6' cy='18' r='2.5'/><path d='M8 8 20 16M8 16 20 8'/>")),
    ("tools","filter","筛选", S("<path d='M4 5h16l-6 7v6l-4 2v-8z'/>")),
    ("tools","eye","查看", S("<path d='M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z'/><circle cx='12' cy='12' r='2.5'/>")),
    ("tools","lock","锁定", S("<rect x='5' y='10' width='14' height='10' rx='2'/><path d='M8 10V7a4 4 0 0 1 8 0v3'/>")),
    ("tools","unlock","解锁", S("<rect x='5' y='10' width='14' height='10' rx='2'/><path d='M8 10V7a4 4 0 0 1 7.5-2'/>")),
    ("tools","bookmark","书签", S("<path d='M6 3h12a1 1 0 0 1 1 1v17l-7-4-7 4V4a1 1 0 0 1 1-1z'/>")),
    ("tools","layers","图层", S("<path d='M12 3 3 8l9 5 9-5z'/><path d='M3 13l9 5 9-5'/>")),
    ("tools","crop","裁剪", S("<path d='M6 2v14a2 2 0 0 0 2 2h14'/><path d='M2 6h14a2 2 0 0 1 2 2v14'/>")),
    ("tools","palette","调色", S("<path d='M12 3a9 9 0 1 0 0 18c1.5 0 2-1 2-2s-1-1.5-1-2.5.5-1.5 2-1.5h2a3 3 0 0 0 3-3 9 9 0 0 0-9-9Z'/><circle cx='7.5' cy='10.5' r='1'/><circle cx='12' cy='7.5' r='1'/><circle cx='16.5' cy='10.5' r='1'/>")),
]
# ============ 状态与提示 status (10) ============
status = [
    ("status","check","完成", S("<path d='M5 12.5 10 17.5 19.5 6.5'/>")),
    ("status","close","关闭", S("<path d='M6 6l12 12M18 6 6 18'/>")),
    ("status","alert","警告", S("<path d='M12 4 2.5 20h19z'/><path d='M12 10v4'/><path d='M12 17h.01'/>")),
    ("status","info","信息", S("<circle cx='12' cy='12' r='9'/><path d='M12 11v5'/><path d='M12 8h.01'/>")),
    ("status","plus","添加", S("<path d='M12 5v14M5 12h14'/>")),
    ("status","minus","减少", S("<path d='M5 12h14'/>")),
    ("status","help","帮助", S("<circle cx='12' cy='12' r='9'/><path d='M9.5 9.5a2.5 2.5 0 0 1 4.5 1.5c0 1.5-2 2-2 3.5'/><path d='M12 17h.01'/>")),
    ("status","flag","标记", S("<path d='M6 21V4'/><path d='M6 4h12l-3 4 3 4H6'/>")),
    ("status","loading","加载", S("<path d='M12 3a9 9 0 1 0 9 9'/><circle cx='12' cy='3' r='1'/>")),
    ("status","mute","静音", S("<path d='M4 9v6h4l5 4V5L8 9z'/><path d='M17 9l4 6M21 9l-4 6'/>")),
]
# ============ 安全与隐私 security (10) ============
security = [
    ("security","shield","盾牌", S("<path d='M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z'/>")),
    ("security","key","钥匙", S("<circle cx='8' cy='8' r='4'/><path d='M11 11l8 8M16 16l2-2M18 18l2-2'/>")),
    ("security","fingerprint","指纹", S("<path d='M5 12a7 7 0 0 1 14 0'/><path d='M7 12a5 5 0 0 1 10 0c0 1 .3 2 .8 3'/><path d='M9.5 12a2.5 2.5 0 0 1 5 0c0 2-.5 3.5-1 5'/><path d='M12 11.5v4.5'/>")),
    ("security","eye-off","隐藏", S("<path d='M3 3l18 18'/><path d='M10.5 6.5A9.7 9.7 0 0 1 12 6c6.5 0 10 6 10 6a17 17 0 0 1-3.3 3.8'/><path d='M6.5 8.5A17 17 0 0 0 2 12s3.5 6 10 6a9.6 9.6 0 0 0 3-.5'/>")),
    ("security","ban","禁止", S("<circle cx='12' cy='12' r='9'/><path d='M6 6l12 12'/>")),
    ("security","shield-check","防护", S("<path d='M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z'/><path d='M9 12l2 2 4-4'/>")),
    ("security","certificate","证书", S("<rect x='4' y='4' width='16' height='13' rx='2'/><path d='M8 9h8M8 12h5'/><circle cx='17' cy='17' r='3'/><path d='M17 14v6'/>")),
    ("security","password","密码", S("<rect x='4' y='9' width='16' height='6' rx='3'/><path d='M8 12h.01M12 12h.01M16 12h.01'/>")),
    ("security","privacy","隐私", S("<path d='M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z'/><path d='M9 12s1.5-2.5 3-2.5S15 12 15 12s-1.5 2.5-3 2.5S9 12 9 12Z'/>")),
    ("security","verified","认证", S("<path d='M12 3l2.2 1.6 2.7-.2 1 2.5 2.2 1.6-1 2.5 1 2.5-2.2 1.6-1 2.5-2.7-.2L12 21l-2.2-1.6-2.7.2-1-2.5L3.9 15l1-2.5-1-2.5 2.2-1.6 1-2.5 2.7.2z'/><path d='M9 12l2 2 4-4'/>")),
]
# ============ 设备与硬件 device (10) ============
device = [
    ("device","monitor","显示器", S("<rect x='3' y='4' width='18' height='12' rx='2'/><path d='M9 20h6M12 16v4'/>")),
    ("device","laptop","笔记本", S("<rect x='4' y='4' width='16' height='11' rx='1.5'/><path d='M2 20h20'/>")),
    ("device","mobile","手机", S("<rect x='7' y='2' width='10' height='20' rx='2.5'/><path d='M11 18h2'/>")),
    ("device","tablet","平板", S("<rect x='5' y='3' width='14' height='18' rx='2'/><path d='M11 18h2'/>")),
    ("device","watch","手表", S("<rect x='7' y='7' width='10' height='10' rx='2.5'/><path d='M9 7l.5-3h5L15 7M9 17l.5 3h5l.5-3'/><path d='M11 11l1.5 1.5'/>")),
    ("device","keyboard","键盘", S("<rect x='2' y='6' width='20' height='12' rx='2'/><path d='M6 10h.01M10 10h.01M14 10h.01M18 10h.01M8 14h8'/>")),
    ("device","mouse","鼠标", S("<rect x='8' y='4' width='8' height='16' rx='4'/><path d='M12 8v3'/>")),
    ("device","printer","打印机", S("<path d='M7 9V4h10v5'/><rect x='4' y='9' width='16' height='6' rx='1.5'/><path d='M8 15h8v5H8z'/><path d='M11 18h2'/>")),
    ("device","camera","相机", S("<rect x='3' y='7' width='18' height='13' rx='2'/><path d='M8 7l1.5-3h5L16 7'/><circle cx='12' cy='13.5' r='3.5'/>")),
    ("device","battery","电池", S("<rect x='3' y='8' width='16' height='8' rx='2'/><path d='M21 11v2'/><path d='M7 12h5'/>")),
]
# ============ 电商与支付 commerce (10) ============
commerce = [
    ("commerce","store","商店", S("<path d='M4 9l1-4h14l1 4'/><path d='M4 9v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9'/><path d='M4 9h16'/><path d='M9 20v-6h6v6'/>")),
    ("commerce","gift","礼物", S("<rect x='4' y='9' width='16' height='11' rx='1.5'/><path d='M3 9h18'/><path d='M12 9v11'/><path d='M12 9c-1-3-4-3-4 0 0 2 4 2 4 0M12 9c1-3 4-3 4 0 0 2-4 2-4 0'/>")),
    ("commerce","discount","折扣", S("<path d='M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z'/><circle cx='8' cy='8' r='1.6'/><path d='M13 13l4 4M17 13l-4 4'/>")),
    ("commerce","credit-card","信用卡", S("<rect x='3' y='6' width='18' height='12' rx='2'/><path d='M3 10h18'/><path d='M6 14h4'/>")),
    ("commerce","invoice","发票", S("<path d='M6 3h9l3 3v15H6z'/><path d='M15 3v3h3'/><path d='M9 11h6M9 14h6M9 17h3'/>")),
    ("commerce","shipping","物流", S("<path d='M2 7h11v9H2z'/><path d='M13 10h4l3 3v3h-7z'/><circle cx='6' cy='18' r='1.6'/><circle cx='17' cy='18' r='1.6'/>")),
    ("commerce","box","包裹", S("<path d='M3 8l9-4 9 4-9 4z'/><path d='M3 8v8l9 4 9-4V8'/><path d='M12 12v8'/>")),
    ("commerce","qrcode","二维码", S("<rect x='4' y='4' width='7' height='7' rx='1'/><rect x='13' y='4' width='7' height='7' rx='1'/><rect x='4' y='13' width='7' height='7' rx='1'/><path d='M14 14h3v3h-3zM19 14v6M14 19h6'/>")),
    ("commerce","coupon","优惠券", S("<path d='M4 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-3a2 2 0 0 0 0-4z'/><path d='M12 5v14'/>")),
    ("commerce","price","价格", S("<path d='M6 3h12v18l-3-2-3 2-3-2-3 2z'/><path d='M9 8h6M9 12h2M12 11v3'/>")),
]
# ============ 位置与地图 map (10) ============
map = [
    ("map","map","地图", S("<path d='M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z'/><path d='M9 4v14M15 6v14'/>")),
    ("map","pin","定位", S("<path d='M12 21s7-6 7-12a7 7 0 1 0-14 0c0 6 7 12 7 12Z'/><circle cx='12' cy='9' r='2.5'/>")),
    ("map","compass","指南针", S("<circle cx='12' cy='12' r='9'/><path d='M15.5 8.5 11 11l-2.5 4.5L13 13z'/>")),
    ("map","globe","地球", S("<circle cx='12' cy='12' r='9'/><path d='M3 12h18'/><path d='M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18'/>")),
    ("map","navigation","导航", S("<path d='M3 11l18-8-8 18-2-8z'/>")),
    ("map","route","路线", S("<circle cx='6' cy='6' r='2.5'/><circle cx='18' cy='18' r='2.5'/><path d='M6 8.5v3a4 4 0 0 0 4 4h6'/>")),
    ("map","landmark","地标", S("<path d='M4 21V8l8-4 8 4v13'/><path d='M4 12h16'/><path d='M9 21v-5h6v5'/><path d='M12 4v4'/>")),
    ("map","direction","方向", S("<path d='M12 3v18'/><path d='M12 7h7l-2-2 2-2h-7'/><path d='M12 13H5l2-2-2-2h7'/>")),
    ("map","location","位置", S("<circle cx='12' cy='12' r='8'/><circle cx='12' cy='12' r='3'/><path d='M12 2v3M12 19v3M2 12h3M19 12h3'/>")),
    ("map","satellite","卫星", S("<rect x='9' y='3' width='6' height='6' rx='1'/><path d='M12 9v6'/><path d='M9 15H5a3 3 0 0 0 0 6h4M15 15h4a3 3 0 0 1 0 6h-4'/>")),
]
# ============ 天气 weather (10) ============
weather = [
    ("weather","cloudy","多云", S("<path d='M7 18a4 4 0 0 1 .5-8 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 18 18z'/>")),
    ("weather","rain","雨", S("<path d='M7 15a4 4 0 0 1 .5-7.5 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 18 15'/><path d='M8 18l-1 2M12 18l-1 2M16 18l-1 2'/>")),
    ("weather","thunder","雷暴", S("<path d='M7 14a4 4 0 0 1 .5-7.5 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 18 14'/><path d='M12 14l-2 4h3l-2 4'/>")),
    ("weather","snow","雪", S("<path d='M7 14a4 4 0 0 1 .5-7.5 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 18 14'/><path d='M9 19l-1 2M12 18v3M15 19l1 2'/>")),
    ("weather","wind","风", S("<path d='M3 9h11a2.5 2.5 0 1 0-2.5-2.5'/><path d='M3 13h15a2.5 2.5 0 1 1-2.5 2.5'/><path d='M3 17h8a2 2 0 1 1-2 2'/>")),
    ("weather","fog","雾", S("<path d='M4 8h12a3 3 0 1 0-3-3'/><path d='M4 12h16M3 16h16M5 20h14'/>")),
    ("weather","thermometer","温度", S("<path d='M14 14V5a2 2 0 1 0-4 0v9a4 4 0 1 0 4 0Z'/><path d='M12 9v5'/>")),
    ("weather","umbrella","雨伞", S("<path d='M12 3a9 9 0 0 1 9 8H3a9 9 0 0 1 9-8Z'/><path d='M12 11v8a2 2 0 0 1-4 0'/>")),
    ("weather","droplet","水滴", S("<path d='M12 3s6 6 6 10a6 6 0 0 1-12 0c0-4 6-10 6-10Z'/>")),
    ("weather","hail","冰雹", S("<path d='M7 12a4 4 0 0 1 .5-7.5 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 18 12'/><circle cx='9' cy='17' r='1.3'/><circle cx='15' cy='17' r='1.3'/>")),
]
# ============ 内容创作 content (10) ============
content = [
    ("content","pen","钢笔", S("<path d='M4 20l1-4L16 5l3 3L8 19z'/><path d='M14 7l3 3'/><path d='M4 20l3-1'/>")),
    ("content","brush","画笔", S("<path d='M5 19c-1-1-1-3 1-4l8-8 3 3-8 8c-1 2-3 2-4 1z'/><path d='M16 5l3 3'/><path d='M6 15l2 2'/>")),
    ("content","text","文字", S("<path d='M5 6h14'/><path d='M5 11h14'/><path d='M5 16h9'/>")),
    ("content","type","字体", S("<path d='M5 6h9M9.5 6v13'/><path d='M15 19h5M17.5 6v13'/>")),
    ("content","template","模板", S("<rect x='3' y='3' width='18' height='18' rx='2'/><path d='M3 9h18'/><path d='M9 9v12'/>")),
    ("content","layout","布局", S("<rect x='3' y='4' width='18' height='16' rx='2'/><path d='M3 4v16M9 4v16'/>")),
    ("content","magic","魔法", S("<path d='M5 19 16 8'/><path d='M15 4l.8 2.2L18 7l-2.2.8L15 10l-.8-2.2L12 7l2.2-.8z'/><path d='M18 14l.6 1.4L20 16l-1.4.6L18 18l-.6-1.4L16 16l1.4-.6z'/>")),
    ("content","highlight","高亮", S("<path d='M15 5l4 4-9 9H6v-4z'/><path d='M6 20h8'/>")),
    ("content","sticker","贴纸", S("<path d='M5 5h14v9l-5 5H5z'/><path d='M19 14h-5v5'/>")),
    ("content","color","取色", S("<rect x='5' y='5' width='14' height='14' rx='2'/><circle cx='9' cy='9' r='1.4'/><circle cx='15' cy='9' r='1.4'/><circle cx='12' cy='15' r='1.4'/>")),
]
# ============ 医疗健康 health (10) ============
health = [
    ("health","pulse","脉搏", S("<path d='M3 12h4l2-6 4 12 2-6h6'/>")),
    ("health","medical","医疗", S("<rect x='4' y='4' width='16' height='16' rx='3'/><path d='M12 8v8M8 12h8'/>")),
    ("health","pill","药丸", S("<rect x='3' y='9' width='18' height='6' rx='3'/><path d='M12 9v6'/>")),
    ("health","first-aid","急救", S("<rect x='3' y='6' width='18' height='13' rx='2'/><path d='M12 10v5M9.5 12.5h5'/>")),
    ("health","dna","基因", S("<path d='M8 4c0 4 8 4 8 8s-8 4-8 8M16 4c0 4-8 4-8 8s8 4 8 8'/><path d='M9 7h6M9 17h6M8 12h8'/>")),
    ("health","stethoscope","听诊器", S("<path d='M5 3v5a4 4 0 0 0 8 0V3'/><path d='M9 16a3 3 0 0 0 6 0v-3'/><circle cx='18' cy='11' r='2'/>")),
    ("health","hospital","医院", S("<path d='M4 21V9l8-5 8 5v12'/><path d='M4 21h16'/><path d='M12 8v6M9 11h6'/>")),
    ("health","bandage","绷带", S("<rect x='5' y='8' width='14' height='8' rx='4'/><rect x='10' y='10' width='4' height='4' rx='1'/>")),
    ("health","wellness","养生", S("<path d='M12 20c-5-2-7-7-7-12 3 0 5 2 7 5 2-3 4-5 7-5 0 5-2 10-7 12Z'/>")),
    ("health","sleep","睡眠", S("<path d='M20 14.5A8 8 0 1 1 9.5 4 6.5 6.5 0 0 0 20 14.5Z'/><path d='M14 9h3l-3 4h3'/>")),
]
# ============ 餐饮美食 food (10) ============
food = [
    ("food","coffee","咖啡", S("<path d='M4 9h13v5a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4z'/><path d='M17 10h2a2 2 0 0 1 0 4h-2'/><path d='M8 3v2M12 3v2M16 3v2'/>")),
    ("food","food","美食", S("<circle cx='12' cy='12' r='8'/><circle cx='12' cy='12' r='4'/>")),
    ("food","burger","汉堡", S("<path d='M4 8a8 8 0 0 1 16 0'/><path d='M3 11h18'/><path d='M4 13a7 7 0 0 0 14 0'/><path d='M3 16a8 8 0 0 0 16 0'/>")),
    ("food","pizza","披萨", S("<path d='M12 3 3 19a1 1 0 0 0 1 1.3h16A1 1 0 0 0 21 19z'/><circle cx='10' cy='13' r='1'/><circle cx='14' cy='15' r='1'/><circle cx='13' cy='10' r='1'/>")),
    ("food","cake","蛋糕", S("<path d='M4 20h16'/><path d='M5 20v-7a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v7'/><path d='M5 13h14'/><path d='M9 7V5M12 7V5M15 7V5'/>")),
    ("food","drink","饮品", S("<path d='M7 4h10l-1 16H8z'/><path d='M12 4v-1'/>")),
    ("food","fruit","水果", S("<path d='M12 8a4 4 0 0 1 4-4 3 3 0 0 0-4 2 3 3 0 0 0-4-2 4 4 0 0 1 4 4Z'/><path d='M12 8c0 4-2 6-2 9a3 3 0 0 0 6 0c0-3-2-5-2-9Z'/>")),
    ("food","bowl","碗", S("<path d='M4 11h16a7 7 0 0 1-14 0Z'/><path d='M9 7c0-1 .5-2 1.5-2M14 7c0-1-.5-2-1.5-2'/>")),
    ("food","utensils","餐具", S("<path d='M8 3v7a2 2 0 0 1-4 0V3M6 10v11'/><path d='M18 3c-2 0-3 2-3 5s1 4 3 4v9'/>")),
    ("food","wine","酒杯", S("<path d='M8 3h8l-1 6a3 3 0 0 1-6 0z'/><path d='M12 12v6'/><path d='M8 21h8'/>")),
]
# ============ 家居生活 home (10) ============
home = [
    ("home","sofa","沙发", S("<path d='M4 10V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v2'/><path d='M3 10h18v4H3z'/><path d='M5 14v4M19 14v4'/>")),
    ("home","bed","床", S("<path d='M3 7v13'/><path d='M3 12h18v7'/><path d='M3 12h7a2 2 0 0 1 2 2v5'/><path d='M21 9h-4v3'/>")),
    ("home","lamp","台灯", S("<path d='M9 3h6l3 7H6z'/><path d='M12 10v8'/><path d='M9 21h6'/>")),
    ("home","plant","植物", S("<path d='M12 16v4'/><path d='M9 20h6l-1-4H10z'/><path d='M12 12c-3-1-5-3-5-6 4 0 5 2 5 6Z'/><path d='M12 11c0-3 3-4 6-4 0 3-3 4-6 4Z'/>")),
    ("home","bath","洗浴", S("<path d='M4 11h16v4a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3z'/><path d='M6 11V8a2 2 0 0 1 4 0'/><path d='M5 21h14'/>")),
    ("home","kitchen","厨房", S("<path d='M5 10h14v6a3 3 0 0 1-3 3H8a3 3 0 0 1-3-3z'/><path d='M9 10V7a3 3 0 0 1 6 0v3'/><circle cx='12' cy='5' r='1'/>")),
    ("home","chair","椅子", S("<path d='M6 3v9M18 3v9'/><path d='M5 12h14v3H5z'/><path d='M7 15v6M17 15v6'/>")),
    ("home","door","门", S("<path d='M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17'/><path d='M17 12h.01'/>")),
    ("home","window","窗", S("<rect x='4' y='4' width='16' height='16' rx='1.5'/><path d='M4 12h16M12 4v16'/>")),
    ("home","blanket","毯子", S("<path d='M4 6h16v12H4z'/><path d='M4 6c1 2 2 2 3 0s2-2 3 0 2 2 3 0 2-2 3 0'/><path d='M7 10v8M12 10v8M17 10v8'/>")),
]
# ============ 增长运营 growth (10) ============
growth = [
    ("growth","funnel","漏斗", S("<path d='M4 5h16l-6 8v6l-4 2v-8z'/>")),
    ("growth","rocket","火箭", S("<path d='M12 3c3 2 5 6 5 10l-3 3H10l-3-3c0-4 2-8 5-10Z'/><circle cx='12' cy='10' r='1.5'/><path d='M9 16l-2 4 4-1M15 16l2 4-4-1'/>")),
    ("growth","users","用户群", S("<circle cx='9' cy='8' r='3'/><path d='M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6'/><path d='M16 5a3 3 0 0 1 0 6'/><path d='M15 14c3 0 6 2.7 6 6'/>")),
    ("growth","target","目标", S("<circle cx='12' cy='12' r='9'/><circle cx='12' cy='12' r='5'/><circle cx='12' cy='12' r='1.5'/>")),
    ("growth","kpi","指标", S("<path d='M4 18a8 8 0 1 1 16 0'/><path d='M12 18l4-5'/><circle cx='12' cy='18' r='1.5'/>")),
    ("growth","megaphone","喇叭", S("<path d='M4 10v4l9 4V6z'/><path d='M13 8a4 4 0 0 1 0 8'/><path d='M6 18v3'/>")),
    ("growth","signal","信号", S("<path d='M3 20v-3M9 20v-7M15 20v-11M21 20V5'/>")),
    ("growth","bolt","闪电", S("<path d='M13 3 5 13h6l-1 8 8-10h-6z'/>")),
    ("growth","award","奖杯", S("<path d='M7 4h10v5a5 5 0 0 1-10 0z'/><path d='M7 6H4v2a3 3 0 0 0 3 3M17 6h3v2a3 3 0 0 1-3 3'/><path d='M12 14v4'/><path d='M9 21h6'/>")),
    ("growth","handshake","合作", S("<path d='M4 9l4-2 4 3 4-3 4 2'/><path d='M4 12l4 2 4-2 4 2 4-2'/>")),
]
# ============ 交通出行 transport (10) ============
transport = [
    ("transport","car","汽车", S("<path d='M3 13l2-5a2 2 0 0 1 2-1h10a2 2 0 0 1 2 1l2 5'/><path d='M3 13h18v4H3z'/><circle cx='7' cy='17' r='1.5'/><circle cx='17' cy='17' r='1.5'/>")),
    ("transport","bus","公交", S("<rect x='3' y='5' width='18' height='13' rx='2'/><path d='M3 12h18'/><circle cx='7' cy='18' r='1.5'/><circle cx='17' cy='18' r='1.5'/><path d='M7 5v3M17 5v3'/>")),
    ("transport","train","火车", S("<rect x='5' y='3' width='14' height='14' rx='3'/><path d='M5 11h14'/><circle cx='9' cy='14' r='1'/><circle cx='15' cy='14' r='1'/><path d='M8 17l-2 4M16 17l2 4'/>")),
    ("transport","plane","飞机", S("<path d='M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z'/>")),
    ("transport","ship","轮船", S("<path d='M4 15h16l-2 4H6z'/><path d='M6 15V8h12v7'/><path d='M12 4v4'/>")),
    ("transport","bike","自行车", S("<circle cx='6' cy='17' r='3.5'/><circle cx='18' cy='17' r='3.5'/><path d='M6 17l4-7h5l3 7M10 10h4'/><path d='M14 10l2-3h2'/>")),
    ("transport","taxi","出租", S("<path d='M3 13l2-5a2 2 0 0 1 2-1h10a2 2 0 0 1 2 1l2 5'/><path d='M3 13h18v4H3z'/><circle cx='7' cy='17' r='1.5'/><circle cx='17' cy='17' r='1.5'/><path d='M11 4h2v2h-2z'/>")),
    ("transport","subway","地铁", S("<rect x='6' y='3' width='12' height='14' rx='6'/><path d='M6 11h12'/><circle cx='9' cy='14' r='1'/><circle cx='15' cy='14' r='1'/><path d='M9 21l-2-3M15 21l2-3'/>")),
    ("transport","fuel","加油", S("<path d='M5 3h10v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2z'/><path d='M15 9h3v6a2 2 0 0 1-2 2'/><path d='M8 6h4v8H8z'/>")),
    ("transport","parking","停车", S("<rect x='4' y='4' width='16' height='16' rx='3'/><path d='M9 16V8h3.5a3 3 0 0 1 0 6H9'/>")),
]
# ============ 自然生物 nature (10) ============
nature = [
    ("nature","leaf","叶子", S("<path d='M5 19C5 9 12 4 20 4c0 8-5 15-15 15Z'/><path d='M5 19c4-6 8-9 12-11'/>")),
    ("nature","tree","树", S("<path d='M12 21v-4'/><circle cx='12' cy='9' r='6'/>")),
    ("nature","flower","花", S("<circle cx='12' cy='12' r='2.2'/><path d='M12 9.5a3 3 0 0 1 0-5 3 3 0 0 1 0 5Z'/><path d='M14.5 12a3 3 0 0 1 5 0 3 3 0 0 1-5 0Z'/><path d='M12 14.5a3 3 0 0 1 0 5 3 3 0 0 1 0-5Z'/><path d='M9.5 12a3 3 0 0 1-5 0 3 3 0 0 1 5 0Z'/>")),
    ("nature","mountain","山", S("<path d='M3 19l6-11 4 6 3-4 5 9z'/>")),
    ("nature","water","水波", S("<path d='M3 8c2-2 4-2 6 0s4 2 6 0 4-2 6 0'/><path d='M3 14c2-2 4-2 6 0s4 2 6 0 4-2 6 0'/>")),
    ("nature","paw","爪印", S("<circle cx='7' cy='9' r='1.6'/><circle cx='12' cy='7' r='1.6'/><circle cx='17' cy='9' r='1.6'/><path d='M12 12c-2.5 0-4 1.8-4 4 0 2 2 3 4 3s4-1 4-3c0-2.2-1.5-4-4-4Z'/>")),
    ("nature","fish","鱼", S("<path d='M3 12c4-5 11-5 15 0-4 5-11 5-15 0Z'/><path d='M21 12l-3-3v6z'/><circle cx='9' cy='11' r='1'/>")),
    ("nature","bird","鸟", S("<path d='M4 14c6-2 9-7 15-7-1 4-4 7-7 8 3 0 4-2 5-4'/><path d='M4 14v3'/>")),
    ("nature","bug","虫", S("<rect x='9' y='7' width='6' height='11' rx='3'/><circle cx='12' cy='5' r='1.5'/><path d='M9 11H6M18 11h-3M9 15H6M18 15h-3M9 18l-2 2M18 18l2 2'/>")),
    ("nature","butterfly","蝴蝶", S("<path d='M12 12c-2-5-7-4-7 0s5 4 7-1M12 12c2-5 7-4 7 0s-5 4-7-1'/><path d='M12 12v8'/>")),
]

ICONS = (general + media + social + nav + time + biz + tools + status +
         security + device + commerce + map + weather + content + health +
         food + home + growth + transport + nature)

def ornament():
    return ("<svg class='orn' width='56' height='12' viewBox='0 0 56 12' fill='none'>"
            "<circle cx='6' cy='6' r='3' fill='#C67E2E'/>"
            "<circle cx='28' cy='6' r='3' fill='#DCC9A8'/>"
            "<circle cx='50' cy='6' r='3' fill='#4A7BB5'/></svg>")

def card(ic):
    cid, en, cn, svg = ic
    disp = svg.replace("stroke='currentColor'", "stroke='#C67E2E'")
    return ("\n      <article class=\"ic-card\" data-name=\"" + en + " " + cn + " " + cid + "\" tabindex=\"0\">\n"
            "        <div class=\"ic-show\">" + disp + "</div>\n"
            "        <div class=\"ic-meta\"><span class=\"ic-en\">" + en + "</span><span class=\"ic-cn\">" + cn + "</span></div>\n"
            "        <button class=\"ic-copy\" data-svg=" + html.escape(svg, quote=True) + " aria-label=\"复制 " + en + " SVG\">复制</button>\n"
            "      </article>")

cats_html = ""
for cid, cn, en in CATS:
    items = [ic for ic in ICONS if ic[0] == cid]
    cards = "".join(card(ic) for ic in items)
    cats_html += ("\n    <section class=\"cat\" id=\"" + cid + "\">\n"
                  "      <header class=\"cat-head\"><h2>" + cn + "<span class=\"cat-en\">" + en + "</span></h2>"
                  "<span class=\"cat-count\">" + str(len(items)) + " 图标</span></header>\n"
                  "      <div class=\"ic-grid\">" + cards + "\n      </div>\n    </section>")

sw = ""
labels = ["paper-50","paper-100","paper-200","paper-300","paper-400"]
for i,l in enumerate(labels):
    c = TOKENS["paper"][i]
    sw += "<div class='sw'><span class='sw-dot' style='background:"+c+"'></span><span class='sw-l'>"+l+"</span><span class='sw-v'>"+c+"</span></div>"
accent = ("<div class='sw'><span class='sw-dot' style='background:"+TOKENS["amber"]+"'></span><span class='sw-l'>amber 主色</span><span class='sw-v'>"+TOKENS["amber"]+"</span></div>"
          "<div class='sw'><span class='sw-dot' style='background:"+TOKENS["inkblue"]+"'></span><span class='sw-l'>ink-blue 辅色</span><span class='sw-v'>"+TOKENS["inkblue"]+"</span></div>")

today = datetime.date.today().isoformat()
total = len(ICONS)

# ---------- 纯字符串模板（CSS/JS 花括号保持原样） ----------
TPL = r"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>图标库 · 全量 @VERSION@ | wawa2000c</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700&family=Noto+Sans+SC:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --paper-50:#FBF7F0; --paper-100:#F4ECDD; --paper-200:#E9DCC4; --paper-300:#DCC9A8; --paper-400:#CBB488;
  --amber:#C67E2E; --inkblue:#4A7BB5; --ink:#2B2B28; --ink-soft:#6B655C;
  --line:#E2D6BE; --card:#FFFFFF; --shadow:0 1px 2px rgba(43,43,40,.06),0 8px 24px rgba(43,43,40,.05);
  --radius:14px;
}
[data-theme="dark"]{
  --paper-50:#1B1916; --paper-100:#23201B; --paper-200:#2C2822; --paper-300:#3A342B; --paper-400:#4A4234;
  --amber:#E0A05A; --inkblue:#7FA8D6; --ink:#F1EBDD; --ink-soft:#B6AC99;
  --line:#3A342B; --card:#26221C; --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px rgba(0,0,0,.25);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Noto Sans SC",system-ui,-apple-system,"PingFang SC",sans-serif;
  background:var(--paper-50);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased;
  transition:background .3s,color .3s}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.topbar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper-50) 88%,transparent);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.topbar .wrap{display:flex;align-items:center;gap:16px;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:16px}
.brand .logo{width:26px;height:26px;border-radius:7px;background:var(--amber);display:grid;place-items:center;color:#fff;font-family:"Noto Serif SC";font-weight:700}
.search{flex:1;max-width:420px;position:relative}
.search input{width:100%;height:40px;border:1px solid var(--line);background:var(--card);color:var(--ink);
  border-radius:10px;padding:0 14px 0 38px;font-size:14px;outline:none;font-family:inherit}
.search input:focus{border-color:var(--amber)}
.search svg{position:absolute;left:12px;top:50%;transform:translateY(-50%);width:18px;height:18px;color:var(--ink-soft)}
.theme-btn{height:40px;padding:0 14px;border:1px solid var(--line);background:var(--card);color:var(--ink);
  border-radius:10px;cursor:pointer;font-size:13px;font-family:inherit;display:flex;align-items:center;gap:6px}
.theme-btn:hover{border-color:var(--amber)}
.hero{text-align:center;padding:64px 20px 40px}
.hero h1{font-family:"Noto Serif SC",serif;font-weight:700;font-size:40px;letter-spacing:.5px}
.hero p{color:var(--ink-soft);max-width:640px;margin:14px auto 0;font-size:15px}
.orn{margin:18px auto 0;display:block}
.badge{display:inline-block;margin-top:22px;font-size:12px;color:var(--amber);border:1px solid var(--line);
  background:var(--card);padding:6px 14px;border-radius:999px}
.spec{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px;margin:8px 0 40px;box-shadow:var(--shadow)}
.spec h3{font-family:"Noto Serif SC",serif;font-size:20px;margin-bottom:18px;display:flex;align-items:center;gap:8px}
.spec h3::before{content:"";width:4px;height:18px;background:var(--amber);border-radius:2px}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}
.sw-row{display:flex;flex-wrap:wrap;gap:10px}
.sw{display:flex;align-items:center;gap:8px;font-size:12px;background:var(--paper-100);border:1px solid var(--line);
  padding:6px 10px;border-radius:9px}
.sw-dot{width:20px;height:20px;border-radius:6px;border:1px solid rgba(0,0,0,.08);flex:none}
.sw-l{font-weight:500}.sw-v{color:var(--ink-soft);font-family:ui-monospace,monospace}
.kv{font-size:13px;color:var(--ink-soft);line-height:2}
.kv b{color:var(--ink)}
.sizes{display:flex;align-items:flex-end;gap:18px}
.sizes span{display:flex;flex-direction:column;align-items:center;gap:6px;color:var(--ink-soft);font-size:11px}
.sizes i{display:block;background:var(--amber);border-radius:3px}
.do-dont{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:8px}
.dd{border:1px solid var(--line);border-radius:10px;padding:14px;font-size:13px}
.dd h4{font-size:13px;margin-bottom:8px}
.dd.ok h4{color:#3E8E5A}.dd.no h4{color:#C0492E}
.dd ul{padding-left:18px;color:var(--ink-soft)}
.cat{margin:0 0 44px}
.cat-head{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1px solid var(--line);
  padding-bottom:10px;margin-bottom:20px}
.cat-head h2{font-family:"Noto Serif SC",serif;font-size:24px;display:flex;align-items:baseline;gap:12px}
.cat-en{font-size:13px;color:var(--ink-soft);font-weight:400;font-family:"Noto Sans SC"}
.cat-count{font-size:12px;color:var(--ink-soft)}
.ic-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:14px}
.ic-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 12px 12px;
  display:flex;flex-direction:column;align-items:center;gap:10px;position:relative;transition:.18s;cursor:default}
.ic-card:hover{border-color:var(--amber);transform:translateY(-2px);box-shadow:var(--shadow)}
.ic-show{width:48px;height:48px;display:grid;place-items:center}
.ic-show svg{width:32px;height:32px}
.ic-meta{text-align:center;line-height:1.3}
.ic-en{display:block;font-size:13px;font-weight:500}
.ic-cn{display:block;font-size:11px;color:var(--ink-soft)}
.ic-copy{position:absolute;top:8px;right:8px;font-size:11px;color:var(--ink-soft);background:var(--paper-100);
  border:1px solid var(--line);border-radius:7px;padding:3px 8px;cursor:pointer;opacity:0;transition:.18s;font-family:inherit}
.ic-card:hover .ic-copy,.ic-card:focus-within .ic-copy{opacity:1}
.ic-copy:hover{color:var(--amber);border-color:var(--amber)}
.ic-copy.done{color:#3E8E5A;border-color:#3E8E5A}
.empty{text-align:center;color:var(--ink-soft);padding:60px 0;display:none}
footer{border-top:1px solid var(--line);padding:32px 20px 56px;text-align:center;color:var(--ink-soft);font-size:13px}
footer .orn{margin-bottom:14px}
@media(max-width:560px){.hero h1{font-size:30px}.ic-grid{grid-template-columns:repeat(auto-fill,minmax(104px,1fr))}}
</style>
</head>
<body>
<header class="topbar"><div class="wrap">
  <div class="brand"><span class="logo">图</span>图标库</div>
  <div class="search">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>
    <input id="q" placeholder="搜索图标（中/英/分类）…" autocomplete="off">
  </div>
  <button class="theme-btn" id="theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/></svg>浅/深</button>
</div></header>

<main class="wrap">
  <section class="hero">
    <h1>图标库 · 全量 @VERSION@</h1>
    <p>基于「纸本美学 · 编辑风格」设计规范的线稿图标体系。viewBox 24×24，描边 1.8，圆角端点，琥珀主色 / 墨蓝辅色。共 @TOTAL@ 枚，覆盖 20 大类，适用于产品、运营与增长场景。</p>
    @ORN@
    <div class="badge">全量 @VERSION@ · @TOTAL@ / @PLAN@ · 作者 wawa2000c</div>
  </section>

  <section class="spec">
    <h3>设计规范 · Design Tokens</h3>
    <div class="spec-grid">
      <div>
        <div class="kv" style="margin-bottom:10px"><b>纸本底色</b>（5 级色谱）</div>
        <div class="sw-row">@SW@</div>
        <div class="sw-row" style="margin-top:10px">@ACCENT@</div>
      </div>
      <div class="kv">
        <div><b>图标几何</b></div>
        viewBox 0 0 24 24<br>
        stroke-width <b>1.8</b><br>
        stroke-linecap / linejoin <b>round</b><br>
        fill <b>none</b> · stroke currentColor<br>
        禁用 emoji，全手绘线稿 SVG
      </div>
      <div>
        <div class="kv" style="margin-bottom:10px"><b>尺寸梯度</b></div>
        <div class="sizes">
          <span><i style="width:16px;height:16px"></i>16 sm</span>
          <span><i style="width:24px;height:24px"></i>24 md</span>
          <span><i style="width:32px;height:32px"></i>32 lg</span>
          <span><i style="width:40px;height:40px"></i>40 xl</span>
          <span><i style="width:56px;height:56px"></i>56 2xl</span>
        </div>
      </div>
      <div>
        <div class="kv" style="margin-bottom:8px"><b>使用准则</b></div>
        <div class="do-dont">
          <div class="dd ok"><h4>✓ 推荐</h4><ul><li>统一 1.8 描边</li><li>圆角端点</li><li>24 栅格对齐</li><li>currentColor 继承文字色</li></ul></div>
          <div class="dd no"><h4>✕ 避免</h4><ul><li>混用实心/线稿</li><li>描边忽粗忽细</li><li>使用 emoji</li><li>随意改 viewBox</li></ul></div>
        </div>
      </div>
    </div>
  </section>

  @CATS@

  <div class="empty" id="empty">未找到匹配的图标</div>
</main>

<footer>
  @ORN@
  图标库 · 全量 @VERSION@ — 纸本美学 · 编辑风格（v6 琥珀主色版）<br>
  作者 wawa2000c · @TODAY@ · 共 @TOTAL@ 枚 / 计划 @PLAN@ 枚
</footer>

<script>
var q=document.getElementById('q'),empty=document.getElementById('empty');
q.addEventListener('input',function(){var t=q.value.trim().toLowerCase();var n=0;
  document.querySelectorAll('.ic-card').forEach(function(c){var m=c.dataset.name.toLowerCase().indexOf(t)>=0;c.style.display=m?'':'none';if(m)n++;});
  document.querySelectorAll('.cat').forEach(function(s){var vis=[].slice.call(s.querySelectorAll('.ic-card')).some(function(c){return c.style.display!=='none';});s.style.display=vis?'':'none';});
  empty.style.display=n?'none':'block';});
document.getElementById('theme').addEventListener('click',function(){var r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark';});
document.querySelectorAll('.ic-copy').forEach(function(b){b.addEventListener('click',function(){var svg=b.getAttribute('data-svg');navigator.clipboard.writeText(svg).then(function(){b.textContent='已复制';b.classList.add('done');setTimeout(function(){b.textContent='复制';b.classList.remove('done');},1400);});});});
</script>
</body>
</html>"""

HTML = (TPL
        .replace("@VERSION@", VERSION)
        .replace("@TOTAL@", str(total))
        .replace("@PLAN@", str(TOTAL_PLAN))
        .replace("@CATS@", cats_html)
        .replace("@ORN@", ornament())
        .replace("@TODAY@", today)
        .replace("@SW@", sw)
        .replace("@ACCENT@", accent))

out = "图标库-全量-v2.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)

data = {"version":VERSION,"total":total,"plan":TOTAL_PLAN,"tokens":TOKENS,
        "categories":[{"id":c[0],"cn":c[1],"en":c[2]} for c in CATS],
        "icons":[{"cat":i[0],"en":i[1],"cn":i[2],"svg":i[3]} for i in ICONS]}
with open("icon-library-v2.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

print("OK ->",out,"icons:",total,"cats:",len(CATS))
