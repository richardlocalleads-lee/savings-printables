# S-688 Fridge Map — pin copy (sketch "下一次可执行的市场验证" verbatim intent)

## Pin

- **Title:** `Fridge full but nothing to eat? A one-time fridge map instead of another subscription`
- **Description:** `One page: where everything lives, what expires when, and what to eat this week. One-time purchase, no subscription, no app. Leave your email to be notified when it's ready.`
- **Link:** https://richardlocalleads-lee.github.io/savings-printables/deliveries/s688-fridge-map-2026-11-15/
- **Board:** TBD at publish time (decide on the account: a Home board if one exists, else Savings Challenge Printables, the board used by all smoke-test pins so far).
- **Image:** `pin-s688-fridge-map-1000x1500.png` (1000×1500, AI-generated concept image: organised fridge with a hand-drawn zone map card on the door. No text, no fake product pages, no claim the product exists.)

## Landing page

- Title: `Fridge full, but nothing to eat?`
- Subtitle: `A one-time fridge map: where everything lives, what expires when, and what to eat this week — on one page. No subscription, no app.`
- Honest boundary on the page: a printable map, not an app — it won't scan receipts or suggest recipes, and it doesn't charge every month.
- No file is offered: this is a notify-me test, the product does not exist yet. The thanks state only confirms "You're on the list".
- Form: FormSubmit AJAX to `richard.localleads@gmail.com`
  - `_subject`: `S-688 Fridge Map - Notify Me`
  - `source`: `s688-fridge-map`
  - First real signup triggers a FormSubmit activation email to richard.localleads@gmail.com — Lee must click ACTIVATE FORM once (established pattern, G4/B).

## Test parameters (sketch §"下一次可执行的市场验证")

- **Method:** landing page + Pinterest pin, 5-day window, pass line 15 saves/inquiries (counted as 15 deduplicated intent emails).
- **Validation question:** does the English Pinterest audience accept the form — a one-time fridge map instead of another subscription? This tests form acceptance, not Korean buyer intent.
- **Channel caveat (read honestly):** Korean buyers find fridge tools via App Store / Google Play / Instagram / Threads; Etsy / Pinterest reach to Korean fridge-management buyers is unverified. Below 15, read by the failure-classification table (no exposure / exposure no click / click no signup) and note the unverified-channel confound. Do not auto-condemn the demand.
- **Window:** 5 days from publish date; judgment the morning after the window closes.
- **Pass ≠ production:** whether a passing result enters production is Lee's separate call.

## Status

- Landing page + pin image + copy: ready (2026-11-15).
- **Pin NOT published yet.** On publish, record the pin ID and time in `~/workspace/audit-tmp/S688-S689-PINTEREST-INTENT-2026-11-15.md`.
