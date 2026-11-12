# BUILD-LOG — G3 Hajj & Umrah Smoke Test Materials

- Production date: 2026-11-12 (HKT)
- Source document: `g3-smoke-test-taskpack-2026-11-12.md` (copy text from §2.2 and §3.2, used verbatim)

## 1. index.html — landing page

- Single file, inline CSS + JS, no external resources (the only external URL in the file is the FormSubmit endpoint the form posts to).
- Structure: H1 + subtitle + intro paragraph + green test-statement box + "why this" box (`.for-box`) + "What it would be" six items + format & language line + waitlist note + form + mailto fallback + brand footer.
- All copy taken verbatim from task pack §2.2: H1, subtitle, intro, test statement, "why this" lead and body, the six "What it would be" items (no functions added or removed), format & language line, waitlist note above the form, footer `SettledDays — Money, home and head, settled.`
- No price appears anywhere on the page (the §2.2 evidence-range sentence was not included). No currency-version promise. No download link, no Etsy link, no marketing-consent checkbox.

### Form configuration (task pack §2.3)

- Method: POST, JSON body, to `https://formsubmit.co/ajax/richard.localleads@gmail.com`
- Fields sent: `email` (trimmed and lowercased before submit; format-checked in the browser first — invalid input shows `Please enter a valid email address.`), `source` = `g3-hajj-umrah`, `_subject` = `G3 Hajj Umrah Planner - New signup`, `_template` = `table`, `_honey` = `''`, `_captcha` = `false`
- The page also contains a hidden `_honey` input (`display: none`) as a spam trap.
- Waitlist note above the form, verbatim: `Join the waitlist and we will email you if this launches. No spam — one email, only if it launches.`
- Success state: the form is hidden and the page shows `You're on the list — we'll email you if it launches.` (no download link, no Etsy link).
- Failure state: shows `That didn't go through. Please use the email link below instead.` plus the `mailto:richard.localleads@gmail.com` link at the bottom of the page.

### First-submission activation note (task pack §2.4)

- The first real email signup will trigger a FormSubmit "Activate Form" email to richard.localleads@gmail.com; Lee must click ACTIVATE FORM once for this form. This form is separate from the G4 and B forms, which have their own activations — do not confuse them.

## 2. pin-g3-hajj-umrah-1000x1500.png — pin image

- Drawn entirely with Python PIL code (Liberation Sans Bold / Liberation Serif Italic); no AI generation or AI editing involved.
- Layout: navy bands (#1B3A6B) at top and bottom, off-white body (#FAF8F3). Card carries only the title `Hajj & Umrah Savings Planner`, the theme line `Save for the journey, one month at a time.`, and the brand footer `SettledDays` in the bottom band.
- No product interior pages, no price, no for-sale wording (no "Buy now" / "On sale" / "Etsy"), no icons or extra text.

## 3. PIN-COPY.md — pin copy

- Title, description, board and link copied verbatim from task pack §3.2.
- Character counts measured at build time: pin title 64 characters; pin description 361 characters.

## 4. Self-check results (run at build time)

- Verbatim check: all 18 fixed strings from §2.2 (including the six items) found word-for-word in the extracted page text — 0 missing.
- Price scan of index.html: `$` character count 0; `$9`, `$15`, `6.99` all 0 hits. (The email validation uses a full-string match comparison instead of a regex end anchor, so the file contains no `$` at all.)
- Absence checks: `etsy` / `Etsy` 0 hits; `checkbox`, `consent`, `marketing` 0 hits.
- Form config check: endpoint, `source`, `_subject`, `_template`, `_honey`, `_captcha`, hidden `_honey` input, mailto link and lowercase conversion each found exactly as specified in §2.3.
- Pin image check: PIL opens the PNG at 1000×1500 (RGB); visually inspected — title fully inside the card, three lines, no clipping, no extra elements.
- PIN-COPY.md check: title, description, board and landing-page link match §3.2 verbatim; counts 64 / 361 as recorded above.
