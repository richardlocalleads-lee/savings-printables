# SettledDays 留邮箱组件（email capture）— 使用说明

日期：2026-11-08。状态：组件已建好、2027 refresh 测试页已上线；S-033／S-035 两页运行中，窗口关之前不动。

## 这是什么

一个可复用的留邮箱表单（邮箱一栏），风格与烟雾测试页一致。访客提交后，地址经 FormSubmit 发到 richard.localleads@gmail.com——收件箱就是第一版名单。无服务器、无注册、无费用。

## 文件

- `email-capture-snippet.html`：组件本体（表单＋样式＋脚本），新页面直接套用，改两行 per-page 值（`SUBJECT`、`SOURCE`）。
- `../2027-refresh-notify-2026-11-08/index.html`：第一个用上它的页面（2027 Quarterly Refresh Pack 通知页，见下）。

## 后端（FormSubmit，formsubmit.co）

- 免费、无需注册。AJAX 端点：`https://formsubmit.co/ajax/richard.localleads@gmail.com`，POST JSON，须带 `Accept: application/json`。
- **首次使用须激活**：第一笔提交会触发一封 "Activate Form" 邮件到收件箱，Lee 点一次即开通；激活前收到的提交会被保留、激活后补发（按官方文档）。激活后 FormSubmit 会给一个随机别名地址，可替换 action 里的邮箱（换地址视为新表单，须重新激活）。
- 成功判断：返回的 `success` 是字符串 `"true"`／`"false"`，不是布尔值——代码里按字符串比较（`data.success === 'true'`），不可写 `if (data.success)`。
- 表单含 `_honey` 蜜罐字段（机器人填了即拒）与 `_captcha: 'false'`（AJAX 下不开验证码）；`_subject` 定邮件标题、`source` 标明页面来源，方便收件箱里区分。
- 失败兜底：提交失败（断网、服务挂了、未激活）时页面显示 mailto 链接，访客仍可直接发邮件，意向不丢。

## 限制（先说明，不藏着）

- 无后台面板；提交记录只保留 30 天、可通过 API 读（每天 5 次）。收件箱是唯一名单——名单长大后迁到 Buttondown／Mailchimp（须 Lee 建账号）。
- FormSubmit 免费服务无可用性保证（2026-10-29 曾观测到 521）；不要把它当成唯一关键链路，mailto 兜底必须一直留着。
- 隐私口径：页面只承诺“launch 时发一封、每季 refresh 发一封”，不多收、不转卖。表单只收邮箱，不收姓名。

## 部署规则

1. 新落地页直接套用组件，改 `SUBJECT` 与 `SOURCE`。
2. **运行中的烟雾测试页窗口期内不动**：S-033／S-035 按 mailto 意向邮件计数至 11-12，换表单会改动测量口径；窗口关后、页面转正时再换。
3. 上线后 Lee 须做的一件事：第一笔真实注册触发激活邮件后，点一次 "Activate Form"（收件箱 richard.localleads@gmail.com，顺带看一眼垃圾箱）。

## 2027 refresh 测试（第一个用它的地方）

- 页面：`deliveries/2027-refresh-notify-2026-11-08/`（已上线）。
- Offer（试探价，Lee 可改）：2027 Quarterly Refresh Pack，$6.99 一次性——2027 goals 包＋Q2／Q3／Q4 三次 refresh（每季 review＋新目标页＋reset 清单，邮件送达）。
- 通过线：与 S-033／S-035 同口径，15 个注册。过了才生产 refresh 内容；不过就停，不追。
- 发 pin 前须 Lee 定：价格与文案已定稿（本页文案为初稿，未经 Lee 过目不得对外承诺）。
