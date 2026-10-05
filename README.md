# Report to Executive Brief

A small Python script that reads a long PDF report and writes a two-minute executive brief using an LLM.

This is my first project with an LLM API.

## What it does

1. Reads the text of a PDF with `pypdf`.
2. Sends the text and a prompt to a Gemini model.
3. Prints a brief: a 3-sentence summary and 3 actionable insights. Each insight has **what to do**, **why**, and a **supporting quote** from the report.

I tested it on the official Saudi Vision 2030 overview (85 pages).

## The prompt

The prompt tells the model five things:

- **Role:** a strategy analyst in the energy sector
- **Task:** write a short executive brief of the report
- **Audience:** senior leadership, two minutes of reading time
- **Format:** a 3-sentence summary, then 3 insights with "what to do" and "why"
- **Rule:** use only the report text, say "not stated in the report" if something is missing, and quote the supporting phrase

## Did the model tell the truth?

LLMs can make things up, so I searched the PDF for every quote and number in the brief. All of them were in the report. For example:

| In the brief | Page in the report |
|---|---|
| Initial target of 9.5 gigawatts of renewable energy | 48 |
| Oil and gas localization from 40% to 75% | 46 |
| The Public Investment Fund "will not compete with the private sector" | 41 |

The full output is in [`sample_output.md`](sample_output.md).

## Limits

- The quotes come from the report. The "what to do" lines are the model's suggestions, so a person still needs to judge them.
- The model only knows the document I give it. This report is from 2016, so some targets may have changed.
- I only use public documents with a free API.

## Run it

```bash
pip install -r requirements.txt
```

Get a free Gemini API key from Google AI Studio and save it as an environment variable called `GEMINI_API_KEY`. The key is never written in the code.

Download the Vision 2030 overview PDF from the official Vision 2030 website and save it in this folder as `vision-2030-overview.pdf`. The PDF is not included here.

```bash
python brief.py
```

## What I would add next

Page numbers for each quote, and a way to ask questions across several reports.
