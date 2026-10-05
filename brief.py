from google import genai
from pypdf import PdfReader

reader = PdfReader("vision-2030-overview.pdf")
client = genai.Client()

report_text = ""
for page in reader.pages:
    content = page.extract_text() or ""
    report_text += content

print(f"Number of pages: {len(reader.pages)}")
print(f"Number of characters: {len(report_text)}")
print(f"First 300 characters: {report_text[:300]}")

prompt = f'''You are a Strategy Analyst at an energy and investment group in Saudi Arabia with 13 years of professional experience in the energy sector.
    Your task is to produce a short Executive brief of the report text(which contains Saudi Arabia Vision 2030).
    The key audience is the Senior leadership, and the reading time must be just 2 minutes.
    The format of the Executive brief is a 3-sentence summary, followed by 3 actionable insights, each insight must have 'What to do' and 'Why'. 
    Use only the report text, if something is not in the report, explicitly say "not stated in the report", for all the actionable insights, quote the supporting phrase
    REPORT: {report_text}'''

interaction = client.interactions.create(
    model = "gemini-3.8-flash",
    input = prompt
)
print(interaction.output_text)     





