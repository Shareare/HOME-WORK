from fpdf import FPDF
from datetime import datetime

# PDF কনফিগারেশন
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# বাংলা ফন্ট যোগ করুন (নোট: আপনার সিস্টেমে Kalpurush বা SolaimanLipi ফন্ট থাকতে হবে)
try:
    pdf.add_font("Bengali", "", "Kalpurush.ttf", uni=True)
    pdf.set_font("Bengali", size=12)
except:
    pdf.add_font("Bengali", "", "SolaimanLipi.ttf", uni=True)
    pdf.set_font("Bengali", size=12)

# হেডার
pdf.set_fill_color(34, 139, 34)  # সবুজ ব্যাকগ্রাউন্ড
pdf.set_text_color(255, 255, 255)  # সাদা টেক্সট
pdf.cell(0, 10, "সুস্থ জীবনযাপনের ডায়েট চার্ট", 0, 1, 'C', True)
pdf.ln(5)

# তারিখ
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, f"তারিখ: {datetime.now().strftime('%d-%m-%Y')}", 0, 1, 'R')
pdf.ln(10)

# মিল টাইমলাইন ফাংশন
def add_meal(time, title, items, bg_color):
    pdf.set_fill_color(*bg_color)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, f"{time} - {title}", 0, 1, 'L', True)
    pdf.set_text_color(0, 0, 0)
    for item in items:
        pdf.cell(10)  # ইন্ডেন্টেশন
        pdf.multi_cell(0, 7, f"• {item}")
    pdf.ln(5)

# ডায়েট প্ল্যান ডেটা
meals = [
    {
        "time": "সকাল ৭:০০–৮:০০",
        "title": "সকালের নাশতা",
        "items": [
            "১ টা সিদ্ধ ডিম (বা অল্প তেলে পোচ)",
            "১ কাপ গ্রিন টি বা লেবু পানি (চিনি ছাড়া)",
            "১টা ছোট কলা বা ১টা আপেল"
        ],
        "color": (75, 192, 192)  # Cyan
    },
    {
        "time": "সকাল ৯:০০–৯:৩০",
        "title": "ব্রেকফাস্ট",
        "items": [
            "১ টা রুটি (আটা দিয়ে) + ১/২ কাপ সবজি (ভাজি না করে)",
            "অথবা ১ কাপ ওটস + ১ কাপ দুধ (low fat)"
        ],
        "color": (54, 162, 235)  # Blue
    },
    {
        "time": "দুপুর ১:০০–২:০০",
        "title": "মধ্যাহ্নভোজ",
        "items": [
            "ভাত – ১/২ কাপ (৫০-৬০ গ্রাম রান্না করা)",
            "মুরগির মাংস – ১ টুকরা (ব্রয়লার না খেলে ভালো)",
            "ডাল – ১/২ কাপ",
            "সবজি – ১ কাপ (ভাজি ছাড়া, ঝোল বা সেদ্ধ)",
            "টক দই – ১/২ কাপ"
        ],
        "color": (255, 159, 64)  # Orange
    },
    {
        "time": "বিকেল ৪:৩০–৫:০০",
        "title": "বিকেলের নাশতা",
        "items": [
            "১ কাপ গ্রিন টি + ২টা বিস্কুট (চিনি ছাড়া/হাই ফাইবার)",
            "অথবা ১টা সিদ্ধ ডিম/১ টুকরা ফল (আপেল/পেয়ারা/কমলা)"
        ],
        "color": (153, 102, 255)  # Purple
    },
    {
        "time": "রাত ৮:০০–৮:৩০",
        "title": "রাতের খাবার",
        "items": [
            "১টা রুটি (আটা)",
            "১/২ কাপ সবজি",
            "১টা সিদ্ধ ডিম বা ১ টুকরা মাছ/মুরগি",
            "রাতে ভাত না খাওয়াই ভালো"
        ],
        "color": (255, 99, 132)  # Pink
    },
    {
        "time": "ঘুমানোর আগে",
        "title": "ঐচ্ছিক",
        "items": [
            "১ গ্লাস গরম পানি",
            "চাইলে ১ চামচ ইসবগুল ভেজানো পানি"
        ],
        "color": (201, 203, 207)  # Gray
    }
]

# মিলস যোগ করুন
for meal in meals:
    add_meal(meal["time"], meal["title"], meal["items"], meal["color"])

# নির্দেশাবলী
pdf.set_fill_color(255, 193, 7)  # Amber
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 8, "বিশেষ নির্দেশনা:", 0, 1, 'L', True)
instructions = [
    "প্রতিদিন অন্তত ৩০–৪০ মিনিট হাটাহাটি/হালকা ব্যায়াম করো।",
    "দিনে অন্তত ৮–১০ গ্লাস পানি খাও।",
    "মিষ্টি, ভাজাপোড়া, সফট ড্রিংকস একেবারে বাদ দাও।",
    "পর্যাপ্ত ঘুম (৬-৮ ঘণ্টা) নিশ্চিত করো।"
]
for instruction in instructions:
    pdf.cell(10)
    pdf.multi_cell(0, 7, f"→ {instruction}")

# ফুটার
pdf.ln(10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, "© 2024 স্বাস্থ্যবিধি - সকল অধিকার সংরক্ষিত", 0, 0, 'C')

# PDF সেভ করুন
pdf.output("Bengali_Diet_Chart.pdf")
print("PDF সফলভাবে তৈরি হয়েছে: Bengali_Diet_Chart.pdf")