# S-689 Newlywed First Month — pin copy (sketch "下一次可执行的市场验证" verbatim intent)

## Pin

- **Title:** `Just married and never did housework? First 30 days, one task a day`
- **Description:** `30 days, one small task a day, plus a card that settles who does what. The first month only — not a whole wedding book. Leave your email to be notified when it's ready.`
- **Link:** https://richardlocalleads-lee.github.io/savings-printables/deliveries/s689-newlywed-first-month-2026-11-15/
- **Board:** TBD at publish time (decide on the account: a Home board if one exists, else Savings Challenge Printables, the board used by all smoke-test pins so far).
- **Image:** `pin-s689-newlywed-first-month-1000x1500.png` (1000×1500, AI-generated concept image: kitchen counter with one daily task card, mug, plant. No text, no fake product pages, no claim the product exists.)

## Landing page

- Title: `Just married and never did housework?`
- Subtitle: `The first 30 days, one task a day — plus a card that settles who does what. A first-month starter, not a whole wedding book.`
- Honest framing: the first month only — not a memoir, not a full wedding bundle. No file is offered: this is a notify-me test, the product does not exist yet. The thanks state only confirms "You're on the list".
- **Honest口径 (audit):** the 22 transactions were for the whole newlywed memoir ebook on 크몽 (gig/698621); whether the 살림 appendix was the purchase motive is undistinguished. Nothing on this page or pin may be read as "the 살림 slice sold 22 units".
- Form: FormSubmit AJAX to `richard.localleads@gmail.com`
  - `_subject`: `S-689 Newlywed First Month - Notify Me`
  - `source`: `s689-newlywed-first-month`
  - First real signup triggers a FormSubmit activation email to richard.localleads@gmail.com — Lee must click ACTIVATE FORM once (established pattern, G4/B).

## Test parameters (sketch §"下一次可执行的市场验证")

- **Method:** landing page + Pinterest pin, 5-day window, pass line 15 saves/inquiries (counted as 15 deduplicated intent emails).
- **Validation question:** does the English Pinterest audience accept the form — first 30 days, one task a day? This tests form acceptance, not Korean buyer intent.
- **Channel caveat (read honestly):** Korean 예비/신혼부부 find solutions via 크몽 / Instagram / Naver Cafe; Etsy / Pinterest reach is unverified. Below 15, read by the failure-classification table (no exposure / exposure no click / click no signup) and note the unverified-channel confound. Do not auto-condemn the demand.
- **Window:** 5 days from publish date; judgment the morning after the window closes.
- **Pass ≠ production:** whether a passing result enters production is Lee's separate call.

## Status

- Landing page + pin image + copy: ready (2026-11-15).
- **Pin NOT published yet.** On publish, record the pin ID and time in `~/workspace/audit-tmp/S688-S689-PINTEREST-INTENT-2026-11-15.md`.
