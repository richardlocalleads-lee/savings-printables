# S-656 Dokhakjaesu Planner — pin copy (REV1 §4, verbatim)

## Pin

- **Title (verbatim, 29 chars):** `독학재수 연간 커리큘럼표: 1년 계획, 매주 점검`
- **Description (verbatim, revised two-page version):** `재종반 없이 혼자 재수한다면, 1년 커리큘럼을 직접 짜고 매주 점검하는 표가 필요합니다. 연간 진도표 1장 + 매주 점검표 1장, 두 장으로 나눠. 무료 2페이지, A4. 이메일을 남기면 다운로드 링크가 바로 나타납니다.`
- **Link:** https://richardlocalleads-lee.github.io/savings-printables/deliveries/s656-dokhakjaesu-planner-2026-11-12/
- **Board:** TBD at publish time (candidate: Savings Challenge Printables, the board used by all smoke-test pins so far — S-033, S-035, G4 table, G4 calculator, B).
- **Image:** `pin-s656-dokhakjaesu-1000x1500.png` (1000×1500, navy header `1년 계획, 매주 점검`, real page-1 render, footer `SettledDays / 무료` — same convention as the B pin).

## Landing page

- Title: `1년 계획, 매주 점검.`
- Subtitle (REV1 revised, point-check first): `학원 없이 혼자 재수한다면, 계획은 짜는 것보다 지키는 것이 어렵습니다. 과목별 연간 진도표와 매주 점검란, 두 장으로 나눠 정리하세요.`
- File: `S656-Dokhakjaesu-Year-Plan-A4.pdf` — 2 pages, A4 only, Korean.
  - Size: 61,394 B
  - SHA-256: `e6f4ed8644e5d727e3acd5eaf48fec2c5d58f0d4f3f9abd439837ffa500b12ff`
  - Producer delivery: `~/workspace/audit-tmp/taskpacks-delivery-2026-11-12/s656/` (Muse audit PASS, 2026-11-12; third-party PASS; no rework).
- Form: FormSubmit AJAX to `richard.localleads@gmail.com`
  - `_subject`: `S-656 Dokhakjaesu Planner - New signup`
  - `source`: `s656-dokhakjaesu-planner`
  - No marketing-consent checkbox (REV1 does not require one).
  - First real signup triggers a FormSubmit activation email to richard.localleads@gmail.com — Lee must click ACTIVATE FORM once (established pattern, G4/B).

## Test parameters (REV1 §4)

- **Method:** landing page + Pinterest pin, 5-day window, pass line 15 intent emails.
- **Validation question:** not "does anyone want a planner" (generic planners are everywhere) — does the buyer see "year curriculum table + weekly self-check" as more valuable than a generic study planner? Copy puts weekly check first.
- **15-email reading:** 15 is an interest condition to enter the next round, not a production trigger and not proof of a commercial opportunity.
- **Channel caveat (read honestly):** Korean students buy planners on Coupang; Pinterest reach to this group is unverified. The test measures intent found via this channel, not Korean market demand itself. Below 15, read by the failure-classification table (no exposure / exposure no click / click no signup) and note the unverified-channel confound. Do not auto-condemn the demand.
- **Window:** no hard window (retaking the exam is a year-round task); test as soon as the prototype is ready, 5 days, judgment the morning after the window closes.
- **Pass ≠ production:** whether a passing result enters production is Lee's separate call.

## Status

- Landing page + pin image + copy: ready (2026-11-12).
- **Pin NOT published.** Publish date TBD — Lee names the start date; on publish, record the pin ID and time, and create the 5-day count cron (judgment the morning after the window closes, same pattern as `g4-gold-smoke-test-count-2026-11-16`).
