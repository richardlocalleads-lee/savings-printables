# 任务包：免费引流品候选 B（Subscription Audit）生产——外包

- 日期：2026-11-11
- 委托方：SettledDays（Lee）｜任务包编制：Muse
- 状态：待制作方接单。Lee 2026-11-09 21:07 已批准做 B；2026-11-11 23:31 决定外包生产。
- 依据文件：设计文件 `FREE-LEAD-MAGNET-TEST-DESIGN-2026-11-09.md`（§1 候选 B、§2–§4 流程／判读／时间线，按 B 改写）；核对门记录 `FREE-LEAD-MAGNET-GATE-CHECK-2026-11-09.md`（B 门通过，附边界）。
- 背景：候选 A（No-Spend Day Tracker）已于 2026-11-09 核对门停止（它是 Budget Full 第 9 页的重做版），不做。B 是接替 A 的引流品。

## 一、产品定义（做且只做这些）

- **产品**：Subscription Audit（订阅费核查表），单页免费模板，只作引流、不作销售、不在 Etsy 上架、不标价、不进 41 款、不进生产队列表。
- **任务**：列出全部订阅，决定取消哪一个。不是记账、不是按时付账单。
- **规格**：1 页；A4 ＋ US Letter 各一档，两档各为独立 PDF。
- **页面内容（逐项）**：
  - 标题：Subscription Audit。
  - 表头四栏（且只有这四栏）：Subscription（订阅名）｜Monthly cost ($，每月费用）｜Last used（上次使用）｜Keep / Cancel（留还是取消）。
  - 12 行空白订阅行（每行：订阅名＋费用＋上次使用＋留／取消勾选）。
  - 页底两行合计：Monthly total $____（每月订阅合计）｜You'd save each month by cancelling $____（取消后每月省下的钱）。
  - 页底一行：Cancelled it? Put it in a challenge.
  - 页脚一行：SettledDays — Money, home and head, settled. ＋ Free — for personal use only. ＋ More savings challenges: etsy.com/shop/SettledDays。
- **无算术**：金额由买家自己写，产品不预填累计金额；生产核验只做：12 行齐全、文字无错、两档打印可用。

## 二、硬边界（违反即打回）

- **不得加 Due day 栏、不得加 Auto-pay 栏**——那是 D4 ADHD Planner “Bills & Subscriptions” 页的地盘。D4 的任务是“发薪日前核对账单、按时付”，B 的任务是“核查订阅、决定取消”，两者不得混同。
- **不得做成账单日历**——那是 D3／M2 的地盘。
- **不得复制 D4 的 “Bills & Subscriptions” 页**（What／Due day／Amount／Auto-pay? Y/N）——只取“列订阅”这个动作，不取它的字段与任务。
- **不承诺任何结果**：PDF 内不写“一定能存下多少钱”“保证省钱”“用了就能买到”等承诺；“取消后每月省下的钱”是买家自己写的数字，不是产品替他赚的钱。
- **不碰 Etsy 内容**：生产输入只用本任务包与自有产品定义，不取材于任何 Etsy 商品页、评价、图序、搜索联想（Lee 2026-10-30 时点 A 红线）。
- **不做免费样品**：本品与 41 款付费产品无内容重叠（核对门已过，附边界）；若制作中发现重叠，停下来报回，不换个说法继续。

## 三、Pin 文案与落地页文案（定稿，执行时逐字用）

### 3.1 Pin（1 张，Muse 侧发布；制作方只备图，不发 pin）

- 画板：Savings Challenge Printables。
- pin 图：本品页面按本店 pin 模板渲成 1000×1500（藏青头尾栏 #1B3A6B＋米白底 #FAF8F3）。
- pin 标题（71 字符，上限 100）：Free subscription audit: find the subscriptions you're still paying for
- pin 描述（上限 800）：Free printable subscription audit: list every subscription, write what it costs each month and when you last used it, mark keep or cancel, and see what cancelling saves you every month. One page, A4 + US Letter. Leave your email and the download appears right here. From SettledDays.
- pin 链接：落地页持久地址（见 §3.2），不带 Etsy 链接。

### 3.2 落地页（Muse 侧搭建；制作方不用建）

- 地址：`https://richardlocalleads-lee.github.io/savings-printables/deliveries/free-subscription-audit-2026-11-11/`（目录 `landing-repo/deliveries/free-subscription-audit-2026-11-11/`）。
- 标题：Find the subscriptions you're still paying for.
- 副标题：A free printable subscription audit. List every subscription, what it costs, and when you last used it — mark keep or cancel, and see what cancelling saves you each month.
- 三行“你得到什么”：① One page, A4 + US Letter, print at home. ② Every subscription in one list — cost, last used, keep or cancel. ③ Free — no account, no card.
- 表单：复用留邮箱组件 `email-capture-snippet.html`（改两行 per-page 值：`SUBJECT = 'Free Subscription Audit - New signup'`，`SOURCE = 'free-subscription-audit'`）。
- 隐私行（必须写在表单下）：We only use your email to send you SettledDays product news — at most one email in the next month, about the paid savings challenges. We never sell or share your address.（只收邮箱，不收姓名。）
- 感谢态：①下载链接（两个：A4 PDF、US Letter PDF，均为 Pages 持久地址，只在提交成功后出现，不在提交前露出）；②一节 “Put what you didn't spend to work”，三行，每行一款：S-002 — Savings Challenge, $4.99：`https://www.etsy.com/listing/4611956807?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；M5 — Goal Savings Challenge, $3：`https://www.etsy.com/listing/4608059394?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；D5 — Low Income Savings Challenges, $4.99：`https://www.etsy.com/listing/4601773193?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；文案：You didn't spend it — now give it a job. A savings challenge turns "money I didn't spend" into a total you can see. ③一行“你已在名单上，未来一个月最多收到一封关于付费储蓄挑战的邮件”。
- 文件地址：`deliveries/free-subscription-audit-2026-11-11/Free-Subscription-Audit-A4.pdf` 与 `deliveries/free-subscription-audit-2026-11-11/Free-Subscription-Audit-Letter.pdf`。
- 提交失败（断网／服务挂／未激活）→ 显示 mailto 兜底，访客可直接发邮件；Lee 收到后手动回下载链接——这是唯一的人工环节，只作兜底，不作主路径。页面文案不得写“we'll email you the file”（FormSubmit 不会给访客发邮件）。

## 四、流程与时间线

| 步骤 | 内容 | 耗时 |
|---|---|---|
| 1. 生产（本包） | 制作方做 2 档 PDF（A4＋Letter）；Muse 侧同步搭落地页＋渲 pin 图 | 约 2–3 天 |
| 2. 核验 | PDF 目视＋两档打印可用检查＋边界检查（无 Due day／Auto-pay、不是账单日历）；落地页表单测试（Lee 自测提交 → 点 FormSubmit “Activate Form” 激活 → 确认收件箱收到、感谢态出现下载链接、两档 PDF 能下载）。**测试通过才发 pin** | 半天 |
| 3. 启动 | 发 pin，记录 pin 发布时刻（日期＋时间，HKT）——窗口起算点 | 1 天 |
| 4. 窗口 | 30 天（自 pin 发布当日 00:00 HKT 起算） | 30 天 |
| 5. 判读 | 窗口关后次日早上 09:12 HKT 计数判读 | 第 31 天早上 |

- **启动日建议**：放在 2026-11-19（100 天烟雾测试判读 11-18 之后），避免两个测试的窗口重叠、订单归因更模糊。重叠不是禁令——若 Lee 想早启动，接受重叠并在判读中注明。启动日由 Lee 点名。
- **示例时间线（若 11-19 启动）**：窗口 11-19–12-18，判读 12-19 早上。

## 五、判读口径（制作方不用判读，写明以便知晓标准）

- 量四项：① pin 出站点击（30 天窗口内，Pinterest 后台）；② 去重邮箱数（FormSubmit 发到 richard.localleads@gmail.com 的提交，去重、剔除 Lee 自家测试提交；主题须为 `Free Subscription Audit - New signup`）；③ 全店付费单数（30 天窗口内，Etsy 后台）；④ 感谢页 → Etsy 点击数（无法直接测量，只记录“不可测”，不列入判读）。
- 通过线：pin 出站点击 ≥10；去重邮箱 ≥5；付费单 ≥1（全店，窗口内）。
- 判读规则（2×2 表）：漏斗通过（点击 ≥10 且邮箱 ≥5）＋窗口内 ≥1 单＝通过；漏斗通过＋窗口内 0 单＝部分通过（留着、第 60 天再判）；漏斗不通过＝不通过（无论有没有单）。
- 诚实前提：没有任何一单能被归因到某一封邮件（Etsy 不把买家邮箱与订单对应）；窗口内出现第 1 单只写成“引流品测试窗口内全店出现第 1 单”，不能写成“引流品带来了第 1 单”。

## 六、交付物与验收

- **交付物（制作方）**：`Free-Subscription-Audit-A4.pdf` 与 `Free-Subscription-Audit-Letter.pdf`，附文件名＋字节＋SHA-256 清单。
- **验收检查单**：
  - [ ] 12 行齐全、文字无错、两档各能正常打印。
  - [ ] 无 Due day 栏、无 Auto-pay 栏、不是账单日历、与 D4 的 “Bills & Subscriptions” 页字段不同。
  - [ ] 页脚三行齐全（品牌标语／Free — for personal use only／More savings challenges: etsy.com/shop/SettledDays）。
  - [ ] 两档 PDF 均可正常打开、无损坏。
- **不交付**：落地页、pin 图、pin 发布由 Muse 侧做，不在制作方交付物内。
- **工期建议**：7 个工作日（与 BRIEF-8 同口径，供参考，以 Lee 与制作方商定为准）。
