# useful-calendar-events-germany
An opinionated collection of German public holidays and school vacations ranging from 2000-01-01 to 2026-12-31 for data science and data analytics.

# NOTE: This repository is WORK IN PROGRESS!
Currently contained are public holidays issued by the federal government as well as the states Baden-Württemberg, Bayern, Berlin, Brandenburg, Bremen and Nordrhein-Westfalen.
Public holidays of the other 10 states are not yet contained, nor are state-level school holidays currently contained. 

# Where does the data come from?
Data about holidays is sourced by hand directly from federal and state legislation.
Dates depending on Easter were calculated using a script (contained in this repository).

However, as most of the data was transferred by hand, no gurantee on corectness or completness is given. If you find an issue, please report it back.

Data about school holidays is currently available from 2009 to 2026. The data was sourced from [KMK PDFs](https://www.kmk.org/service/ferienregelung.html), extracted via LLM assisted OCR and hand-checked row by row.

# What is counted as a public holiday?
A public holiday for the purpose of this repository is hereby defined as a day mentioned in German federal or state legislation, where most commercial activities are prohibited, shops are closed, and employees are generally entitled to paid time off, that is not protected by law because it is a Sunday.
Apart from this definition, a public holiday may be excluded if
- it is always a sunday, or
- it is a state legislated public holiday on October 3rd (German Unity Day), the only federal pubic holiday in German (those days are only included once with `issuer_type` and `issuer` both being `BUND`).

## Could those exceptions please be added back?
Feel free to PR them.
