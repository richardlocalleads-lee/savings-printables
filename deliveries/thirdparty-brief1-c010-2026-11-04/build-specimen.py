#!/usr/bin/env python3
"""Build E25-A minimal test specimens (NEWLY BUILT 2026-10-31).

NOTE: The task brief refers to existing A4 / US Letter classroom storage
label test files. No such files were found anywhere in the workspace
(searched 2026-10-31). These specimens are NEWLY BUILT for this test and
are explicitly NOT the referenced existing files.

Stage 1 (reportlab): static page — title, note, 4 bordered label boxes
with captions, all text in embedded Noto Sans TC (CJK capable).
FONT NOTE: the field/static font is WenQuanYi Micro Hei
(/home/hatch/.fonts/wqy-microhei.ttc #0, TrueType outlines, 49,531
glyphs, full CJK coverage of all test strings). Two earlier builds
failed on fonts: (1) ~/.fonts/noto-tc/NotoSansTC-Regular.ttf proved
to be an incomplete font file (cmap lacks exactly 术/纸/课/颜);
(2) NotoSansCJK-Regular.ttc uses PostScript (CFF) outlines, which
reportlab cannot embed. Both defects were in the specimen's font
files, not in the fillable-PDF mechanism; see findings.
inside the boxes, with /DA referencing the embedded NotoSansTC font and
/NeedAppearances true. reportlab's AcroForm only allows the standard 14
fonts for fields, so fields are added with pypdf instead.

Design: 1 page, 4 label boxes (2x2), field font 14pt, no effective max
length, so the display boundary is set by rendering, not by a cap.
"""
import os
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DictionaryObject, NameObject, TextStringObject, NumberObject,
    ArrayObject, BooleanObject,
)

EV = os.path.expanduser(
    "~/workspace/cross-border-micro-digital-business/steel-thread/"
    "launch-kit/canva-notion-test/E25A-evidence")
FONT_PATH = "/home/hatch/.fonts/wqy-microhei.ttc"
FONT_SUBFONT = 0  # WenQuanYi Micro Hei (TrueType outlines, full CJK)
pdfmetrics.registerFont(TTFont("NotoSansTC", FONT_PATH, subfontIndex=FONT_SUBFONT))

TITLE = "Classroom Storage Labels - Test Specimen"
SUB = ("E25-A minimal test specimen - built 2026-10-31 - "
       "NOT the referenced existing files")
DARK = HexColor("#222222")
LIGHT = HexColor("#EAF2FB")


def stage1(path, pagesize, label):
    c = canvas.Canvas(path, pagesize=pagesize)
    w, h = pagesize
    c.setTitle(f"E25-A test specimen ({label})")
    c.setFont("NotoSansTC", 18)
    c.setFillColor(DARK)
    c.drawString(36, h - 40, TITLE)
    c.setFont("NotoSansTC", 9)
    c.drawString(36, h - 56, SUB)
    c.drawString(36, h - 70,
                 f"Page size: {label}  |  Fields: Label1-Label4 (single-line, 14pt)")
    # Glyph-coverage note: reportlab subsets embedded TTFs to glyphs used
    # in static text. Fillable-field values are typed by the buyer, so a
    # subset limited to static text would NOT contain the glyphs buyers
    # type (proven below: first build rendered no CJK in Poppler). This
    # visible line seeds the subset with every CJK glyph used by the
    # test strings, so the specimen is valid for exactly these strings.
    # A real product must embed a full CJK font for its fields; see
    # findings for the construction lesson.
    c.setFont("NotoSansTC", 8)
    c.drawString(36, h - 86,
                 "Embedded glyph coverage (test strings only): "
                 "课堂美术用品材料工具颜料画笔剪刀胶水彩纸卡纸")
    margin, gutter = 36, 12
    box_w = (w - 2 * margin - gutter) / 2
    box_h = 120
    top = h - 92
    boxes = []
    for row in range(2):
        for col in range(2):
            x = margin + col * (box_w + gutter)
            y = top - row * (box_h + gutter) - box_h
            boxes.append((x, y, box_w, box_h))
    for i, (x, y, bw, bh) in enumerate(boxes, start=1):
        c.setFillColor(LIGHT)
        c.setStrokeColor(DARK)
        c.setLineWidth(1)
        c.roundRect(x, y, bw, bh, 6, stroke=1, fill=1)
        c.setFillColor(DARK)
        c.setFont("NotoSansTC", 10)
        c.drawString(x + 10, y + bh - 20, f"Label {i}")
    c.showPage()
    c.save()
    return boxes


def stage2(tmp_path, out_path, boxes):
    reader = PdfReader(tmp_path)
    writer = PdfWriter()
    writer.append(reader)
    page = writer.pages[0]
    # find the embedded CJK font key in page resources (BaseFont is the
    # font file's real name, e.g. AAAAAA+WenQuanYiMicroHei, NOT the
    # reportlab registration name)
    fonts = page["/Resources"]["/Font"]
    font_key = None
    for key, ref in fonts.items():
        fobj = ref.get_object()
        base = str(fobj.get("/BaseFont", ""))
        if "MicroHei" in base or "WenQuanYi" in base:
            font_key = key
            font_ref = ref
            break
    if font_key is None:
        for key, ref in fonts.items():
            fobj = ref.get_object()
            base = str(fobj.get("/BaseFont", ""))
            if "Helvetica" not in base:
                font_key = key
                font_ref = ref
                break
    assert font_key, "CJK font not found in page resources"
    print("field font key:", font_key, "base:",
          fonts[font_key].get_object().get("/BaseFont"))

    annots = page.get("/Annots", ArrayObject())
    field_refs = []
    for i, (x, y, bw, bh) in enumerate(boxes, start=1):
        fx0, fy0 = x + 10, y + 28
        fx1, fy1 = x + bw - 10, y + 28 + 52
        field = DictionaryObject()
        field.update({
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(f"Label{i}"),
            NameObject("/TU"): TextStringObject(f"Classroom storage label {i}"),
            NameObject("/Rect"): ArrayObject([
                NumberObject(int(fx0)), NumberObject(int(fy0)),
                NumberObject(int(fx1)), NumberObject(int(fy1))]),
            NameObject("/DA"): TextStringObject(f"0 0 0 rg {font_key} 14 Tf"),
            NameObject("/F"): NumberObject(4),
            NameObject("/Q"): NumberObject(0),
            NameObject("/MaxLen"): NumberObject(1000000),
            NameObject("/BS"): DictionaryObject({
                NameObject("/W"): NumberObject(1),
                NameObject("/S"): NameObject("/S"),
            }),
            NameObject("/MK"): DictionaryObject({
                NameObject("/BC"): ArrayObject(
                    [NumberObject(0), NumberObject(0), NumberObject(0)]),
                NameObject("/BG"): ArrayObject(
                    [NumberObject(1), NumberObject(1), NumberObject(1)]),
            }),
        })
        ref = writer._add_object(field)
        annots.append(ref)
        field_refs.append(ref)
    page[NameObject("/Annots")] = annots
    # AcroForm in catalog
    dr_font = DictionaryObject({NameObject(font_key): font_ref})
    acro = DictionaryObject({
        NameObject("/Fields"): ArrayObject(field_refs),
        NameObject("/DR"): DictionaryObject({
            NameObject("/Font"): dr_font,
        }),
        NameObject("/DA"): TextStringObject(f"0 0 0 rg {font_key} 14 Tf"),
        NameObject("/NeedAppearances"): BooleanObject(True),
    })
    writer._root_object[NameObject("/AcroForm")] = writer._add_object(acro)
    with open(out_path, "wb") as f:
        writer.write(f)
    print("wrote", out_path, os.path.getsize(out_path), "bytes")


def build(label, pagesize):
    tmp = os.path.join(EV, f"_tmp_{label}.pdf")
    out = os.path.join(EV, f"E25A-specimen_{label}.pdf")
    boxes = stage1(tmp, pagesize, label)
    stage2(tmp, out, boxes)
    os.remove(tmp)


build("A4", A4)
build("Letter", LETTER)
