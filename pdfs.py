#!/mnt/c/Users/Max/AppData/Local/Programs/Python/Python310/python.exe

# pdfs.py

import sys
from contextlib import ExitStack

from docopt import docopt
import PyPDF2 as pdf


doc = """Usage:
    pdfs join <newfile> <files>...
    pdfs rotate [--180 --270] <file> <pages>... 
"""

args = docopt(doc)

writer = pdf.PdfFileWriter()
if args["join"]:
    readers = [pdf.PdfFileReader(fn) for fn in args["<files>"]]

    for reader in readers:
        for page in reader.pages:
            writer.addPage(page)

    with open(args["<newfile>"], "wb") as file:
        writer.write(file)
elif args["rotate"]:
    angle = 90
    if args["--180"]: angle = 180
    if args["--270"]: angle = 270

    reader = pdf.PdfFileReader(args["<file>"])
    for num, page in enumerate(reader.pages):
        if str(num) in args["<pages>"]:
            page.rotateClockwise(angle)
        writer.addPage(page)
    with open(args["<file>"], "wb") as file:
        writer.write(file)

