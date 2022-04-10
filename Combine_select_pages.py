import PyPDF2
import os

filenames = []

# FIND ALL THE FILES IN DIRECTORY, ENDING WITH .pdf
for file in os.listdir('./pdfs/to_merge'):
    if file.endswith('.pdf'):
        filenames.append(file)

filenames.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
result_pdf = open(f'pdfs/to_merge/combined_pdf.pdf', 'wb')

# LOOP OVER EACH FILE AND ADD ALL THE PAGES TO result_pdf
for file in filenames:

    file1 = open(f"pdfs/to_merge/{file}", 'rb')
    fileReader = PyPDF2.PdfFileReader(file1)

    for page in range(fileReader.numPages):
        pageObj = fileReader.getPage(page)
        pdfWriter.addPage(pageObj)

    pdfWriter.write(result_pdf)
    file1.close()

result_pdf.close()

