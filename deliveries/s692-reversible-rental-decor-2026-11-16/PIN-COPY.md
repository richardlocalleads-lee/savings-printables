# S-692 Reversible Rental Decor — pin copy (sketch "下一次可执行的市场验证" verbatim intent)

## Pin

- **Title:** `Renting in Korea? Decorate without losing your deposit`
- **Description:** `A reversible decorating pack for renters: what you can stick where, a move-in photo record, and a pre-move-out checklist. Leave your email to be notified when it's ready.`
- **Link:** https://richardlocalleads-lee.github.io/savings-printables/deliveries/s692-reversible-rental-decor-2026-11-16/
- **Board:** TBD at publish time (decide on the account: a Home board if one exists, else Savings Challenge Printables, the board used by all smoke-test pins so far).
- **Image:** `pin-s692-reversible-rental-decor-1000x1500.png` (1000×1500, AI-generated concept image: small rental room decorated with removable hooks and washi tape, no text, no fake product pages, no claim the product exists.)

## Landing page

- Title: `Renting in Korea? Decorate without losing your deposit`
- Subtitle: `A reversible decorating pack for renters: what you can stick where, a move-in photo record, and a pre-move-out checklist — before the landlord's walkthrough.`
- Honest boundary on the page: a printable guide and record tool, not a legal service — it doesn't promise the landlord won't deduct, and it's not legal advice.
- No file is offered: this is a notify-me test, the product does not exist yet. The thanks state only confirms "You're on the list".
- Form: FormSubmit AJAX to `richard.localleads@gmail.com`
  - `_subject`: `S-692 Reversible Rental Decor - Notify Me`
  - `source`: `s692-reversible-rental-decor`
  - First real signup triggers a FormSubmit activation email to richard.localleads@gmail.com — Lee must click ACTIVATE FORM once (established pattern, G4/B).

## Test parameters (sketch §"下一次可执行的市场验证")

- **Method:** landing page + Pinterest pin, 5-day window, pass line 15 saves/inquiries (counted as 15 deduplicated intent emails).
- **Validation question:** does the English Pinterest audience accept the form — a reversible decorating pack for renters? This tests form acceptance, not Korean buyer intent.
- **Channel caveat (read honestly):** Korean 자취생 find decorating know-how via blogs / 크몽 / 자취 communities; Etsy / Pinterest reach to Korean renters is unverified. Below 15, read by the failure-classification table (no exposure / exposure no click / click no signup) and note the unverified-channel confound. Do not auto-condemn the demand.
- **Window:** 5 days from publish date; judgment the morning after the window closes.
- **Pass ≠ production:** whether a passing result enters production is Lee's separate call.

## Status

- Landing page + pin image + copy: ready (2026-11-16).
- **Pin NOT published yet.** On publish, record the pin ID and time in `~/workspace/audit-tmp/S692-S693-PINTEREST-INTENT-2026-11-16.md`.
