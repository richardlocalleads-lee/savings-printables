# BRIEF-7：可交互 Undated 周计划本（IWP-01）——第三方制作任务书

- 日期：2026-11-05
- 发件：Lee（SettledDays）
- 制作：第三方
- 审核：产出带回主聊（Muse）先审，合格后 Lee 定稿、上架；不合格打回重做。
- 类型：真做新产品（不是核验、不是改现有产品）。

## 一、背景（白话）

Pinkoi 上卖得最好的两件规划本都是带超链接导航的可交互本：一件 180 件成交、一件 172 件成交，都是 A 级证据（页面公开售出数）。我们现在要做一款新的：导航本身就是产品——每一页都有标签，点一下就跳到对应章节；打印出来和普通打印品一样，链接不影响打印。

这款是全新产品，不是给现有产品加链接（现有两款 P1-Move First、P1-Family Sorting 已加过链接作试点，那是另一件事）。

## 二、产品定义（工作代号 IWP-01）

- 工作名：Interactive Undated Weekly Planner（可交互 Undated 周计划本）
- 形态：可填写 PDF（fillable，AcroForm），A4＋Letter 两版；英文；极简黑白；导航标签须一眼可辨
- 定位：通用周计划本，不针对特定人群、不针对 ADHD；undated（不限年份，常青）
- 与现有产品的区别（制作时须守住）：
  - D4-Weekly 是 ADHD 专项、8 页、静态本；本款是通用、导航优先、10 页，不得复制 D4-Weekly 的 ADHD 专项内容与文案
  - Speed7 是 5 页任务清单专项；本款第 9 页任务清单是周计划本里的通用工具页，不得复制 Speed7 的具体文案
  - 上架时描述会带防重买句说明与 D4-Weekly、Speed7 的关系；制作方不用处理描述，只须保证内容不复制

## 三、页结构（10 页，页码从 1 起）

| 页 | 内容 | 要求 |
|---|---|---|
| 1 | Cover（封面） | 标题＋linked contents（每行链到对应章节）＋一句 "Tap a section name to jump straight to it." |
| 2 | How to use | 导航地图（全部 9 个章节列表，每行带链接）＋打印说明（链接不打印，打印出来与普通打印品一样） |
| 3 | Month overview | Undated 12-month grid，可填月份 |
| 4 | Week at a glance | Undated 7-day spread，本款核心页 |
| 5 | Priorities | Top 3＋weekly focus |
| 6 | Week review | What worked／carry forward |
| 7 | Habit tracker | Monthly 31-day grid |
| 8 | Brain dump | Free notes |
| 9 | Task inbox | Sorted today／this week |
| 10 | Notes | Closing page＋link back to cover |

## 四、导航机制（本款核心要求）

1. 封面目录每行 → 对应章节首页；第 2 页导航地图每行 → 对应章节首页。
2. 每页内容页（p.3–10）带标签条，9 个标签全部可达：Cover／Month／Week／Priorities／Review／Habits／Dump／Tasks／Notes，点标签跳到对应页；章节标题点回封面。
3. 标签条位置与形式由制作方定（顶部单行／双行／侧边均可），须满足：每页同一位置、同一形式；9 个标签全部可读（100% 显示与 300px 缩略图下均可辨）；点击落点正确。
4. 链接用 PDF `/Link` 标注；不插页、不改内容、不改排版；链接不打印。
5. 可填字段：规划页上的任务、日期、勾选框均为可填字段（AcroForm text fields／checkboxes），Adobe Reader 里填了能保存、重开后仍在。
6. 字体：须完整嵌入；英文用系统字体或可商用字体；不用未授权字体；不用图片字体。
7. 视觉：极简黑白；导航标签用灰底或描边与正文区分；不做彩色插画、不做照片背景。

## 五、交付物

1. 主 PDF 两版：`IWP-01-Interactive-Weekly-Planner_A4.pdf`、`IWP-01-Interactive-Weekly-Planner_Letter.pdf`（可填、带链接）
2. `README.txt`（英文：怎么用链接、怎么打印、字段说明）
3. `PERSONAL_USE_LICENSE.txt`（随附的标准个人使用许可，原样用，不得改）
4. 买家 ZIP：`IWP-01-Buyer-Files-1.zip`（内含以上 4 件：两份 PDF＋README＋LICENSE）

## 六、验收清单（主聊按此逐项验，不合格打回）

1. 页数 10 页，两版一致。
2. 链接逐个核对：封面目录每行落点对、第 2 页导航地图每行落点对、每页标签条 9 个标签落点全对、回封面链对；链接矩形均在页内。
3. 字段：可填字段在 Adobe Reader 填写、保存、重开后仍在；字段数两版一致。
4. 打印：逐页渲染与无链接版像素一致（链接不打印）；页面无截断、无重叠。
5. 字体完整嵌入，无缺字。
6. 300px 缩略图下各页可辨、标签可读。
7. ZIP 内文件与清单一致，字节＋SHA-256 有记录。

## 七、红线（写死）

1. 不得抄袭 Pinkoi 同类产品的版式、文案、内容——借的是“可交互导航”这个机制，产品、文案、版式须原创。
2. 绝对不碰 Etsy 内容（不打开、不引用、不分析任何 Etsy 页面）；也不得引用、转发任何 Etsy 研究文件。
3. 不得编造承诺（无疗效、无“保证”、无销量口径）；文案诚实，有一分证据说一分话。
4. 不登录任何账号、不发布、不付款；Publish 永远 Lee 亲手点。
5. 定价由 Lee 定，不用第三方定（本任务书不含定价）。
6. 随附文件只用第八节清单里的；不得向第三方提供清单外的文件。

## 八、随附文件清单（与本任务书一起发）

1. `PERSONAL_USE_LICENSE.txt`（标准个人使用许可，原样用；来源：D4-Weekly 买家 ZIP，464 B）
2. `REF-D4-Weekly-EN-A4-Style-Reference.pdf`（仅作版式与字段风格参考：极简黑白、可填字段样式、A4 尺寸；不得复制其内容——ADHD 专项内容不适用本产品；来源：D4-Weekly 买家 ZIP 内 `Weekly_EN_A4.pdf`，105,299 B）
3. `PRODUCTION-STANDARDS-2026-11-05.md`（我方新产品生产标准：可点击目录的规则与五项验证，供对照）

## 九、交付方式与时间

- 产出文件由 Lee 转交主聊审核；通过后才进上架包阶段。
- 初版建议 5 个工作日内；时间由 Lee 与第三方约定。
- 发的时候把本任务书 `.md` 文件本身发过去，不只发下载页链接；请第三方先回执文件名、SHA-256 与字节数确认版本无误再开工。
