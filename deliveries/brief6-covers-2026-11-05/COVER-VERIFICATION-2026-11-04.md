# COVER-VERIFICATION-2026-11-04 — BRIEF-6 六张新封面核验报告

日期：2026-11-05（HKT）。任务：BRIEF-6-COVER-IMAGES-6-LISTINGS-2026-11-04。
本报告只陈述本对话实际做过、验过的事；换图动作不在本对话执行（见 FIELD-NOTE）。

## 0. 源文件接收核验（开工前提）

- 源文件经 BRIEF-6-SOURCES-2026-11-05.md 给出的 GitHub Pages 地址下载，共 39 个（m5 7、m6 6、m2 6、m3 6、s023 10、dated12 4），另加 MANIFEST-SHA256.txt 本身。
- 逐个 `sha256sum -c MANIFEST-SHA256.txt`：**39/39 OK**，与清单全对。下载文件存 `~/workspace/etsy/briefs-2026-11-05/sources/`（按原相对路径）。
- 页面身份互证（合成前先确认「哪一页是哪一页」，避免贴错页）：
  - M5：A4 PDF 第 2 页与 m5-img1-house-grid-a4.png 像素签名差 0.89（近乎同一渲染）→ 封面用 PDF 第 2 页（House Fund 第 1 页）。其余 5 页签名差 1.6–15.4，非此页。
  - S-023：移交 A4 PDF 第 1 页与 s023-img6-walkthrough-print.png 签名差 1.38 → 封面用第 1 页（Room Walkthrough）。
- xlsx ↔ img1 对照（试算表类，确认现有图 1 就是已填示例的截图、内容同一张表）：
  - M2 已填示例 sheet XML 内含 "Bill Calendar" 标题与 Rent (part 1 of 2)、Car insurance、Minimum debt payment 等行 → 与 m2-img1 同表 ✓。
  - M3 已填示例内含 "Budget Overview" 与 Venue & Rentals、Rehearsal Dinner 等行 → 与 m3-img1 同表 ✓。
  - S-023 已填示例内含 Inventory 及 Kitchen/Bedroom/Garage/Living 等房间名 ✓（本封面采用印出页路线，未用此截图，见 §5）。
  - 三个已填示例经 LibreOffice 转 PDF 成功打开（24 / 57 / 16 页），文件完好。

## 合成方法（六张通用）

- 场景：AI 生成的「空白表面」照片（空白纸面/空白屏幕，无任何文字），柔光、低饱和，与黑白极简品牌一致。场景图为生成图、非实拍，先行声明。
- 产品层：只用真实源文件——打印类由随附 PDF 以 300 dpi 渲染整页；试算表类直接用随附 img1 截图原图；dated12 用随附 img1 原图。只做透视贴合（按场景表面四角映射），**保持原始宽高比**（fit-inside，不拉伸变形），不重绘、不改字、不改数字、不改版面。
- 场景里原本压在纸面上的实物（M6 的笔、dated12 的两枚图钉）在合成后按原位置回贴到打印页之上，与场景照片中的遮挡关系一致。
- 无任何文字叠加：未在图上加标题、卖点、价格或水印。笔记本键盘上的键帽字母是场景照片自带的实物细节，非叠加文字。
- 统一规格：2000×2000 px、JPG、RGB（sRGB 值，与源文件一致，无嵌入 ICC）、每张 ≤2 MB（实测 337–488 KB）。

## 1. M5 Goal Savings Challenge → `m5-cover-new.jpg`

- 源文件：`m5/M5-Goal-Savings-Challenge_A4.pdf` 第 2 页（House Fund 房子基金，第 1 页，共 2 页），300 dpi 渲染。
- 场景：俯拍，打印页平放在浅色木桌上，黑笔立在纸的右侧边沿。
- 成品：2000×2000，499,785 字节，SHA256 `5ae72b8346993660d6430bc4443ed9467131e59778afc97adfb95693a214eaca`。
- 对照原图：标题 House Fund 房子基金 ✓；副行 $5 × 40 · $10 × 40 · $20 × 20 ✓；格阵 4 行 $5 + 1 行 $10 ✓；页脚 This page: $300 · Goal total: $1,000 ✓；与 m5-img1 版面逐项一致，无增删。
- 缩略图自查（300×300）：房子格阵与金额一眼可辨，主体居中、留白充足 ✓。

## 2. M6 One-Page Habit Tracker → `m6-cover-new.jpg`

- 源文件：`m6/M6-One-Page-Habit-Tracker_A4.pdf`（单页），300 dpi 渲染。
- 场景：整页夹在棕色写字板上，写字板略斜放在浅色桌面，黑笔横放在页面下沿（在打印页之上回贴）。
- 成品：2000×2000，396,066 字节，SHA256 `fc6d00b2e96b169da18dbb95eb2267797e9f72e6dc8c65d0fde08816b9e17017`。
- 对照原图：标题 One-Page Habit Tracker 一頁習慣追蹤表 ✓；Month 行 ✓；Habit 1/2/3 三行 × 1–31 格完整、无裁切 ✓；页脚温和文案与 1/1 页码 ✓；整页四边都在画面内 ✓。
- 缩略图自查：写字板与标题、三行格阵可辨 ✓。

## 3. M2 Biweekly Bill Calendar & Debt Payoff → `m2-cover-new.jpg`

- 源文件：`m2/m2-img1-bill-calendar.png`（已填示例 Bill Calendar 表截图原图；与已填示例 xlsx 互证同表，见 §0）。
- 场景：银色笔记本电脑放在木桌上，屏幕显示该表（顶部对齐、白底与屏幕融为一体）；左侧合上的笔记本，后方一杯咖啡。
- 成品：2000×2000，409,497 字节，SHA256 `ae143197c79bcb443c255ada52a50adcb0ad6c8b63052fe4271a309712a7e2f8`。
- 对照原图：标题 Bill Calendar — bills assigned to a paycheck by due date ✓；9 行账单（Rent 两段、Electric、Phone、Internet、Water、Car insurance、Streaming、Minimum debt payment）与金额 ✓；合计 Total — all bills 1,870.00 ✓；一字未改。截图自带的浅蓝输入格底色为源文件原样，未加色、未去色。
- 缩略图自查：笔记本＋表格形态一眼可辨，标题行可读 ✓（细格数字在缩略图下不可读属预期，与原图 1 同级）。

## 4. M3 Wedding Planner Spreadsheet → `m3-cover-new.jpg`

- 源文件：`m3/m3-img1-budget-overview.png`（已填示例 Budget Overview 截图原图；互证见 §0）。
- 场景：深灰笔记本电脑放在白色桌面正对镜头，屏幕显示预算总览整表；右侧笔记本与一支笔。除此以外无任何婚礼元素（无花、无戒指、无婚纱、无喜字）✓。
- 成品：2000×2000，392,500 字节，SHA256 `c49b41cd5697724a722f353fb8ecd6c2bafcc4d694357ce973d5f297114a42bf`。
- 对照原图：标题 Wedding Budget — Budget Overview ✓；Total Budget $30,000.00、Wedding Date 2027-10-23 ✓；15 个类别行与 Total 100% / $30,000.00 / $1,800.00 / $7,800.00 / $28,200.00 / $20,400.00 ✓；底部 Totals from Vendor Payments 段 ✓。截图自带的浅黄输入列底色为源文件原样，保留未改。
- 缩略图自查：整表结构与标题可辨 ✓。

## 5. S-023 Home Inventory → `s023-cover-new.jpg`

- 路线选择：简报给了两条（笔记本屏幕／印出移交页），本封面采用**印出页**路线。
- 源文件：`s023/Home-Inventory-Walkthrough-Handover-A4.pdf` 第 1 页（Home Inventory — Room Walkthrough），300 dpi 渲染（与 s023-img6 互证同页，见 §0）。
- 场景：印出的 walkthrough 页平放在储物间小木桌上，背景是虚化的货架与纸箱——与简报 B 路线的「印出页＋虚化货架」一致；差异如实记：页面是平放在货架前的小桌上，**不是手持**。
- 成品：2000×2000，495,341 字节，SHA256 `e127c080513e580d8f92d80e1a381e30a63eb157176bb362493cc53015be59bd`。
- 对照原图：标题与用法段 ✓；Room / Item / Est. value / Photo filename 四栏与 Living Room / Kitchen / Dining Room / Hallway / Entry / Bedroom (Primary) 行序 ✓；勾选框列 ✓；页脚 Settled Days — Personal use only · Page 1 of 3 ✓。
- 缩略图自查：标题可读、清单表形态可辨、储物背景成立 ✓。

## 6. 2027 Dated 12-pack → `dated12-cover-new.jpg`

- 源文件：`dated12/img1-january-a4-01.png` 原图（一月 A4 页本身，非渲染改制）。
- 场景：一月页用两枚图钉钉在浅色墙上（图钉按原位置回贴在打印页两角之上），下方木条上放一支黑笔。
- 成品：2000×2000，344,420 字节，SHA256 `c75edeaef27f21d5031708a51622c6f1154c5f4a437b9f434e1ebb61c6966e1a`。
- 对照原图：January 一月 · 2027 ✓；Mon–Sun 双语星期行 ✓；日期格 1 起于周五、31 天完整 ✓；页脚 Personal use only / 僅限個人使用 ✓。
- 缩略图自查：月历形态与日期数字在 300×300 下仍可辨（本组六张中缩略图可读性最好）✓。

## 按简报自查项逐条（§4 的 1–5）

1. **真实文件**：六张的产品层全部来自随附源文件（PDF 渲染页／img1 原图），无一张是重画或凭记忆补的 ✓。源文件接收时 39/39 SHA 对清单 ✓。
2. **无叠加文字**：六张均未加任何文字、价格、卖点 ✓（场景照片自带的键盘键帽字母除外，见合成方法）。
3. **缩略图检查**：六张均已缩到 300×300 逐张目检，结论记在各节 ✓（拼版对照图存 work/thumbs/contact-300.png）。
4. **场景对版**：六个场景互不相同（木桌俯拍／写字板／木桌笔记本／白桌笔记本／储物间小桌／墙面钉页），且与各产品当前图 1 的白底平铺版式明显不同 ✓。
5. **无婚礼素材**：M3 场景只有笔记本、笔记本子与笔，无任何婚礼库存图元素 ✓。

## 边界与未做事项（照实写）

- 未碰 Etsy：未登录、未打开 listing 编辑页、未换任何一张图。换图步骤与顺序见 FIELD-NOTE-2026-11-04.md，在主聊的已登录会话里做。
- 未验证新封面带来的点击/转化变化——那要换图后用店铺数据看，本报告不声称任何效果。
- 场景图为 AI 生成照片（空白表面），非实拍；产品内容本身 100% 为真实文件。如实标注，供上架决策时知情。
- 本任务只用了 BRIEF-6-SOURCES 清单内的 39 个文件；M2/M3 的 Etsy 调研类生产资料未接触、未外发。合成脚本与中间文件在本机 `~/workspace/etsy/briefs-2026-11-05/work/`，可复跑。
