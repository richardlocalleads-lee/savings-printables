# 任务书 — 第四批次：17 款无直达 pin 补 pin＋listing 图片 v1 审计（草稿）

- **文件**：`~/workspace/audit-tmp/quality-overhaul/TASK-PACKAGE-BATCH4-2026-11-08.md`
- **状态**：已批复（Lee 2026-11-08 18:56 本聊批准整体＋执行方）。**待派发；派发后执行。**
- **执行方**：第四方。**验收方**：主聊（按 §5 逐项验收；图包回来先审，审过才发 pin、才换 listing 图）。【执行方裁决（主聊定，Lee 批准）：第三方已承第一批 D 组 14 张＋P0 表催补，第四批 17 款新 pin＋17 款 listing 审计再压过去会单线全押第三方；第四方第二批 B 零返工已证明能按 v1 执行，且本线当前空闲；两线并行、互为独立校验。】
- **背景**：质感改造任务包 `TASK-PACKAGE-OVERHAUL-2026-11-08.md` §1 已定第四批＝17 款无直达 pin 的款各补 1 张新 pin＋17 款 listing 图片按 v1 审计。§5.3 已定 B（Lee 2026-11-08 17:09：listing 层亦按 v1 全面执行）。§5.2 闭合报告 `SECTION-5.2-CLOSURE-DRAFT-2026-11-08.md`（2026-11-08）已出：41 款中 6 款 BRIEF-6 封面已核，**35 款**须 v1 逐款近看（任务包原文称 34 款，第 7 个排除项无文件指明，工作集按 35 款列；若 Lee 指明第 7 款，补充执行单减 1 款）。
- **依据文件**：质感规范 v1.1 `ST/质感专项/SettledDays质感规范-v1-2026-11-08.md`（执行标准全文，含 §5.8 红像素机检豁免两条裁决）；`ST/质感专项/定版样板三张审计-2026-11-08.md`（三型尺）；`ST/质感专项/量产三批十三图审计-2026-11-08.md`；§5.2 闭合报告（见上）；归因表 `ST/launch-kit/PIN-FORMAT-ATTRIBUTION-2026-11-06.md`（新 pin 画板按该表画板列）；11-06 全量检查报告 `~/workspace/audit-tmp/listing-image-review-2026-11-06/LISTING-IMAGE-FULL-REVIEW-REPORT-2026-11-06.md`（截断／口径四类原判）。

## §0 红线与边界（执行方须遵守）

1. **不碰 Etsy 页面作输入**（ToS 红线）：备料与评估只用本任务书列明的本地文件；listing 实况核对走 Lee 的 Mac＋原热点场，不得用执行方自己的浏览器登录 Etsy。**线上实况抓图由主聊提供**（U5 补证：10 个 listing 线上图库实况，见 §1 注）。
2. **Publish 与发 pin 归主聊**：执行方只备图、不发 pin、不点发布。新 pin 的删旧发新由主聊执行（云端浏览器）；listing 换图走热点场、Lee 亲手点 Publish。
3. **不改 canonical 文件**：执行过程不改信号池、主状态表、MEMORY、归因表原文；读数与新 pin 记录按验收后另起行记。
4. **不做 AI 生成／修改**：新图一律用真实产品页截图或程序重绘（PIL 等）制作，**不使用任何 AI 图像生成或 AI 修改**；制作记录须逐图写明制作方式（真实页截图／程序重绘）。Etsy 平台内容不得进入任何 AI（ToS 红线）；本任务书的源文件均为 Lee 自有产品文件，制作只用这些文件。
5. **诚实口径不变**：图内数据须与源文件逐项核对；不得把“产品真实＋AI 场景”宣传为纯手工感；S1 披露句等既有文案规则不动。
6. **后续批次不得自行启动**：本任务书只含第四批 17 款；做完即止，补充执行单（附录）须主聊另行派发。
7. **不得在交付前预写“已通过主聊验收”**：验收结论只由主聊写；执行方交付包只写自检结果。

## §0.3 样板尺与色值（执行前须知）

- 三型尺已冻结：**单页填实（D4W）／双模块（S-010）／复杂表格（HOMEINV）**，三型并存不强行统一；标记规则＝**零覆盖层批注**（无红圈／箭头／编号／装饰性手绘勾），内容层真实填写保留；主体跨度 ≥90%、下半不留空；1000×1500；标题带＋页脚沿用现行样式。
- **8 色表已冻结**：学习青蓝 #1F6E8C、存钱绿 #2F7D32、预算深蓝 #1B3A6B、身后事墨绿 #1E4D3B、婚礼酒红 #7B2231、输入蓝 #1F4E9C、完成绿 #2E7D32、提醒橙 #C05E10。色值核验以众数色为准。功能色与品类色撞色时以功能色为准、品类色让位。
- 红像素机检口径（v1.1 §5.8）：批注红近色（与 (208,43,28) 欧氏距离＜60）＋主体区严格红（R＞150、G＜110、B＜110 且 R−G＞60、R−B＞60）均为 0；品牌色带及白字抗锯齿不计；功能色豁免窄限三支 canonical 功能色（输入蓝 #1F4E9C、完成绿 #2E7D32、提醒橙 #C05E10）及其抗锯齿混合色；源图固有红豁免须三条件齐备（红 100% 在源图区内、制作方新增区贡献 0、源图原尺寸计数与复算逐字一致）。

## §1 范围：17 款（无直达 pin 的款）

每款两项工作：**(a) 新 pin 1 张**（1000×1500＋100px 缩略图）；**(b) listing 图片 v1 审计**：逐张核该款全部 listing 图（截断／口径／密度／骨架／用色／页脚／标题），出审计记录；首图不合 v1 的重做首图，其他图不合 v1 的列入改项清单（随补充执行单走，不擅自重做全套）。

| # | 产品／Listing ID | 现行首图（§5.2 闭合报告 §1） | 备注 |
|---|---|---|---|
| 1 | Christmas Kit／4600874500 | M1 hero（磁盘文件名未确认） | 首图文件名未确认，审计以线上实况为准 |
| 2 | D5／4601773193 | M1 hero（磁盘文件名未确认） | 同上；§5.1 第 4 项（M6_inside.jpg 截断）落在本款，执行时一并做 |
| 3 | S-006／4601983813 | M1 hero（磁盘文件名未确认） | 同上；live 视频已确认为 Take 4，不动视频 |
| 4 | 婚礼／4604186625 | 主图 Overview（Budget Overview） | 线上只有 1 张静态图＋1 视频（已闭合）；binder 方向另行走 BRIEF-8，不属本批 |
| 5 | 年度一期／4604232532 | Start Here 指南页 | §5.1 第 5 项（Year at a Glance “Variable spendin”截断）落在本款，执行时一并做 |
| 6 | D3／4600362280 | M1 hero（候选 `cover_biweekly.png` 未确认为线上图 1） | §5.1 第 3 项（listing_split.png 截断）＋第 6 项（封面“14 template pages”口径）落在本款，执行时一并做 |
| 7 | Savings Full／4598465559 | 未确认（第 3 项） | **C 类**：首图以线上实况为准，磁盘候选仅作对照；候选见 §5.2 报告 §2.3（thread2-build 8 张） |
| 8 | Savings Starter／4598538460 | 未确认（第 3 项） | **C 类**，同上 |
| 9 | Habit Full／4598582424 | 未确认（第 3 项） | **C 类**，同上；§5.1 第 7 项（图 4 用了 Starter 版内页封面）落在本款，执行时一并做 |
| 10 | Habit Starter／4598576567 | 未确认（第 3 项） | **C 类**，同上；§5.1 第 8 项（图 2／3／5 用了 Full 版内页封面）落在本款，执行时一并做 |
| 11 | Budget Full／4598655675 | 未确认（第 3 项） | **C 类**，同上 |
| 12 | Budget Starter／4598659063 | 未确认（第 3 项） | **C 类**，同上 |
| 13 | 2027 Full／4598684850 | 01 主图（磁盘文件名未确认） | 首图文件名未确认，审计以线上实况为准 |
| 14 | 2027 Starter／4598687922 | 未确认（第 3 项） | **C 类**，同上；§5.1 第 9 项（图 2–5 用了对方内页封面）落在本款，执行时一并做 |
| 15 | D4 ADHD Planner／4600823259 | 未确认（第 3 项） | **C 类**，同上；候选 p-01～p-04（`ST/adhd-planner-light/mockup/renders/`） |
| 16 | P1 Parents' Move／4600844093 | 未确认（第 3 项） | **C 类**，同上；候选 p-01～p-04（`ST/p1-moving-command/listing-assets/renders150/`） |
| 17 | Restart／4600838577 | 未确认（第 3 项） | **C 类**，同上；候选 L-1～L-4（`ST/weekly-restart-kit/internal-evidence/page-renders/`） |

**§5.1 重叠说明**：§5.1 确定改 10 项中落在本批 17 款范围内的 7 项（上表“执行时一并做”），由本批执行，不另立项；§5.1 另 3 项（S-023 图 1、S-023 图 3、S-023 视频 S2 重建）属有 pin 款，不属本批，随补充执行单走。

**C 类 10 款特别说明**：首图文件名尚未确认（§5.2 第 3 项未闭合：20 张磁盘候选无法钉到 10 个 listing）。本批任务书派发时，主聊随附 U5 线上实况抓图（10 个 listing 图库实况）；执行方以线上实况图 1 为准做新 pin 与审计，磁盘候选仅作对照，**不得把候选直接写成“各款图 1”**。U5 补证未到之前，C 类 10 款不得先行开工。

## §2 执行标准（逐项执行，审计逐项核）

与任务书 A §2 同口径，适用本批 17 款（核心新品 pin 以 D3 为目标；其余普通 pin ≥D2）：

1. **画布**：1000×1500 px（2:3）。标题带占画布高 10%–14%，页脚条占 4%–6%，其余为主体。四周留边一致，任一侧不小于画布宽的 6%（60 px）。卡片之间、分区之间沟距一致，不小于画布宽的 2%（20 px）。
2. **三型选型**：按产品内容在三型里选——可打印类走真实页面截图（单页填实或双模块），表格类走 HOMEINV「特写＋摘要」原生重绘。拼图上限 4 页（2×2）；每页显示宽度不小于画布宽的 45%；每页关键正文不小于 §2.7 正文字号下限；达不到则改选一页最强内容做主图。
3. **选页**：禁说明页／目录页／封面页作首图；选产品最强的一页内容（真实产品页／填好真实数据的表格／完整速查表，三者取其一）。**§3.2 裁决备查（Lee 授权主聊定，2026-11-08）**：说明页＋空白表的混合页按说明页计，不得作图 1；空白表须有已填示例才可作图 1（例：S-023 Walkthrough 页算说明页，图 1 改用 25 行已填示例表；S-023 不在本批 17 款内，随补充执行单走）。
4. **密度**：普通 pin ≥D2；核心新品 pin 以 D3 为目标。须填演示数据（虚构人物与虚构数据，不得用真实个人信息）做到 D3 的，执行方先做；包内无已填示例页、冲 D3 须另做一页已填演示的，属新生产，**不得擅自生产**，在制作记录中写明建议、报主聊定夺。
5. **痕迹**：只用白名单四类（规范 §4.1）；黑名单四类禁用（§4.2）；混合痕迹须答得出“在帮哪条信息说话”，按“混”记录。
6. **用色**：一图一主色；系列内沿用同一主色；饱和色只给重点；功能色按含义使用（可填／输入＝浅蓝填充；提醒／注意＝橙；完成／达成＝绿），首次出现须有文字或图例讲明含义。品类色按 §0.3 冻结 8 色表：存钱绿（Savings 系、2027 系）、预算深蓝（Budget 系、D3、D5、年度一期）、婚礼酒红（婚礼）、学习青蓝（D4）、身后事墨绿（不适用本批）。功能色与品类色撞色时以功能色为准。
7. **字号**：标题字号不小于正文字号的 2.2 倍；正文最小字号不小于基准画布宽的 2%（1000 px 宽下 20 px）。**该下限为暂定阈值**：全页截图路线点开后可读的前提下可到约 14–16 px（定版样板 D4W／S-010 同一结构性取舍，第一批审计已接受），须在制作记录中披露实际字号。
8. **红像素口径**：按 §0.3（v1.1 §5.8）。执行方出厂自验按此口径计数并记录。
9. **栏头与产品一致**：栏头须与产品字段一致，不得改名、不得重定义字段。披露过的标准缩写与有理由的省列可以；**未披露的省列不可以**——凡省去产品原表的一列，须在制作记录中逐项写明省了哪列、为什么。
10. **演示数据**：空白模板先填演示数据再成图；日期须对真实日历（用 `date -d` 核对星期）；金额须能复加；合计须与分项闭合。禁 Lorem ipsum、乱码、全 0.00、Habit 1／2／3 类占位作主视觉。
11. **标题带**：一个标题＋一句主题承诺，不放卖点堆叠、不放价格、不放第二标题。页脚条按样板固定模板：品牌名 SettledDays＋系列／产品识别＋主色条＋固定位置。
12. **自检**：缩到约 100 px 宽，三检（标题读得出／主题说得清／只有一个视觉重点）全过才算通过；不过先改标题、再改主体选页与构图，不得靠加装饰补救。
13. **核数**：数字、金额、日期、合计逐项对源文件；收尾边框须完整闭合（第一批审计教训：只数行数不验边框不算验过）。

## §3 逐款执行指令与源文件清单（已补齐，2026-11-08）

**执行指令**：先目视现行首图（线上实况 U5 抓图，随本包附送）定最强页，再按 §2 做新 pin；listing 图片逐张 v1 审计，首图不合即重做。**U5 线上实况抓图已随附，C 类 10 款可开工**（§1 注“等 U5 到齐后开工”的条件已满足）。

**婚礼**：本批只做 pin＋图片审计，binder 内容本身不属本批；BRIEF-8 活页夹文件另行，不随本包。

### 3.1 逐款源文件清单（17 款；路径以 `~/workspace/cross-border-micro-digital-business/` 为基准，`steel-thread/` 即 `ST/`）

#### 1. Christmas Kit／4600874500
- **上架包**：
  - `steel-thread/christmas-budget-kit/listing-assets/LISTING-PACK.md`（6,670 B，SHA-256 `e4a335037b6a336477fc110a4a6edc7a800561e01b7853f95d8562a57d92f5ce`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/christmas-budget-kit/buyer-files/Christmas-Budget-Kit-A4.pdf`（42,472 B，SHA-256 `629c3f56e434cc3082989d44a0f7dac230aad871cad6496a0496d85791f4f7f7`）

#### 2. D5 Low Income Savings Challenge／4601773193
- **上架包**：
  - `steel-thread/d5-build/LISTING-PACK.md`（11,982 B，SHA-256 `1bb1d772ecbe34af1eed70ef6227cec0694dc8c0ad90eb2bcc88e78e7087a016`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/d5-build/buyer-files/Low-Income-Mini-Challenges-A4.pdf`（58,654 B，SHA-256 `4f74f224c2308a85576e1a9e27e9b7248ab43a097274e73f037b0d3e1adafcd3`）
  - `steel-thread/d5-build/buyer-files/Low-Income-Mini-Challenges-A6.pdf`（59,296 B，SHA-256 `e80068a5f05a5ebcaf40228042af4e41b6cb4dfbab86e2cf7b957d6c53a51448`）
  - `steel-thread/d5-build/buyer-files/Low-Income-Mini-Challenges-Letter.pdf`（57,250 B，SHA-256 `e042f1ae197c828dbf4cb1a2f1240948d13096a837d96dea79886a7a6b602fa9`）

#### 3. S-006 Christmas Savings Challenge Spreadsheet／4601983813
- **上架包**：
  - `steel-thread/s006-build/LISTING-PACK.md`（10,223 B，SHA-256 `54d3e6a1d8a2bfe23529b3df0dc57b5854588449492becf8a69c1c350caadadf`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/s006-build/buyer-files/Christmas-Countdown-Checkoff-A4.pdf`（29,974 B，SHA-256 `d6a0550b1ce1941727f3a160a8d80e95f8fb73984ea7fad6e73098624e55eae9`）
  - `steel-thread/s006-build/buyer-files/Christmas-Countdown-Checkoff-Letter.pdf`（29,823 B，SHA-256 `d091863b4f151ccf18a7faec4200394ec79876fec8252ae257c7a131f158c1f3`）
  - `steel-thread/s006-build/v2/Christmas-Countdown-Savings-v2-2026-10-24.xlsx`（11,515 B，SHA-256 `160decd79f7a003cc245181c421b91b6183842c42ef707f1e42b18cfff68bf70`）

#### 4. 婚礼 Wedding Budget Planner／4604186625
- **上架包**：
  - `steel-thread/wedding-build/WEDDING-LISTING-PACK-2026-10-26.md`（12,927 B，SHA-256 `6c9f91c3c025ca9fbac15abc2959a8fcc0d3fd9193e2ae1129b6de88b8bfd30a`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/wedding-build/Wedding-Budget-Master-Blank.xlsx`（27,355 B，SHA-256 `7881481232d7ea2001353cc2ef5b8fbb74622cdf77000d511691d1e89c8d366a`）
  - `steel-thread/wedding-build/Wedding-Budget-Filled-Example-Fictional.xlsx`（27,742 B，SHA-256 `06d3d89686f31a2aa03547f3ef0bdd1b7cb368d3b5d1c38da02717af48591d8f`）
  - `steel-thread/wedding-build/Wedding-Print-Companion-A4.pdf`（31,173 B，SHA-256 `a43c4daececc9509e302f6b3c2b5a326fa55d367115b0946eeea40670ef92dbf`）
  - `steel-thread/wedding-build/Wedding-Print-Companion-Letter.pdf`（30,540 B，SHA-256 `b79cb863309400577834c9843e7e56cb87655a7bf25da599d7e7cb25c730dc4d`）
  - `steel-thread/wedding-build/Wedding-Budget-Start-Here.pdf`（32,432 B，SHA-256 `5d1a25f7f161dcd0c31f9aeb3e20c3f35585739f534ee625f625f92cfdb59915`）

#### 5. 年度一期 Monthly Budget Spreadsheet／4604232532
- **上架包**：
  - `steel-thread/budget-sheets-build/LISTING-PACK-DRAFT.md`（9,031 B，SHA-256 `f5745643d3c9751f83674c7fbd6f3b885d57f6ae90ce79899914a27d34c80f2f`）
  - `steel-thread/budget-sheets-build/ANNUAL-LISTING-DESCRIPTION-2026-10-27.md`（5,252 B，SHA-256 `cc13798e9028798936243e527dbce0dc6297f0f7176cba59fc362096fe048301`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/budget-sheets-build/Monthly-Budget-Spreadsheet.xlsx`（40,135 B，SHA-256 `c68c461d8d5e4f39a4864cf8c701fe48a7bbd13e2dd0f9c84a0f117d8067b598`）
  - `steel-thread/budget-sheets-build/Monthly-Budget-Filled-Example.xlsx`（40,795 B，SHA-256 `b9c5e280304305cc2039ef9cf70cc7b289a84897928c960ae3cd7595191b63db`）
  - `steel-thread/budget-sheets-build/Monthly-Budget-Start-Here.pdf`（32,531 B，SHA-256 `1cea5a864635a88779209eab3ea8205bf6a3bf8f035b419e4d90c384273ad5ae`）

#### 6. D3 Biweekly Paycheck Budget Planner／4600362280
- **上架包**：
  - `steel-thread/biweekly-paycheck-planner/LISTING-PACK.md`（5,669 B，SHA-256 `45ecd1a040a2103363e1d33f163a2ff510f8f4ac56d7b96e5dee05683577f95f`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/biweekly-paycheck-planner/biweekly_fullpack_A4.pdf`（84,922 B，SHA-256 `725ae2fba4ab42e9bd5354efff9f772664099e2d02c58df610b110366c879b0f`）
  - `steel-thread/biweekly-paycheck-planner/biweekly_fullpack_Letter.pdf`（84,405 B，SHA-256 `a598ced7aed3e32b5ff04272a41054c2392ef7f545808d7b9878435379518b46`）

#### 7. Savings Full／4598465559
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/fullpack_10page_A4_TC.pdf`（74,977 B，SHA-256 `59c628aec9b39bf18fecf986a93f2eac568a49153c99b5954549ab8cdececacf`）
  - `steel-thread/thread2-build/fullpack_10page_Letter_TC.pdf`（74,331 B，SHA-256 `9733cd953686176661ec1bbf365e6ee63e32084dd94d2a1bec3215a2364df098`）
  - `steel-thread/thread2-build/fullpack_10page_A4.pdf`（17,813 B，SHA-256 `f18004b040c378f5c838e53960ef99a986fc459a703fa0273eadd65e7d9adcfd`）

#### 8. Savings Starter／4598538460
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/starter_2page_A4_TC.pdf`（34,020 B，SHA-256 `51ef3fdd8aab8b4cf578294c02ac4e84371d3a5a09b1c14834ebfac6d649b1ae`）
  - `steel-thread/thread2-build/starter_2page_Letter.pdf`（4,707 B，SHA-256 `021efa00bcb0de183e118b1c0cf49e352c09f08019efe95a0f6c813fd35459ff`）

#### 9. Habit Full／4598582424
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/habit-tracker/fullpack_10page_Letter.pdf`（76,423 B，SHA-256 `9dbbb7a317ef6559b986f7692868e68182d6f62066e1a0aeb9b44ac29ff6fac5`）
  - `steel-thread/thread2-build/habit-tracker/fullpack_10page_A4.pdf`（76,803 B，SHA-256 `bba0139e734221b9000d7d20182d6810e2e22ca2f44d1960b2e47a73323a517d`）

#### 10. Habit Starter／4598576567
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/habit-tracker/starter_2page_A4.pdf`（35,446 B，SHA-256 `955e5b16aaf02fc4a250449c9bb28632a4b33c30fa9ef7ebc71cf39a013b9e27`）
  - `steel-thread/thread2-build/habit-tracker/starter_2page_Letter.pdf`（35,374 B，SHA-256 `2e3d0137607e2a40e29139b8edb3b204290fa476925c6d7eea7c58b58ea9d018`）

#### 11. Budget Full／4598655675
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/budget-planner/fullpack_10page_A4.pdf`（75,948 B，SHA-256 `ebae47e943c3e7b57fdf1f40bfa60f5fa8e75be0c939e7a0204234099be90a1b`）
  - `steel-thread/thread2-build/budget-planner/fullpack_10page_Letter.pdf`（75,478 B，SHA-256 `d54e6425169208c1b27872f0df8acd06999b8f193ae8da552b6b6e3815dfe81c`）

#### 12. Budget Starter／4598659063
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/budget-planner/starter_2page_A4.pdf`（39,934 B，SHA-256 `028d83b76d1bd7514b55899d4c939b3d2074292fa0c6dcf5c70b815b7b4dea92`）
  - `steel-thread/thread2-build/budget-planner/starter_2page_Letter.pdf`（39,836 B，SHA-256 `92f08ad9cad8600ce42060cd6241da150d05405eeb59c390286bcf5619347e68`）

#### 13. 2027 Full／4598684850
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/newyear-goals-2027/fullpack_10page_Letter.pdf`（75,605 B，SHA-256 `306f08b349be4ac321f02a7a67a50914300d31e43257498937b33ada2f322d95`）
  - `steel-thread/thread2-build/newyear-goals-2027/fullpack_10page_A4.pdf`（76,024 B，SHA-256 `d6d409ebad2ffc56964babc0cca06bce8766b260d505c57f35ee94fbff709ee2`）
  - `steel-thread/thread2-build/newyear-goals-2027/dated-12p-2026-10-24/dated-12p-2027_A4.pdf`（37,396 B，SHA-256 `803caa8d153504b56f6541ba8a82dc072b026d5b143523ef936243e37a172860`）
  - `steel-thread/thread2-build/newyear-goals-2027/dated-12p-2026-10-24/dated-12p-2027_Letter.pdf`（36,782 B，SHA-256 `fa267d10d63a887d8791ff853223100a90d16495990fc934964a4ab3f0ac2ee5`）

#### 14. 2027 Starter／4598687922
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/thread2-build/newyear-goals-2027/starter_2page_Letter.pdf`（34,355 B，SHA-256 `6abc16a79c907169c1677ef8c49c7995767bcc12b5ea3fa646b2d19767e6888c`）
  - `steel-thread/thread2-build/newyear-goals-2027/starter_2page_A4.pdf`（34,444 B，SHA-256 `a441f34c1f9f52fb6e3368b76b1045a8adfc4cafa5febafdd783a134bf443686`）

#### 15. D4 ADHD Planner／4600823259
- **上架包**：
  - `steel-thread/adhd-planner-light/LISTING-PACK.md`（4,884 B，SHA-256 `6f7478a755dd56586257dea6f439d516809b805ef8b6e2bdb174a960953cc77b`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/launch-kit/renamed-assets/pdfs/d4-adhd-light/adhd_light_EN_A4.pdf`（124,021 B，SHA-256 `2b40165f1e76a5c0a47dc52528adadd4fd0e2f160ed3da2d336ae0b231d34e4e`）
  - `steel-thread/launch-kit/renamed-assets/pdfs/d4-adhd-light/adhd_light_EN_Letter.pdf`（120,605 B，SHA-256 `d1a9188ea33d7b780152c76044e23bd1a730594c94927a8e7af3d260add9b144`）
  - `steel-thread/launch-kit/renamed-assets/pdfs/d4-adhd-light/adhd_light_TC_A4.pdf`（274,701 B，SHA-256 `24abfc6f13a15e2102d0e420aa2295d2b79a2fc7b1e30fce14d897d7eb6ba5ff`）
  - `steel-thread/launch-kit/renamed-assets/pdfs/d4-adhd-light/adhd_light_TC_Letter.pdf`（271,288 B，SHA-256 `ce647531b7b3ee4244874c2492bc7603efc509a7deb33c274cb3d817979c8fa8`）

#### 16. P1 Parents' Move Planner／4600844093
- **上架包**：
  - `steel-thread/p1-moving-command/LISTING-PACK.md`（7,960 B，SHA-256 `59596da09d81c4e39fe08c4c60220a9ac0fa777e6b58662d5c5235d77c2d13fa`）
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/p1-moving-command/buyer-files/Parents-Move-Command-Center-A4.pdf`（646,561 B，SHA-256 `0d41623c0fd48ddc1a9c7f1ca666d3e8badb0bc3cb1141b1225c79b3157f127a`）
  - `steel-thread/p1-moving-command/buyer-files/Parents-Move-Command-Center-Command-Sheet.xlsx`（11,567 B，SHA-256 `9672a6e98e8addfbf57a7fb5bc4070ec80941a43381dd6b4eb389ec6d9decb3a`）
  - `steel-thread/p1-moving-command/buyer-files/Parents-Move-Command-Center-EXAMPLE.pdf`（34,103 B，SHA-256 `9e42e1f7b23414e5a08546af8b65f4079c8007464548542b38d64545cc1d9b64`）
  - `steel-thread/p1-moving-command/buyer-files/Parents-Move-Command-Center-Letter.pdf`（635,383 B，SHA-256 `8f4fbf99bc371512d2904b09cee8ede74f76d5fe40c38200615e63aa55de5e49`）
  - `steel-thread/p1-moving-command/buyer-files/PERSONAL_USE_LICENSE.txt`（861 B，SHA-256 `5dd291a9a3f17147512364186476d0c8f8c9e1ac0ff59f0bf4b8bca6ab6dcfd4`）

#### 17. Restart Weekly Planner／4600838577
- **上架包**：无单款包文件，用共用源文件（§3.2：wave1 TITLE-TAG-PACK／DESC-PACK；另见同节描述存档）。
- **产品文件**（买家档，与 Etsy 在售文件逐字节核对过，见 §3.3）：
  - `steel-thread/launch-kit/renamed-assets/pdfs/weekly-restart-kit/Weekly-Restart-Kit-A4.pdf`（158,402 B，SHA-256 `db9b77e2956906fa6dbad58ff98f598cc6cc66bbe99c3f43e3974a0a56b9d99d`）
  - `steel-thread/launch-kit/renamed-assets/pdfs/weekly-restart-kit/Weekly-Restart-Kit-EXAMPLE.pdf`（32,920 B，SHA-256 `b230f10209359d485aba1ac0987df8ff4bc946f4bd5fdf86feb00a8666989c0f`）
  - `steel-thread/launch-kit/renamed-assets/pdfs/weekly-restart-kit/Weekly-Restart-Kit-Letter.pdf`（154,981 B，SHA-256 `5c9540999c73b4f42141199987fe9170469b7fd85c4244af03ab9a2389e995ad`）
  - `steel-thread/weekly-restart-kit/buyer-files/PERSONAL_USE_LICENSE.txt`（824 B，SHA-256 `1cf93fa757e7033df18d9b9b546a1b31982adc38bf06a5623d6e8f1eb1528ee3`）

### 3.2 共用源文件（随本包附送，各款共用）

- **wave1 上架包（Etsy 标题／标签／描述总包）**：
  - `steel-thread/launch-kit/wave1/TITLE-TAG-PACK.md`（12,737 B，SHA-256 `c9d10b2f172f0a38c488ced226fd31d75768049c87fb51a75f90d57580c360d6`）
  - `steel-thread/launch-kit/wave1/DESC-PACK.md`（35,564 B，SHA-256 `9a83229d10a1daeb5d43f67b306fabc60be706bbb992383531bde7201d20da1d`）
  - `steel-thread/launch-kit/wave1/SHEETS-PIN-PACK.md`（20,839 B，SHA-256 `8028bad07cd173adee44728a2bba0c0b187dee99fb633596dea1a6387440b44f`）
- **各款描述实况存档（2026-10-27／28 live 实读）**：
  - `steel-thread/launch-kit/wave1/KIT-DESCRIPTION-LIVE-ARCHIVE-2026-10-27.md`（5,451 B，SHA-256 `3f2b306fd0bd3ab527e5a7f21bb580df113f4aaed56abe938408d7f47488184f`）
  - `steel-thread/launch-kit/wave1/S006-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（1,014 B，SHA-256 `dbdc9c0402ba0e4864ebd8908b51a2d72cb3cd836c372a4d8f897eed13fab3c4`）
  - `steel-thread/launch-kit/wave1/D3-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（3,380 B，SHA-256 `45a92866d7b9bc5d3bd5cfccd7180f5941def148a4852888bfe9645881d99de6`）
  - `steel-thread/launch-kit/wave1/SAVINGSFULL-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（2,797 B，SHA-256 `c7e3e6988f5144222bc718167e6967a7a8aa0099b561f341092b0b83036484b9`）
  - `steel-thread/launch-kit/wave1/HABITFULL-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（3,021 B，SHA-256 `41780a24f6c235466a75541ae6e6ae207a103cdf6d9131f162623c6a300840d0`）
  - `steel-thread/launch-kit/wave1/BUDGETFULL-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（4,012 B，SHA-256 `288bfac8fdcde2a1331e0253d28cfd981dffdedee6c8a9e809e441782fdd4c81`）
  - `steel-thread/launch-kit/wave1/2027FULL-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（3,381 B，SHA-256 `4acd37b582a3882e6df04a7e0e5f392b0eb906eb43fba514111b8893c5b34472`）
  - `steel-thread/launch-kit/wave1/P1-DESCRIPTION-LIVE-ARCHIVE-2026-10-28.md`（697 B，SHA-256 `6ce46ca21299440cbccdcd053cd8165211638fc7d7be95c88cb170b14e52b3f7`）
- **U5 线上实况抓图（10 份 PDF，C 类 10 款权威图 1 依据，见 §1 注）**：原文件 `~/.hatch-browser/outputs/browser-task:b538d895-0373-5855-8d65-7e6874df3724/browser-page-…-N.pdf`（实际路径 `~/workspace/.hatch-browser/outputs/…`），本包内改名 `u5-live-<款>.pdf`，SHA 不变：
  - `u5-live-savings-full.pdf`（原 `browser-page-20261108T093708.877313791Z-0.pdf`，1,086,626 B，SHA-256 `c0e02bed872520b6517395cc6f2585f9fc51446a5fded3bf46d0a431c6f774a7`）
  - `u5-live-savings-starter.pdf`（原 `browser-page-20261108T093827.572562267Z-1.pdf`，1,080,525 B，SHA-256 `39bef175d7f1d9632c486819d8a60958d9f6e336fb3dbcd073ba81bb7eedf6dc`）
  - `u5-live-habit-full.pdf`（原 `browser-page-20261108T093850.810213566Z-2.pdf`，1,102,590 B，SHA-256 `07a528613f88cc2c64cff47af4864c7c73907a17cfd8ebf8abb788062ea19368`）
  - `u5-live-habit-starter.pdf`（原 `browser-page-20261108T093925.313724017Z-3.pdf`，1,092,877 B，SHA-256 `7bbfaee0bcb364cfd8d2511641444d3082912784ec6f69e0c690fd4c9f265307`）
  - `u5-live-budget-full.pdf`（原 `browser-page-20261108T093957.838456138Z-4.pdf`，1,105,318 B，SHA-256 `d5e55342bee6b49b90773199b46256aebe3b6b38087b2023667428fbb336b63e`）
  - `u5-live-budget-starter.pdf`（原 `browser-page-20261108T094048.024013148Z-5.pdf`，1,120,996 B，SHA-256 `ceb39d0eeedb57aebaaec4bf01404b1ead5508963ea0a3f3d7f789a24c36b207`）
  - `u5-live-2027-starter.pdf`（原 `browser-page-20261108T094124.829008267Z-6.pdf`，1,099,826 B，SHA-256 `1588945468d13b50135f71ef520530f17cacb34650aa996e5cfd571d17d46f5f`）
  - `u5-live-d4.pdf`（原 `browser-page-20261108T094156.190212590Z-7.pdf`，2,061,596 B，SHA-256 `4f2a7a4ce347baab545d5d3f5ecd65535348bf4e4df3f67ff1c5121302b5cbff`）
  - `u5-live-p1.pdf`（原 `browser-page-20261108T094226.728431722Z-8.pdf`，1,901,439 B，SHA-256 `3a3e33231988294624076ff5fa555b2a52a7cd4be9ae627dfc8349f66cfdba4f`）
  - `u5-live-restart.pdf`（原 `browser-page-20261108T094318.773031249Z-9.pdf`，1,599,674 B，SHA-256 `4cfca6ceffafb9ef295071b8d8ec9c985fe2ce6d6e65209ef95ce88bb9218896`）

### 3.3 核对说明（清单编制时已逐项核过）

- 字节核对基准：`audit-tmp/pack-swap-2026-11-08/SHOP-WIDE-FILE-CHECK-2026-11-08.md`（2026-11-08 Etsy 编辑器实读：文件名＋kb）。除下述三项外，全部产品文件字节与该记录逐字一致。
- **S-006 xlsx**：Etsy 在售 `Christmas-Countdown-Savings.xlsx` 为 11.51 kb；磁盘 `s006-build/buyer-files/Christmas-Countdown-Savings.xlsx` 仅 9,645 B，与在售不符，**未采用**；在售版是 `s006-build/v2/Christmas-Countdown-Savings-v2-2026-10-24.xlsx`（11,515 B），磁盘文件名与 Etsy 显示名不同，以字节为准采用 v2。
- **D4**：Etsy 在售 4 档与 `launch-kit/renamed-assets/pdfs/d4-adhd-light/` 的 4 份逐字节一致；`adhd-planner-light/` 根目录同名 4 份各大 ~300 B（后渲染版，非在售版），未采用。
- **Restart**：Etsy 在售 3 份 PDF 与 `launch-kit/renamed-assets/pdfs/weekly-restart-kit/` 的 3 份逐字节一致；`weekly-restart-kit/buyer-files/` 内同名 3 份为旧版（小 ~10 kb），未采用；LICENSE 取 `weekly-restart-kit/buyer-files/PERSONAL_USE_LICENSE.txt`（824 B，与在售一致）。
- **Christmas Kit**：Etsy 在售仅 1 档（A4 PDF）；磁盘 `christmas-budget-kit/buyer-files/` 内另有 Letter 版与 LICENSE，未上架，不在清单内。
- **年度一期**：上架包 `budget-sheets-build/LISTING-PACK-DRAFT.md` 本身标注“草稿、未定版”（2026-10-24），价格已于 2026-10-27 订正为 $12.99；描述以同目录 `ANNUAL-LISTING-DESCRIPTION-2026-10-27.md` 为准。
- **婚礼**：上架包 `wedding-build/WEDDING-LISTING-PACK-2026-10-26.md`（$9.99、5 买家档，字节与在售逐字一致），文件内未注明 listing ID，以产品名＋价格＋文件集认定；M3 上架包（`launch-kit/M3-LISTING-PACK-2026-11-01.md`）是另一款婚礼 listing（4608119576，$12.99、2 份 xlsx），**不是**本款，未采用。
- **D5／S-006／D3／D4／P1 的 LISTING-PACK.md**：文件内未注明 listing ID，以所在产品目录＋产品名＋价格认定。
- **Savings／Habit／Budget／2027 八款**：无单款 Etsy 上架包文件（各产品目录内的 LISTING-PACK.md 是 Ko-fi 包，非 Etsy 包，未采用）；Etsy 上架文案以 §3.2 共用源文件（wave1 总包＋各款描述存档）为准。
- **2027 Full 的 dated 档**：`dated-12p-2027_A4.pdf`／`dated-12p-2027_Letter.pdf` 是 2027 Full 买家档第 3、4 档；`wave1/DATED12-LAUNCH-PACK-2026-10-29.md` 是另一款 listing（2027 Dated 补充包 4608638057）的包，未采用。
- **年度一期 LICENSE**：`budget-sheets-build/PERSONAL_USE_LICENSE.txt`（916 B）在磁盘存在，但不在 Etsy 3 档买家文件内，未列入清单。

### 3.4 缺失项

- **无**：17 款的上架包与产品文件全部找到，无缺失。BRIEF-8 活页夹文件（婚礼 binder）按任务书“另行”，不属本批缺失。

## §4 交付物

1. 17 张新 pin（1000×1500 PNG／JPG）＋17 张 100px 缩略图，文件名 `batch4-<产品>-pin-v2-1000x1500.png`（缩略图同名 `-thumb-100px`）。
2. 首图重做图（仅首图不合 v1 的款，每款 1 张，同名规则加 `-img1`）。
3. 逐图制作记录（选页理由／选型／色值／字号／演示数据来源／省列说明／红像素自验计数）。
4. 逐款 listing 图片 v1 审计记录（每张图：密度／骨架／用色／页脚／标题／痕迹／截断，PASS／FAIL＋依据）。
5. 改项清单（首图以外不合 v1 的图，列入补充执行单候选，不擅自重做）。

## §5 验收（主聊执行，执行方不得预写结论）

1. 逐图按 §2 逐项核，任一项 FAIL 即打回该图重做，不整批退回。
2. 色值以众数色核对 8 色表；红像素按 §0.3 口径机检＋目视复核。
3. 数字／金额／日期逐项对源文件复核；演示数据须可复加、日期须对日历。
4. 验收通过的图才进入统一换图（删旧发新＋listing 换图，届时一起）；未通过的图不发、不换。
5. **执行方不得在交付包预写“已通过主聊验收”**（第二批已有两度预写，均不予采信）。

## 附录：补充执行单（草稿，另列一行，等 34／35 定论后定稿）

其余 18 款有 pin 款的首图 v1 审计（不做新 pin，只审计首图是否合 v1；不合的列入改项）：Speed7、年度二期、D4-Daily、D4-Essentials、D4-Weekly、P1-FS、P1-FN、P1-MF、C014-A、C039-A、C010、C012、C037（13 款）＋S-010、S-002、S-022、S-027、IWP-01（wave2 5 款）。6 张 BRIEF-6 封面已在 §5.2 闭合报告第 5 项核查，不重复列入。**总数对账**：第四批 17 款＋补充 18 款＋已核 6 款＝41 款；若 Lee 指明第 7 个排除项，补充执行单减 1 款。

—— 草稿完 ——
