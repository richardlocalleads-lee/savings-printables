# 老款图包映射定稿 — §5.2 第 3 项（SettledDays 质感改造任务包）

日期：2026-11-08（HKT）。性质：纯案头核查。方法：10 份公开 listing 页 PDF 实物（U5 浏览器任务登出状态抓取）＋磁盘全树像素比对（4066 个文件）＋12 张 pin 图全分辨率目视。
依据文件：§5.2 闭合报告（草稿）`SECTION-5.2-CLOSURE-DRAFT-2026-11-08.md` §2.3（20 张候选）；任务包 `TASK-PACKAGE-OVERHAUL-2026-11-08.md` §5.1／§5.2；11-06 全量检查报告 `LISTING-IMAGE-FULL-REVIEW-REPORT-2026-11-06.md`；主状态表 v3.44 §14 2026-11-06 23:35 行第 ③ 条。
（`ST/` = `~/workspace/cross-border-micro-digital-business/steel-thread/`。）

## 0. 结论总表

**20 张磁盘候选（去重后 19 张）**：**2 张在线上出现**（均为各款图 1：`cover_fullpack.png`→Savings Full 图 1、`cover_starter.png`→Savings Starter 图 1）；**17 张未在线上出现**（v2-02／v2-03／v2-04／v2b-08／v2b-09、D4 p-01～p-04、P1 p-01～p-04、Restart L-1～L-4）；`v2c-02.png` 与 `v2-02.png` 为同一文件（SHA 完全相同），非独立候选。

**52 张线上图**：**50 个位置文件级已确认**（46 个 distinct 磁盘文件）；**2 个位置未确认**（Savings Full 图 2、图 6，磁盘未找到）。【主聊核验补记 2026-11-08：原“2 个位置封面级已确认”即 Savings Starter 图 3／图 4 已由回包索引表标题＋磁盘原图标题双源确认为 pin18-habitstack／pin3-starter，见文末补记；两图不是同一文件。】

**§5.1 三处核对**：② Budget Full 图 1 与图 2–5 为两个不同封面文件——**已确认**；③ Habit Full 图 4 用 Starter 封面、Habit Starter 图 2／3／5 用 Full 封面、2027 Starter 图 2–5 用 Full 封面——**三处均已确认，与 §5.1 第 7／8／9 项一致**。

**对闭合报告 §2.3 的修正**：线上图库并非笼统的“生活照＋网格”——D4／P1／Restart 三款确为生活照（hero／场景）＋总览网格（M4_allpages／04_AllPages／M5_all_pages）；Savings／Habit／Budget／2027 六款图库为**封面＋竖版 pin 图**（1000×1500，上为标题、下为封面），无生活照、无内页渲染图。11-06 报告“B 组候选 20 张”的框架（暗含候选即线上图）亦须修正：20 张候选中仅 2 张封面在线上出现，其余 17 张页面渲染图在 10 个 listing 的 52 张线上图中**一张都未出现**——老款 listing 的图库不是用产品内页渲染图搭的，而是用封面、竖版 pin 图与 listing-asset mockup 搭的。

**证据说明（重要）**：任务书称“回包索引表见父对话”，但**本任务的工作上下文中并无该索引表全文**（工作区亦无以 `b538d895` 命名的索引文件；逐张截图 i1–i66 未落盘）。故本定稿未用索引表文字描述，而是直接以 10 份 PDF 实物比对：每份 PDF 内嵌 1 张 794×794 主图（图 1）＋N 张 75×75 filmstrip 缩略图（图 1–N，顺序与线上一致，已用“缩略图 1 ≈ 主图 MSE 13–25”验证顺序），再对磁盘全树 4066 个文件做像素 MSE 匹配（方形原图直接比对；竖版 1000×1500 pin 图用中心裁切比对，见 §6）。证据等级高于索引表文字描述。三处残留未确认项如需索引表复核，可由父代理补发索引表后重核。

## 1. 20 张磁盘候选逐张归属

| # | 候选文件 | SHA-256（前 8 位）／字节 | 线上归属 | 结论 |
|---|---|---|---|---|
| 1 | `thread2-build/cover_fullpack.png` | `15eb5e6b`／56,273 | **Savings Full 图 1**（MSE 7） | 已确认 |
| 2 | `thread2-build/cover_starter.png` | `b5b01240`／56,216 | **Savings Starter 图 1**（MSE 15） | 已确认 |
| 3 | `thread2-build/preview/v2-02.png` | `42f29376`／59,650 | — | 未在线上出现 |
| 4 | `thread2-build/preview/v2-03.png` | `26ebb973`／56,789 | — | 未在线上出现 |
| 5 | `thread2-build/preview/v2-04.png` | `097cd3e2`／47,091 | — | 未在线上出现 |
| 6 | `thread2-build/preview/v2b-08.png` | `53ecef78`／21,866 | — | 未在线上出现 |
| 7 | `thread2-build/preview/v2b-09.png` | `586ef0b8`／40,211 | — | 未在线上出现 |
| 8 | `thread2-build/preview/v2c-02.png` | `42f29376`／59,650（与 v2-02 同一 SHA） | —（与 #3 同一文件） | 非独立候选；未在线上出现 |
| 9 | `adhd-planner-light/mockup/renders/p-01.png` | `0577748b`／86,770 | —（D4 线上为 M1–M4 mockup） | 未在线上出现 |
| 10 | `adhd-planner-light/mockup/renders/p-02.png` | `115aa5a6`／175,577 | — | 未在线上出现 |
| 11 | `adhd-planner-light/mockup/renders/p-03.png` | `c7e0d312`／54,995 | — | 未在线上出现 |
| 12 | `adhd-planner-light/mockup/renders/p-04.png` | `e0680244`／73,416 | — | 未在线上出现 |
| 13 | `p1-moving-command/listing-assets/renders150/p-01.png` | `5e500a83`／198,535 | —（P1 线上为 01–06 listing-assets） | 未在线上出现 |
| 14 | `p1-moving-command/listing-assets/renders150/p-02.png` | `8bd7d4ed`／298,684 | — | 未在线上出现 |
| 15 | `p1-moving-command/listing-assets/renders150/p-03.png` | `5019aae0`／226,350 | — | 未在线上出现 |
| 16 | `p1-moving-command/listing-assets/renders150/p-04.png` | `5b4ad518`／223,283 | — | 未在线上出现 |
| 17 | `weekly-restart-kit/internal-evidence/page-renders/L-1.png` | `9989b99c`／123,647 | —（Restart 线上为 M1–M7 listing-assets） | 未在线上出现 |
| 18 | `weekly-restart-kit/internal-evidence/page-renders/L-2.png` | `3eecdbcc`／125,009 | — | 未在线上出现 |
| 19 | `weekly-restart-kit/internal-evidence/page-renders/L-3.png` | `ff647846`／38,115 | — | 未在线上出现 |
| 20 | `weekly-restart-kit/internal-evidence/page-renders/L-4.png` | `2ccb9d29`／29,013 | — | 未在线上出现 |

“未在线上出现”的判定依据：① 19 候选 × 52 缩略图逐项 MSE 匹配（方形直接比对＋竖版中心裁切比对），最佳 MSE 均 ≥824（Savings 组）或落在白页噪声区（见 §6 阈值说明），远高于同一文件阈值；② 4066 文件全树复核：v2／p-／L- 文件未进入任何一张线上图的 top-3；③ 目视：52 张线上图无一张为 100-Day／52-Week／Savings Log／Sinking Funds 网格页或 p-01～p-04／L-1～L-4 渲染页（Savings 六款线上图为封面＋pin 图＋繁中页；D4／P1／Restart 线上图为 mockup／listing-assets 文件，见 §3）。注意：L-4「BRAIN DUMP 20 行空白横线」与 D-01（Speed7 pin，20 行空白倒脑页）为同类页面但不同文件、不同产品，不得混淆（闭合报告 §2.3 已注）。

## 2. 10 张线上首图逐张来源（全部已确认）

PDF 身份核对：10 份 PDF 标题＋价格与任务书顺序逐一对上——f0 Savings Full $3.00（10 Page）、f1 Savings Starter $1.00（2 Page）、f2 Habit Full $3.00（10 Page）、f3 Habit Starter $1.00（2 Page）、f4 Budget Full $3.00（10 Page）、f5 Budget Starter $1.00（2 Page）、f6 2027 Starter $1.00（2 Page）、f7 D4 $9.99（32 Page）、f8 P1 $14.99（43 Pages）、f9 Restart $9.99。Listing ID 沿用闭合报告 §1（Savings Full 4598465559、Starter 4598538460、Habit Full 4598582424、Starter 4598576567、Budget Full 4598655675、Starter 4598659063、2027 Starter 4598687922、D4 4600823259、P1 4600844093、Restart 4600838577）。

| Listing | 图 1 内容（PDF 794px 主图目视） | 磁盘来源文件 | SHA-256（前 8 位）／字节 | MSE |
|---|---|---|---|---|
| Savings Full | "The Savings Challenge You'll Actually Finish"／"FULL PACK · 10 pages" | `thread2-build/cover_fullpack.png` | `15eb5e6b`／56,273 | 7 |
| Savings Starter | 同标题／"STARTER · $1 · 2 pages" | `thread2-build/cover_starter.png` | `b5b01240`／56,216 | 15 |
| Habit Full | "The Habit Tracker You'll Actually Keep"／"FULL PACK · 10 pages" | `thread2-build/habit-tracker/cover_fullpack.png` | `d798c3eb`／89,140 | 16 |
| Habit Starter | 同标题／"STARTER · $1 · 2 pages" | `thread2-build/habit-tracker/cover_starter.png` | `d3cae6d5`／82,587 | 14 |
| Budget Full | **"The Budget / One page, one month"**／"20 printable budget pages"／"FULL PACK · 10 pages" | `thread2-build/budget-planner/cover_fullpack_m1_v2.png`（**不是** `cover_fullpack.png`，后者 MSE 174） | `d1fd0a7b`／51,592 | 14 |
| Budget Starter | "The Budget You'll Actually Keep"／"STARTER · $1 · 2 pages" | `thread2-build/budget-planner/cover_starter.png` | `6c37c7f1`／52,683 | 14 |
| 2027 Starter | "2027／The 2027 Goals You'll Actually Reach"／"STARTER · $1 · 2 pages" | `thread2-build/newyear-goals-2027/cover_starter.png` | `5ff43881`／62,895 | 15 |
| D4 | 生活照：桌面摊开笔记本 "ADHD-FRIENDLY PLANNER" | `adhd-planner-light/mockup/M1_hero.jpg` | `a27dfd21`／388,322 | 12 |
| P1 | 生活照：桌面摊开笔记本 "PARENTS' MOVE COMMAND CENTER" | `p1-moving-command/listing-assets/01_Main.jpg` | `395c4ded`／504,407 | 13 |
| Restart | 生活照：桌面摊开笔记本 "WEEKLY PLANNER + RESTART KIT" | `weekly-restart-kit/listing-assets/M1_hero.jpg` | `5c185865`／378,276 | 12 |

## 3. 其余 42 张线上图逐张来源

证据等级：A＝PDF 794px 主图目视（仅图 1）／B＝PDF 75px filmstrip 缩略图目视＋MSE 同文件（阈值见 §6）／C＝磁盘原图全分辨率目视（12 张 pin 图封面行逐字核对）。MSE 栏为缩略图 vs 磁盘文件的 75px MSE（竖版 pin 图用中心裁切比对）。

### 3.1 Savings Full（6 张）

| 位置 | 内容（缩略图目视） | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | Full 封面 | `thread2-build/cover_fullpack.png` | `15eb5e6b`／56,273 | 7 | 已确认 |
| 图 2 | 繁中文字页（说明页，非封面） | — | — | 最接近 `cover_fullpack_tc.png` 167 | **未确认**（见 §5 U-1） |
| 图 3 | 竖版 pin 图（封面＋标题） | `thread2-pinterest/pin1-fullpack-hero.png`（标题 "Full Pack Hero" 系） | `343f7b11`／113,810 | 13 | 已确认 |
| 图 4 | 竖版 pin 图 | `thread2-pinterest/pin7-52week.png` | `3b95fa6a`／114,059 | 13 | 已确认 |
| 图 5 | 竖版 pin 图 | `thread2-pinterest/pin2-fullpack-ink.png` | `eb8ff971`／112,211 | 10 | 已确认 |
| 图 6 | 竖版 pin 图（存钱封面） | — | — | 最接近 147（三者并列） | **未确认**（见 §5 U-2） |

### 3.2 Savings Starter（5 张）

| 位置 | 内容 | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | Starter 封面 | `thread2-build/cover_starter.png` | `b5b01240`／56,216 | 15 | 已确认 |
| 图 2 | 繁中 Starter 封面 | `thread2-build/cover_starter_tc.png` | `af9faad3`／63,467 | 14 | 已确认 |
| 图 3 | 竖版 pin 图（Starter 封面） | pin3-starter／pin11-colorcalm／pin18-habitstack 三者之一 | 见 §5 U-3 | 54–55（三者并列） | 封面级已确认；**文件级未确认** |
| 图 4 | 与图 3 同一文件（逐像素 MSE=0） | 同图 3 | 同图 3 | 54–55 | 同上 |
| 图 5 | 竖版 pin 图（Starter 封面） | `thread2-pinterest/pin4-starter-today.png`（标题 "$1 Savings Challenge"） | `eddaa672`／108,138 | 56（次优 94） | 已确认 |

### 3.3 Habit Full（5 张）／Habit Starter（5 张）——图 2–5 为同一组 4 个文件

交叉核对（缩略图逐对 MSE）：Habit Full 图 2＝Starter 图 2（MSE 0）、Full 图 3＝Starter 图 5（0）、Full 图 4＝Starter 图 4（0）、Full 图 5＝Starter 图 3（0）。即 Full[2,3,4,5]＝Starter[2,5,4,3]，4 个文件在两款 listing 间复用，仅 3／5 位互换。

| 位置 | 磁盘来源（竖版 pin 图，1000×1500） | 封面行（磁盘原图全分辨率目视） | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| Habit Full 图 1 | `thread2-build/habit-tracker/cover_fullpack.png` | FULL PACK · 10 pages | `d798c3eb`／89,140 | 16 | 已确认 |
| Habit Full 图 2 ＝ Starter 图 2 | `habit-tracker/habit-pin1.png`（标题 "Mark 30 Days in a Row"） | **FULL PACK · 10 pages** | `34f25273`／138,140 | 45 | 已确认 |
| Habit Full 图 3 ＝ Starter 图 5 | `habit-tracker/habit-pin3.png`（标题 "Stack a Tiny Habit"） | **FULL PACK · 10 pages** | `7ccc81c2`／133,097 | 44 | 已确认 |
| Habit Full 图 4 ＝ Starter 图 4 | `habit-tracker/habit-pin4.png`（标题 "Own Your Morning & Evening"） | **STARTER · $1 · 2 pages** | `39904e6b`／130,285 | 45 | 已确认 |
| Habit Full 图 5 ＝ Starter 图 3 | `habit-tracker/habit-pin2.png`（标题 "Build a Habit in 66 Days"） | **FULL PACK · 10 pages** | `f42a5f77`／136,879 | 46 | 已确认 |
| Habit Starter 图 1 | `thread2-build/habit-tracker/cover_starter.png` | STARTER · $1 · 2 pages | `d3cae6d5`／82,587 | 14 | 已确认 |

### 3.4 Budget Full（5 张）

| 位置 | 磁盘来源（竖版 pin 图，1000×1500） | 封面行（磁盘原图全分辨率目视） | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | `thread2-build/budget-planner/cover_fullpack_m1_v2.png` | "The Budget / One page, one month"／FULL PACK · 10 pages | `d1fd0a7b`／51,592 | 14 | 已确认 |
| 图 2 | `budget-planner/budget-pin4.png`（标题 "Watch Your Debt Shrink"） | "The Budget You'll Actually Keep"／**FULL PACK · 10 pages** | `7e69b62a`／101,715 | 49 | 已确认 |
| 图 3 | `budget-planner/budget-pin1.png`（标题 "Where Did It All Go?"） | 同上／FULL PACK · 10 pages | `b9884cbd`／98,662 | 48 | 已确认 |
| 图 4 | `budget-planner/budget-pin2.png`（标题 "Never Miss a Bill Again"） | 同上／FULL PACK · 10 pages | `1c832eee`／98,345 | 51 | 已确认 |
| 图 5 | `budget-planner/budget-pin3.png`（标题 "The No-Spend Challenge"） | 同上／FULL PACK · 10 pages | `0b6783b5`／100,990 | 51 | 已确认 |

### 3.5 Budget Starter（4 张）

| 位置 | 内容 | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | Starter 封面（"The Budget You'll Actually Keep"） | `thread2-build/budget-planner/cover_starter.png` | `6c37c7f1`／52,683 | 14 | 已确认 |
| 图 2 | 两页并排（Two Pages） | `launch-kit/wave1/demo-pack-2026-10-24/images/Budget-Starter-M2-Two-Pages-2026-10-24.png` | `db0996f8`／258,879 | 5 | 已确认 |
| 图 3 | 已填示例（Filled Example） | `launch-kit/wave1/demo-pack-2026-10-24/images/Budget-Starter-M3-Filled-Example-2026-10-24.png` | `6465d931`／323,255 | 9 | 已确认 |
| 图 4 | 版式说明（Formats，深色底双页） | `launch-kit/wave1/demo-pack-2026-10-24/images/Budget-Starter-M4-Formats-2026-10-24.png` | `033768e7`／366,273 | 7 | 已确认 |

注：demo-pack 目录仅有 M2／M3／M4 三张图（无 M1），图 2–4 与之逐一对应。

### 3.6 2027 Starter（5 张）

| 位置 | 磁盘来源（竖版 pin 图，1000×1500） | 封面行（磁盘原图全分辨率目视） | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | `thread2-build/newyear-goals-2027/cover_starter.png` | STARTER · $1 · 2 pages | `5ff43881`／62,895 | 15 | 已确认 |
| 图 2 | `newyear-goals-2027/goals-pin2.png`（标题 "12 Big Goals for 2027"） | **FULL PACK · 10 pages** | `88b257cc`／114,798 | 95 | 已确认 |
| 图 3 | `newyear-goals-2027/goals-pin1.png`（标题 "New Year, Real Goals"） | **FULL PACK · 10 pages** | `99f4ed55`／115,998 | 95 | 已确认 |
| 图 4 | `newyear-goals-2027/goals-pin4.png`（标题 "Mid-Year Review, Built In"） | **FULL PACK · 10 pages** | `2a5080b5`／114,334 | 96 | 已确认 |
| 图 5 | `newyear-goals-2027/goals-pin3.png`（标题 "Check In Every Quarter"） | **FULL PACK · 10 pages** | `53f0d907`／115,858 | 96 | 已确认 |

注：goals-pin 四张 MSE 95–96 高于其余 pin 图（44–56），因竖版裁切对位残差较大；佐证为双射排列（图 2→pin2、图 3→pin1、图 4→pin4、图 5→pin3，无碰撞）＋次优 121–147 的 margin＋封面行逐字目视。列为已确认，MSE 照录。

### 3.7 D4（4 张）

| 位置 | 内容 | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | 生活照（笔记本 "ADHD-FRIENDLY PLANNER"） | `adhd-planner-light/mockup/M1_hero.jpg` | `a27dfd21`／388,322 | 12 | 已确认 |
| 图 2 | 生活照（"START ANY DAY. SKIP A DAY. START AGAIN."） | `adhd-planner-light/mockup/M2_lowbattery.jpg` | `90899988`／446,519 | 18 | 已确认 |
| 图 3 | 生活照（"WANT TO BUY IT? … FOR 24 HOURS"） | `adhd-planner-light/mockup/M3_impulse.jpg` | `d8acd37a`／364,006 | 12 | 已确认 |
| 图 4 | 总览网格（"ALL 32 PAGES"＋月历格） | `adhd-planner-light/mockup/M4_allpages.jpg` | `79153368`／400,076 | 8 | 已确认 |

### 3.8 P1（6 张）

| 位置 | 内容 | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | 生活照（笔记本 "PARENTS' MOVE COMMAND CENTER"） | `p1-moving-command/listing-assets/01_Main.jpg` | `395c4ded`／504,407 | 13 | 已确认 |
| 图 2 | "WHAT'S INSIDE" 文字页 | `p1-moving-command/listing-assets/02_Contents.jpg` | `d91048c6`／450,213 | 10 | 已确认 |
| 图 3 | "HOW IT WORKS" 文字页 | `p1-moving-command/listing-assets/03_HowItWorks.jpg` | `cc6a05e2`／363,524 | 7 | 已确认 |
| 图 4 | "ALL 43 PAGES" 总览网格 | `p1-moving-command/listing-assets/04_AllPages.jpg` | `7abe5ddd`／609,821 | 9 | 已确认 |
| 图 5 | 生活照（"SEE IT FILLED IN" 已填示例） | `p1-moving-command/listing-assets/05_Example.jpg` | `053e1173`／509,716 | 20 | 已确认 |
| 图 6 | "FILES & SIZES" 文字页 | `p1-moving-command/listing-assets/06_FilesAndSizes.jpg` | `bdcf514c`／322,570 | 8 | 已确认 |

### 3.9 Restart（7 张）

| 位置 | 内容 | 磁盘来源 | SHA（前 8 位）／字节 | MSE | 结论 |
|---|---|---|---|---|---|
| 图 1 | 生活照（笔记本 "WEEKLY PLANNER + RESTART KIT"） | `weekly-restart-kit/listing-assets/M1_hero.jpg` | `5c185865`／378,276 | 12 | 已确认 |
| 图 2 | 生活照（"MISSED A WEEK? RESTART WITHOUT CATCHING UP"） | `weekly-restart-kit/listing-assets/M2_restart.jpg` | `71ee828e`／566,806 | 21 | 已确认 |
| 图 3 | 生活照（"BIG, FUZZY TASK? TRY FIRST STEP"） | `weekly-restart-kit/listing-assets/M3_converter.jpg` | `9c55e681`／390,996 | 12 | 已确认 |
| 图 4 | 生活照（"TYPE IT IN OR PRINT IT"） | `weekly-restart-kit/listing-assets/M4_fillable.jpg` | `dc50180d`／429,279 | 12 | 已确认 |
| 图 5 | "ALL 9 PAGES · ONE SIMPLE SYSTEM" 总览网格 | `weekly-restart-kit/listing-assets/M5_all_pages.jpg` | `6efd263d`／394,417 | 7 | 已确认 |
| 图 6 | "FIVE TOOLS, ONE SIMPLE LOOP" 图解页 | `weekly-restart-kit/listing-assets/M6_five_tools.jpg` | `4d110ad2`／343,564 | 7 | 已确认 |
| 图 7 | "WHAT YOU RECEIVE" 文字页 | `weekly-restart-kit/listing-assets/M7_files_sizes.jpg` | `c5f106e0`／220,595 | 6 | 已确认 |

注：`listing-assets/old-name-backup/M1_hero.jpg` 与现行 M1_hero MSE 仅 4（近乎同一文件），为旧名备份，不作来源认定。

## 4. §5.1 三处核对（任务书核对点 ②③④）

**核对点 ②——Budget Full 图 1 与图 2–5 是否为两个不同封面文件：已确认是。**
- 图 1＝`cover_fullpack_m1_v2.png`：标题 "The Budget / One page, one month"，副文 "20 printable budget pages"，封面行 "FULL PACK · 10 pages"（PDF 794px 主图目视＋MSE 14）。
- 图 2–5＝budget-pin4／pin1／pin2／pin3：内嵌封面标题均为 "The Budget You'll Actually Keep"，副文 "10 printable budget pages"，封面行 "FULL PACK · 10 pages"（磁盘原图全分辨率逐字目视＋MSE 48–51）。
- 标题不同 → 不同封面文件。补充：图 2–5 的 Full 封面与 Budget Full 产品（$3／10 页）口径一致，此处无 D 类问题；与图 1 不同的只是封面文案版本，不是 Full／Starter 错配。

**核对点 ③——Habit Starter 图 2／3／5 配 Full 版封面、图 4 配 Starter 封面：已确认，与 §5.1 第 7／8 项一致。**
- habit-pin1／pin2／pin3 内嵌封面行均为 "FULL PACK · 10 pages"（磁盘原图逐字目视；pin1 "10 printable pages. No app · No subscription · No guilt"，pin2／pin3 同文）。
- habit-pin4 内嵌封面行为 "STARTER · $1 · 2 pages"（副文 "2 pages to start your first streak. 2 頁精簡版，開始你的第一個打卡。"，磁盘原图逐字目视）。
- 落位：Habit Full 图 2＝pin1（Full ✓）、图 3＝pin3（Full ✓）、**图 4＝pin4（Starter ✗——§5.1 #7：Full listing 用了 Starter 版内页封面，与 $3／10 页不符）**、图 5＝pin2（Full ✓）；Habit Starter **图 2＝pin1（Full ✗）、图 3＝pin2（Full ✗）**、图 4＝pin4（Starter ✓，与本 listing 相符）、**图 5＝pin3（Full ✗——§5.1 #8：Starter 图 2／3／5 用 Full 版封面，与 $1／2 页不符）**。
- 交叉核对：两款图 2–5 为同一组 4 个文件（逐对 MSE=0，位置对应 Full[2,3,4,5]＝Starter[2,5,4,3]），故错配成因是同一组 pin 图被原样复用于两款 listing，未按 Full／Starter 区分。

**核对点 ④——2027 Starter 图 2–5 配 Full 版封面：已确认，与 §5.1 第 9 项一致。**
- goals-pin1／pin2／pin3／pin4 内嵌封面行均为 "FULL PACK · 10 pages"（副文 "10 printable goal pages"，磁盘原图逐字目视；SHA 见 §3.6）。
- 落位：2027 Starter 图 2＝pin2、图 3＝pin1、图 4＝pin4、图 5＝pin3，**四张全部配 Full 版封面**，与 $1／2 页的 Starter 产品不符（§5.1 #9：用了对方内页封面）。
- 附带：2027 Starter 图 1＝`newyear-goals-2027/cover_starter.png`（STARTER · $1 · 2 pages），图 1 本身无错配。

## 5. 未确认清单

| # | 未确认项 | 缺什么证据 | 下一步 |
|---|---|---|---|
| U-1 | Savings Full 图 2（繁中文字页）磁盘来源 | 全树 4066 文件最佳匹配仅 `cover_fullpack_tc.png`（MSE 167，未达同一文件阈值；且缩略图内容为文字说明页、非该封面的大标题＋7 格构图） | 在工作区另寻：疑似繁中版 quick-start／使用说明页，可能只存在于产品 PDF 内（`fullpack_10page_A4_TC.pdf` 等）而无独立 PNG；或为已删的 pin 文件。须主聊定是否追查——不影响 §5.1（该图无封面错配问题） |
| U-2 | Savings Full 图 6（竖版 pin 图，存钱封面）磁盘来源 | 全树最佳匹配 147（三者并列：pin14-vacationfund／pin10-ownpace／pin12-freshstart），未达阈值；demo-pack 仅 3 张 Budget 图，无 Savings 文件 | 在工作区另寻：疑似 thread2-pinterest 之外另存的存钱 pin 图，或已删文件。须主聊定是否追查 |
| U-3 | Savings Starter 图 3／图 4 各是哪一张 pin 文件 | — | **已解决（主聊核验补记 2026-11-08）**：图 3＝`thread2-pinterest/pin18-habitstack.png`（标题 "One Box a Day"），图 4＝`thread2-pinterest/pin3-starter.png`（标题 "Try It for $1"）。依据：回包索引表（浏览器全图目视）图 3 标题 "One Box a Day / color it · build the habit"、图 4 标题 "Try It for $1 / 2-page savings challenge starter"，与磁盘原图标题逐一对应（pin18、pin11 已由主聊目视确认标题；pin3 标题见本定稿 §5 原文）。两图不是同一文件——75px 中心裁切缩略图逐像素相同是因为标题栏在裁切区之外，封面区相同；此前“同一文件重复上传”的说法作废。 |

**不属未确认、但须主聊知晓**：
- ~~Savings Starter 图 3 与图 4 为同一文件重复上传（缩略图逐像素 MSE=0），属图库重复，不属 §5.1 缺陷，但第四批换图时可顺带去重。~~【主聊核验补记 2026-11-08：此条作废。两图不是同一文件（见 U-3 已解决），无重复上传问题。】
- Habit Full／Starter 图 2–5 为同一组 4 个 pin 文件复用（逐对 MSE=0），是 §5.1 #7／#8 错配的成因。
- Budget Full 图 1 用的 `cover_fullpack_m1_v2.png` 与 `cover_fullpack.png` 为两个版本（MSE 174）；后者未在线上出现（未作任何一款图 1），疑似被 m1_v2 替换下来的旧版。
- `v2c-02.png` 与 `v2-02.png` 同一文件（SHA 相同），候选去重后为 19 张 distinct 文件。

## 6. 方法与证据等级

- **PDF 实物**：10 份 PDF（`~/workspace/.hatch-browser/outputs/browser-task:b538d895-0373-5855-8d65-7e6874df3724/`，f0–f9，2026-11-08 09:37–09:43），每份 7 页 letter。页 1 含 1 张 794×794 主图（图 1）＋N 张 75×75 filmstrip 缩略图（N＝各款图数：6／5／5／5／5／4／5／4／6／7＝52，与主表 §14 2026-11-06 23:35 行第 ③ 条逐字一致）。缩略图顺序验证：每款缩略图 1 vs 主图 MSE 13–25（同一文件重编码水平），证实 filmstrip 顺序即线上图序。PDF 文本层另核对了 10 款标题＋价格（§2）。
- **像素 MSE（75px，numpy）**：同一文件判定阈值以实测校准——方形原图→缩略图：MSE 1–21；竖版 1000×1500 pin 图→缩略图（中心裁切）：MSE 44–56（goals-pin 95–96，见 §3.6 注）；同模板不同文件：MSE 165–220（Full vs Starter 封面 200–219；cover_fullpack vs m1_v2 174）；不同内容：MSE ＞300（通常 ＞800）。判定线：≤60 已确认（竖版 pin 允至 ≤100，须双射排列＋目视佐证）；＞150 未确认。白页噪声说明：全白页面互比 MSE 可低至 40–300（如 R-L4／v2b-08 反复进入 top-3），故 MSE 须与目视内容结合，单凭数值不认——本定稿所有“已确认”均有内容目视佐证（标题文字逐字对上）。
- **竖版 pin 图结构**：12 张 pin 图均为 1000×1500（上为英文标题＋副文，下为方形封面），Etsy 75px 缩略图取其中央裁切（1000×1000 中段）——以 [sq]（整图压扁）比对 MSE 均 ＞1100，以 [cr]（中心裁切）比对 MSE 44–96，证实裁切方式。裁切区之外的标题栏不在缩略图内，故 U-3 三者无法区分。
- **全树复核**：磁盘池 4066 个 PNG／JPG（ST/ 全树，含 thread2-build、thread2-pinterest、launch-kit、adhd-planner-light、p1-moving-command、weekly-restart-kit、budget-sheets-build 等），每张线上图取 top-3，未确认项为全树最优仍未达阈值者。
- **磁盘原图目视**：habit-pin1–4、goals-pin1–4、budget-pin1–4 共 12 张全分辨率目视，封面行逐字记录（§3.3／§3.4／§3.6）；10 张首图文件与 PDF 主图逐项对照。
- **未用回包索引表**：见 §0 证据说明。逐张截图 i1–i66 未落盘，无法复核；本定稿以 PDF 实物＋全磁盘像素匹配为准，证据等级不低于索引表文字描述。
- **未改动文件**：本定稿只写本文件；比对用中间文件（PDF 提取图、比对脚本）存于 `~/workspace/audit-tmp/quality-overhaul/.u5-scratch/`（临时），定稿后由父代理决定是否清理。

## 7. 主聊核验补记（2026-11-08，映射定稿交付后独立核验）

核验通过项（与源头逐字一致）：① 10 份 PDF 实物结构——抽查 f0（Savings Full）含 1 张 794×794 主图＋6 张 75×75 缩略图（pdfimages 核对），与定稿 §6 所述一致；② D4 M1_hero.jpg SHA `a27dfd21…`、Restart M1_hero.jpg SHA `5c185865…`，与定稿 §2 逐字一致；③ 两张封面匹配（cover_fullpack→Savings Full 图 1、cover_starter→Savings Starter 图 1）与浏览器回包图 1 描述、闭合报告 §2.3 逐字一致；④ §5.1 三处核对与浏览器回包核对点 ②③④逐字一致。

U-3 已解决（见 §5 表内）：图 3＝pin18-habitstack（标题 "One Box a Day"），图 4＝pin3-starter（标题 "Try It for $1"）。核验方法：回包索引表标题（浏览器全图目视）＋磁盘原图标题目视（pin18、pin11 已由主聊目视确认标题；pin3 标题见定稿 §5 原文）。75px 中心裁切缩略图逐像素相同不等于同一文件——标题栏在裁切区之外。§0 总数与 §5“同一文件重复上传”一说已同步更正（50 个位置文件级已确认／46 distinct／2 个未确认）。

定稿结论采信：映射定稿整体采信，§5.2 第 3 项记为**闭合**（附 U-1、U-2 两处磁盘来源未找到，不影响 §5.1 与第四批——两图均无封面错配问题）。

—— 映射定稿完 ——
