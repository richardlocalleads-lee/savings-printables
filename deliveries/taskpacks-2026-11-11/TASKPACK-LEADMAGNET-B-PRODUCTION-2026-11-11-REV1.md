# 任务包：免费引流品候选 B（Subscription Audit）生产——外包

- 日期：2026-11-11（初版）／2026-11-12（REV1）
- 委托方：SettledDays（Lee）｜任务包编制：Muse
- 状态：待制作方接单。Lee 2026-11-09 21:07 已批准做 B；2026-11-11 23:31 决定外包生产。
- **修订说明（REV1，2026-11-12）**：按第三方独立审核意见（2026-11-11，三份任务包审核）修订本包；初版文件 `TASKPACK-LEADMAGNET-B-PRODUCTION-2026-11-11.md` 已被本版取代。修订内容只动漏斗与判读，不动产品规格：①营销同意机制——领取免费资源与同意收营销邮件分开，下载不依赖勾选；②“去重邮箱≥5”改为“有效表单提交≥5”，不是已验证的订阅者；③漏斗通过与成交通过拆开判读，窗口内全店订单只记为全店事件、不归因、不作通过条件。产品 PDF 规格（1 页、A4＋Letter、四栏、12 行、两项合计）**无修改**。
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
- **营销同意与下载分开**：表单分两件，缺一不可——①邮箱栏（必填）：提交后下载链接直接出现在本页感谢态；②营销同意勾选框（选填，默认**不勾**）：“Also send me SettledDays product news — at most one email in the next month, about the paid savings challenges.” **下载不依赖勾选**：不勾也能下载；勾了才进营销名单。提交时把同意状态一并写进 FormSubmit（`marketing_consent: yes/no`），Lee 在收件箱里分得清“只领文件的人”和“同意收营销邮件的人”。**页面文案不得把领取免费 PDF 写成同意营销订阅**，两者是两件事。
- 隐私行（必须写在表单下，）：We use your email to send you this free file's download record. We only send you product news if you tick the box above — at most one email in the next month, about the paid savings challenges. We never sell or share your address.（只收邮箱，不收姓名。）
- 感谢态：①下载链接（两个：A4 PDF、US Letter PDF，均为 Pages 持久地址，只在提交成功后出现，不在提交前露出）；②一节 “Put what you didn't spend to work”，三行，每行一款：S-002 — Savings Challenge, $4.99：`https://www.etsy.com/listing/4611956807?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；M5 — Goal Savings Challenge, $3：`https://www.etsy.com/listing/4608059394?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；D5 — Low Income Savings Challenges, $4.99：`https://www.etsy.com/listing/4601773193?utm_source=settleddays-free&utm_medium=thank-you&utm_campaign=subscription-audit-test-2026-11`；文案：You didn't spend it — now give it a job. A savings challenge turns "money I didn't spend" into a total you can see. ③一行“你已在名单上，未来一个月最多收到一封关于付费储蓄挑战的邮件”——**这行只在勾选了营销同意时出现；未勾选时改为“下载链接在上方；你没有订阅营销邮件。”**
- 文件地址：`deliveries/free-subscription-audit-2026-11-11/Free-Subscription-Audit-A4.pdf` 与 `deliveries/free-subscription-audit-2026-11-11/Free-Subscription-Audit-Letter.pdf`。
- 提交失败（断网／服务挂／未激活）→ 显示 mailto 兜底，访客可直接发邮件；Lee 收到后手动回下载链接——这是唯一的人工环节，只作兜底，不作主路径。页面文案不得写“we'll email you the file”（FormSubmit 不会给访客发邮件）。

## 四、流程与时间线

| 步骤 | 内容 | 耗时 |
|---|---|---|
| 1. 生产（本包） | 制作方做 2 档 PDF（A4＋Letter）；Muse 侧同步搭落地页＋渲 pin 图 | 约 2–3 天 |
| 2. 核验 | PDF 目视＋两档打印可用检查＋边界检查（无 Due day／Auto-pay、不是账单日历）；落地页表单测试（Lee 自测提交 → 点 FormSubmit “Activate Form” 激活 → 确认收件箱收到、感谢态出现下载链接、两档 PDF 能下载；**加测：不勾营销同意也能下载、勾选后收件箱里 consent 字段为 yes**）。**测试通过才发 pin** | 半天 |
| 3. 启动 | 发 pin，记录 pin 发布时刻（日期＋时间，HKT）——窗口起算点 | 1 天 |
| 4. 窗口 | 30 天（自 pin 发布当日 00:00 HKT 起算） | 30 天 |
| 5. 判读 | 窗口关后次日早上 09:12 HKT 计数判读 | 第 31 天早上 |

- **启动日建议**：放在 2026-11-19（100 天烟雾测试判读 11-18 之后），避免两个测试的窗口重叠、订单归因更模糊。重叠不是禁令——若 Lee 想早启动，接受重叠并在判读中注明。启动日由 Lee 点名。
- **示例时间线（若 11-19 启动）**：窗口 11-19–12-18，判读 12-19 早上。

## 五、判读口径（漏斗与成交拆开判）

- 量四项：① pin 出站点击（30 天窗口内，Pinterest 后台）；② **有效表单提交数**（FormSubmit 发到 richard.localleads@gmail.com 的提交，去重、剔除 Lee 自家测试提交；主题须为 `Free Subscription Audit - New signup`）；③ 同意收营销邮件的人数（consent 字段为 yes 的去重提交，单独记）；④ 全店付费单数（30 天窗口内，Etsy 后台）。
- **“有效表单提交”不是“已验证的订阅者”**：文件链接在提交成功后出现，并不验证邮箱所有权——访客可以提交错误或他人的地址，FormSubmit 仍可能进入成功状态。因此“有效表单提交 ≥5”只证明表单在工作，不证明有 5 位真实订阅者。免费品一定会有错填／假邮箱，这是免费 offer 的正常噪声；判读只用去重后的数字，不逐封核实真假，不把“提交数”等同于“意向人数”或“订阅者人数”。
- 通过线：pin 出站点击 ≥10；有效表单提交 ≥5。
- **判读规则（漏斗与成交分开）**：
- **漏斗通过**＝点击 ≥10 且有效表单提交 ≥5。只答“引流漏斗是否在工作”这一个问题。
- **窗口内全店订单单独记录**：窗口内全店出现订单，记为“引流品测试窗口内全店出现第 1 单”（全店事件），**不归因到引流品、不列为通过条件、不写成“引流品带来了第 1 单”**。Etsy 不把买家邮箱与订单对应，逐单归因做不到。
- 四格读法：漏斗通过＋窗口内有单＝漏斗通过（页面留着、pin 留着；窗口内的单记为全店事件，不归因）；漏斗通过＋窗口内 0 单＝漏斗通过、销售未见（引流品继续跑，成本为零、名单在长大，第 60 天再判一次；名单可由 Lee 手动发一封邮件，只讲新品／付费挑战，不群发、不催促）；漏斗不通过＋窗口内有单＝漏斗未通过（窗口内的单记为全店事件，不记到引流品头上；停止为这张模板做新 pin）；漏斗不通过＋窗口内 0 单＝不通过（停；不按这个模式做第二张引流品；页面留着，不删）。
- **一句话判读**：通过＝漏斗数字达标；只达标一半＝部分通过（留着、再看）；漏斗不达标＝不通过（无论有没有单）。漏斗数字只是“进入下一轮验证的兴趣条件”，不能自动认定已经形成可生产的商业机会。
- 感谢页 → Etsy 点击数无法直接测量（Pages 站无统计、Etsy Stats 不按 utm 分拆；Etsy Stats 的来源分拆只给域名级 referrer，不可靠）。本测试不把“感谢页点击数”列入判读，只列为“不可测、写明”。

## 六、交付物与验收

- **交付物（制作方）**：`Free-Subscription-Audit-A4.pdf` 与 `Free-Subscription-Audit-Letter.pdf`，附文件名＋字节＋SHA-256 清单。
- **验收检查单**：
- [] 12 行齐全、文字无错、两档各能正常打印。
- [] 无 Due day 栏、无 Auto-pay 栏、不是账单日历、与 D4 的 “Bills & Subscriptions” 页字段不同。
- [] 页脚三行齐全（品牌标语／Free — for personal use only／More savings challenges: etsy.com/shop/SettledDays）。
- [] 两档 PDF 均可正常打开、无损坏。
- **不交付**：落地页、pin 图、pin 发布由 Muse 侧做，不在制作方交付物内。
- **工期建议**：7 个工作日（与 BRIEF-8 同口径，供参考，以 Lee 与制作方商定为准）。
