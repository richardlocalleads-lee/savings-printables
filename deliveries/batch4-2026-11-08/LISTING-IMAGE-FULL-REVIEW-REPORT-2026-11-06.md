# SettledDays 全店上架图／视频全面审查报告

- 审查日期：2026-11-06（晚场）
- 任务书：`ST/launch-kit/LISTING-IMAGE-FULL-REVIEW-2026-11-05.md`
- 范围：A 组（M2、M3、S-023、2027、年度一期、D3）→ B 组（其余在售款图片）→ C 组（其余 8 支 listing 视频逐帧核）
- 性质：只审查，不改任何 listing／文件／价格。本报告报父代理审核，不直接交付 Lee。
- 准绳：源文件（xlsx 结构、PDF 页数、build 脚本文本、buyer-files 实际文件名）。
- 缺陷分型：A 渲染分页裁切／B 一侧大空白／C 文字边缘截断／D 图文口径不一致。
- 审查方法：A 组逐图全分辨率目视＋源文件对照；B 组 2×2 蒙太奇目视（1000px／格），存疑处全分辨率放大裁切复核；C 组 ffmpeg 逐秒抽帧（1fps）＋相邻帧平均绝对差分＋蒙太奇目视，技能 `etsy_listing_video_verification`。

## 总表

| 组 | 审查图片／视频 | 通过 | 缺陷 | 未核实 |
|---|---|---|---|---|
| A 组 | 22 张 | 19 | 3（S-023 图 1 C、S-023 图 3 C 轻微、D3 split C） | 年度一期（全部，磁盘无图无源文件） |
| B 组 | 83 张（映射确定） | 82 | 1（D5 M6 C） | 老款 8 个 listing 的图包映射（见候选组） |
| B 组候选 | 20 张（映射未核实） | 20（画面本身干净） | 0 | 映射本身未核实 |
| C 组 | 8 支视频 | 8 | 0 | — |
| 合计（映射确定） | 105 张图＋8 支视频 | 101 张＋8 支 | 4 张 | 年度一期 |

**4 处缺陷全是 C 类（文字边缘截断），无 A 类、无 D 类硬缺陷。**另有 1 处 D 类轻微口径备注（D3「14 template pages」），见 D3 节。

---

## A 组

### M2（4608070249）—— 4/4 PASS
- 图 1 Bill Calendar：9 栏＋合计 1,870.00 全在位；「Due month 到期月份」栏经右缘放大裁切核实完整，非截断。
- 图 2 Debt Payoff：雪球 19 个月／每月 130.00／X 2026-07-02／Y 2027-08-02 全在位。
- 图 3 Paycheck Plan：26 期＋TOTAL 6,411.00／1,870.00／1,560.00／1,014.00／650.00／5,094.00／1,317.00。
- 图 4 Year at a Glance：12 月＋YEAR TOTAL。
- 源 xlsx 7 表；未入图部分（Start Here、Payday Setup、26 Paychecks，及 Bill Calendar 月历行 25–28 与月小结行 31–44）包内有书面记录，描述未宣称图片覆盖全部 7 表，不作 D 类缺陷。

### M3（4608119576）—— 4/4 PASS
- 图 1 Budget Overview：15 类别＋Total 100%／$30,000／$1,800／$7,800／$28,200／$20,400＋Vendor Payments 合计块＋备注句完整两行。
- 图 2 Payment Timeline：状态合计＋类别合计＋Grand total $1,800／$7,800／$9,600＋4 行供应商明细，12 栏全在位。
- 图 3 Guest List：12 位宾客＋Total invited 12／Attending 9／Declined 1／No reply 1／Invited 1。
- 图 4 Task Checklist：12 项任务＋Days Left 4／75／92／160／200／242／287／304／351／356。
- 源 xlsx 16 表，仅 4 表入图，包内有书面记录，描述未宣称覆盖全部 16 表。

### S-023（4608642398）—— 4/6 PASS，2 处缺陷
- **图 1 FAIL（C）**：Dining Room 示例品名源文件为「Dining table with a very long descriptive name for testing text wrapping in narrow columns」，图上只剩「Dining table with a very long descriptive name for」，尾部「testing text wrapping in narrow columns」缺失。该品名本就是为测试换行而设，渲染证明未换行。
- 图 2 Start Here 第 1 页 PASS；图 4 Summary 合计（25 件／8,140／12,540 与源一致）PASS；图 5 Handover 合计（25／8,140）PASS；图 6 Walkthrough 打印伴侣第 1 页（复选框完整、页脚「Page 1 of 3」）PASS。
- **图 3 FAIL（C，轻微）**：空白 Inventory 13 栏纵向适合页宽，栏头粘连——「Estimated value」与「Serial number」并成「Estimated valueSerial number」（经栏头放大裁切核实；包内已有「栏头字距略紧」书面记录）。
- 修法（按年度二期样板）：图 1 缩短示例品名或强制换行后重渲染；图 3 横向重渲染。

### 2027 Dated 12 张独立补充包（4608638057）—— 4/4 PASS
- 图 1 January（2027-01-01 周五、31 天、5 行、周一起始、双语月份名、页脚在位）、图 2 July（2027-07-01 周四、31 天）、图 3 December Letter（2027-12-01 周三、31 天）、图 4 January 顶部细节裁切（包内注明为有意裁切，非分页错误）。
- 现售图 1 为 BRIEF-6 新封面，2026-11-04 已验＋2026-11-06 公开页回读无裁切，另核通过。

### 年度一期（4604232532，Phase 1，16 tabs，$12.99）—— 未核实
- 工作区未找到其磁盘图片与源 xlsx（`external-2027-corrected-review/` 的 4 张 JPG 经核对属于 2027 Full 4598684850，不是年度一期）。
- 须实况浏览器读公开页核验，子代理无浏览器，留待父代理安排。

### D3 双周薪预算（4600362280，$9.99）—— 3/4 PASS，1 处缺陷＋1 处 D 备注
- 源 xlsx 5 表（Start Here、26 Paychecks A1:L30、Paycheck Worksheet A1:C17、Bills Split A1:D23、Year at a Glance A1:F16），文件 `ST/biweekly-paycheck-planner/biweekly_budget.xlsx`；候选图 `ST/biweekly-paycheck-planner/` 下 cover_biweekly.png、listing_inside.png、listing_split.png、listing_formats.png（均为 2000px，已做 2×2 蒙太奇核验）。
- 封面 PASS、WHAT'S INSIDE PASS（13 项页面＋Excel 伴侣 5 表，与源一致）、YOU GET PASS。
- **图 listing_split FAIL（C）**：底部第二行文字在图右缘截断，末词只剩「befo」；源文本见 `build_biweekly.py:523`：「Two months a year bring a 3rd paycheck — plan it as a bonus, on paper, before payday.」——「re payday.」缺失。经右缘全分辨率放大裁切确认，文字被图框切断，非蒙太奇假象。
- 修法：缩短该句或缩小字号／折成两行后重渲染。
- **D 备注（轻微）**：封面写「14 template pages」，WHAT'S INSIDE 只列 13 项页面；`pdfinfo` 核实 A4 与 Letter 版 PDF 均为 14 页，`build_biweekly.py` 的 PAGES 表为 1 张封面＋13 张模板页——第 14 页是封面本身。两图口径差 1 页。修法：封面改「13 template pages + cover」或「14 pages incl. cover」。

---

## B 组（映射确定的 83 张）

| Listing | 图数 | 结论 |
|---|---|---|
| Speed7（4610318509） | 5 | 5/5 PASS（p1 Brain Dump、p2 Sort It Honestly、p3 Today's Honest Three、p4 Weekly Inventory、p5 Next Week, Blank；页码 1/5–5/5 全在位） |
| D4-Daily（4610375507） | 4 | 4/4 PASS（封面 p1、My Bare Minimum p2、Brain Dump p3、Daily Page p5；时间格 7:00–20:00 完整） |
| D4-Essentials（4610384841） | 4 | 4/4 PASS（封面 p1、My Bare Minimum p2、Routine Builder p3、Daily Essentials p5；31 天格每行 31 格全在位） |
| D4-Weekly（4610415182） | 4 | 4/4 PASS（英文封面 p1、My Week p2、Weekly Reset p3、繁中封面 p1；繁中页脚「Light」未译是源文本，非渲染缺陷） |
| P1-Family Sorting（4610424844） | 4 | 4/4 PASS（封面 p1、Six Ways p4、Family Claims p12、Box Labels p15；6 张标签图案与文字完整） |
| P1-First Night（4610419263） | 4 | 4/4 PASS（封面 p1、First Night Box p6、Move-Day Command p11、Box Labels p12；3 张标签完整） |
| P1-Move First（4610444597） | 4 | 4/4 PASS（封面 p1、Two-Stage Task List p2、Whole Move One Page p6、Command Dashboard p28；封面「English edition」与产品一致） |
| C010（4610494240） | 4 | 4/4 PASS（A4 空白、A4 已填示例、水彩笔 24色等填值未溢出、单标签放大、Letter 空白；页脚「· C010」在位） |
| C012（4610489673） | 4 | 4/4 PASS（门户顶、审批库 By Status、示例客户页、复制按钮悬停；注：图 2 底部对照表仅见 2 行，属视口截图裁切，非渲染缺陷） |
| C014-A（4610295973） | 4 | 4/4 PASS（18 图全在位、3 张 5×7 边框、缎带＋拱门细节、5×7 邀请函预览「You're Invited!」全文完整；预览为成品邀请函示例，描述 PLEASE CHECK FIRST 已说明只售图形，不作 D 缺陷） |
| C039-A（4610329670） | 7 | 7/7 PASS（contact-sheet 12 图案＋6 张 preview-card M1-S1～M6-S6；平铺无可见接缝，中央留白卡完整） |
| C037（4610533980） | 4 | 4/4 PASS（整页、已编辑副本 5 showings、Canva 编辑器截图、交付指引；图 4 底部 License 句经全分辨率裁切确认完整收尾，非截断） |
| M5（4608059394） | 4 | 4/4 PASS（img2 说明页、img3 House Fund A5 p1/2、img4 Travel Fund A4 p1/2、BRIEF-6 新封面生活照；封面已验＋公开页回读） |
| M6（4608071942） | 4 | 4/4 PASS（img2 Full Letter、img3 网格特写、img4 生活照、BRIEF-6 新封面；注：img3 右缘「31」格边框贴图边，数字完整、无内容丢失，属紧裁切） |
| S-006（4601983813） | 5 | 5/5 PASS（M1 hero、M2 重分、M3 打勾页、M4 五格输入、M5 文件清单；M5 所列 5 个文件名与 `s006-build/buyer-files/` 实际文件逐一对上；注：M4 标题与内容框之间、M5 下半约 50% 为留白，属构图稀疏、非渲染缺陷） |
| D5（4601773193） | 8 | **7/8 PASS，M6 FAIL（C）**——见下 |
| Kit（4600874500） | 5 | 5/5 PASS（M1 hero、M2 内容、M3 九页全览、M4 已填示例 caps $230／actual $187、M5 文件清单；M5 所列 3 文件与 `christmas-budget-kit/buyer-files/` 对上，「Gift lists hold 40 people」与 2 页×20 行一致；注：M5 下半约 60% 留白，属构图稀疏） |
| 婚礼（4604186625） | 1 | 1/1 PASS（主图 Overview：15 类别、Total 100%／$30,000.00、Total Paid $1,800.00／Pending $7,800.00／Remaining $20,400.00，份额与金额加总无误，「Example figures」在位；**磁盘只找到这一张图，live listing 是否另有图片未核实**） |
| 2027 Full（4598684850） | 4 | 4/4 PASS（01 主图、02 内容、03 双语、04 流程；注：04 下半约 55% 留白，属构图稀疏） |

### D5 唯一缺陷
- **M6_inside.jpg FAIL（C）**：右上文字块「Standard ($) + No-curren」——「No-currency」末尾「cy」被图右缘切掉。经全分辨率右缘放大裁切确认，字母「n」贴边被切，非蒙太奇假象。产品确有两个版本：Standard ($) 与 No-currency（M6 左页 WHAT'S IN THIS FILE 原文「no-currency version」可证）。
- 修法：缩小该行字号或把文字块左移，重渲染。
- 其余 7 张 PASS：M1 hero、M2 选档、M3 Payday First（注：绿色说明框压住表格右下角，属有意标注、遮住末 3 行×1 列预览，非渲染缺陷）、M4 Bill-Week Step-Down＋Skip Cards、M5 双罐示例、M7 A6 活页夹、M8 三页缩略图。

### B 组候选（画面干净、映射未核实）
- thread2-build 8 张（cover_fullpack、cover_starter、v2-02、v2-03、v2-04、v2b-08、v2b-09、v2c-02）：100-Day、52-Week、Savings Log、Sinking Funds 等页全部完整。**未核实这些文件具体上了 Savings Full／Starter、Habit Full／Starter、Budget Full／Starter、2027 Full／Starter 哪一款。**
- D4 候选 p-01～p-04（adhd-planner-light/mockup/renders）：封面、How This Planner Works、My Brain Profile、My Bare Minimum，全部完整；映射到 D4（4600823259）未核实。
- P1 候选 p-01～p-04（p1-moving-command/listing-assets/renders150）：43 页全本封面、How to Use、Start Here、First Family Conversation，全部完整；映射到 P1（4600844093）未核实。
- Restart 候选 L-1～L-4（weekly-restart-kit/internal-evidence/page-renders）：封面、Quick-Start Guide、Weekly Focus、Brain Dump，全部完整；映射到 Restart（4600838577）未核实。
- 观察项（非四类缺陷）：Restart 候选图页脚品牌为旧名「SavingsPrintablesCo」，与现店名 SettledDays 不一致（产品 PDF 本体即如此；D4／P1 候选图已是 Settled Days）。

---

## C 组（8 支视频，逐帧核）

全部 15.000 秒、1280×720、h264、30fps，时长合规。每支均为 5 段×约 3 秒（符合 Lee 2026-10-25 视频标准：每段 ≤3–4 秒、段内持续动作、无 5 秒定格）。逐秒抽帧＋相邻帧平均绝对差分全程非零（D4 系 1.3–4.6，C010 8.5–23.7，P1 系 3.7–7.8），无静止段＞4 秒、无闪帧（＜2 秒）、无界面元素残留（无工具栏／光标／头像），每段均为完整页面。

| 视频 | 段结构（约 3 秒／段） | 结论 |
|---|---|---|
| D4-Daily | 封面→My Bare Minimum→Brain Dump→Daily Page→Low-Battery Day | PASS |
| D4-Essentials | 封面→My Bare Minimum→Routine Builder→Daily Essentials→Where Things Live | PASS（末段推镜极慢，帧差 1.3–1.6，但画面持续漂移，非定格） |
| C010 | A4 空白→A4 已填→单标签放大→Letter 空白→A4 已填近景 | PASS |
| Speed7 | Brain Dump→Sort It Honestly→Today's Honest Three→Weekly Inventory→Next Week, Blank | PASS |
| D4-Weekly | 英文封面→My Week→Weekly Reset→繁中封面→Dump & Sort | PASS |
| P1-Family Sorting | 封面→Six Ways→Family Claims→Box Labels→Room by Room: Living Room | PASS |
| P1-First Night | 封面→First Night Box→Move-Day Command→Box Labels→Day One in the New Home | PASS |
| P1-Move First | 封面→Two-Stage Task List→Whole Move on One Page→Command Dashboard→Command Sheet | PASS |

### 其余视频核对记录（不重抽帧）
- C012：PASS（2026-11-04，返工一次后复验通过）。C014-A：PASS（2026-11-03）。C039-A：PASS（2026-11-03；两段 0.1–0.2 秒低均值帧已核实为持续动作，记观察项）。
- 年度二期：PASS（2026-11-04，五项全过）。C037：PASS（Take 5，2026-11-05；Take 1–4 均失败，Take 5 为首支可用）。
- M2：重建版验片通过（解码通过，2026-11-01）。M3：验片通过（解码通过；逐秒差分最小 8.96，2026-11-01）。M6：验片通过（解码通过，2026-11-01）。
- D3：PASS（独立核验，Lee 2026-10-26 18:55 接受，含头像现状接受）。
- **S-006：记录不完整。**Take 4 验片通过（2026-10-26，四段动作／结果／时长均合规），但记录写明「待 Lee 核验 verdict」，且「现挂 v3 定格版」——live 视频可能仍是含定格段的 v3，Take 4 是否已上传替换**未核实**。
- **M5／S-023／2027：书面 PASS 结论在磁盘上未找到。**三款的 ffmpeg 目录只有抽帧与 contact-sheet（verify-frames、verify-contact-sheet.png），无 verdict .md；shotlist 亦无 PASS 行。帧证据存在，但无书面结论——记为「记录不完整」，不冒认 PASS。

---

## 待修清单（4 处 C 类缺陷，按修法样板）

| # | 位置 | 缺陷 | 证据 | 修法 |
|---|---|---|---|---|
| 1 | S-023 图 1（Dining Room 示例品名） | C：尾部「testing text wrapping in narrow columns」缺失 | 源品名全句 vs 图上只剩前半句 | 缩短示例品名或强制换行后重渲染 |
| 2 | S-023 图 3（空白 Inventory 栏头） | C 轻微：「Estimated valueSerial number」粘连 | 栏头放大裁切核实 | 横向重渲染 |
| 3 | D3 listing_split.png（底部第二行） | C：「…on paper, befo」，「re payday.」缺失 | `build_biweekly.py:523` 全句 vs 图右缘放大裁切 | 缩短该句或缩小字号／折两行后重渲染 |
| 4 | D5 M6_inside.jpg（右上文字块） | C：「Standard ($) + No-curren」，「cy」缺失 | 右缘全分辨率放大裁切；左页原文「no-currency version」 | 缩小字号或文字块左移后重渲染 |

另：D3 封面「14 template pages」与 WHAT'S INSIDE 13 项页面差 1 页（第 14 页是封面），建议封面改「13 template pages + cover」或「14 pages incl. cover」。

## 未核实项（须父代理另行安排）
1. 年度一期（4604232532）全部图片：磁盘无图无源文件，须实况浏览器读公开页。
2. 婚礼 listing 除主图外是否另有图片：磁盘只找到 1 张。
3. 老款 8 个 listing（Savings Full／Starter、Habit Full／Starter、Budget Full／Starter、2027 Starter、D4、P1、Restart）的图包映射：候选图画面干净，但哪张上了哪款未核实。
4. S-006 live 视频是否为 Take 4（还是仍挂含定格段的 v3）。
5. M5／S-023／2027 视频的书面 PASS 结论未在磁盘找到（仅有帧证据）。

## 工作文件
- 拼图与放大裁切：`~/workspace/audit-tmp/listing-image-review-2026-11-06/m-*.png`、`/tmp/d3split-right.png`、`/tmp/d5-m6-right2.png`、`/tmp/m6-img3-right.png`、`/tmp/c037-04-bottom.png`
- 视频逐秒帧与蒙太奇：`~/workspace/audit-tmp/listing-image-review-2026-11-06/vframes/`
- 本报告：`~/workspace/audit-tmp/listing-image-review-2026-11-06/LISTING-IMAGE-FULL-REVIEW-REPORT-2026-11-06.md`

## 附录：年度一期缺陷检查完成（2026-11-07 实况近看）

- 方法：Lee 开原热点，Mac 实况浏览器打开公开页（listing 4604232532），看图器逐张放大目视；栏头疑点另做 4 倍放大裁切＋OCR 双确认。
- 数量纠正：实为 **6 张图＋1 视频**（本报告及 11-06 盘点称“5 张”数错了，漏了 1 张月结总表特写图“Totals, left over, and savings rate — done for you.”）。视频首帧与图 1 相同（11-06 已记），本次未重验视频。
- 逐项结果（6 张）：
  1. Start Here 指南页：通过，无截断（标题、16 tabs 两行、全部说明段完整）。
  2. 月结总表特写：通过，无截断（“Left over”一行的 L 在看图器里被“<”翻页按钮挡住，属看图器遮挡；January 图里同一总表的“Left over”完整，已交叉证实）。
  3. January：通过，无截断（INCOME、FIXED BILLS、MONTH SUMMARY 全完整，“Left over”首字母完整）。
  4. Expense Log：通过，无截断（TOTALS BY MONTH、TOTALS BY CATEGORY 全完整）。
  5. Year at a Glance：**1 处 C 类缺陷——栏头“Variable spending”显示为“Variable spendin”，末尾 g 被栏宽切掉**（4 倍放大截图＋OCR“Variable spendin Savings”双确认）。其余栏头（Month、Income、Bills、Savings、Left over）与数值全完整。疑似原表栏宽不足（表格本身可能就这么显示），修图时顺带核对原表；修法是放宽该栏后重渲染，不是只改图。
  6. Debt Payoff：通过，无截断（栏头、两行数据、Totals 行、底部说明全完整）。
- 结论：未核实项第 1 项闭环。待修清单现为 **5 张 C 类图**（原 4 张＋Year at a Glance 本张）＋3 处 D 类口径＋S-023 视频 S2＋D3 封面口径；5 项未核实至此全部闭环。
- 证据截图：`~/workspace/nodes/` 下本次看图器截图（screen-window.jpg 各帧）＋栏头 4 倍放大 `/tmp/yag-header.png`。
