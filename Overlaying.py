import PyPDF2

pdfFile1 = open('pdfs/meetingminutes.pdf', 'rb')
watermark = open('pdfs/watermark.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile1)
pageObj = pdfReader.getPage(0)

watermarkReader = PyPDF2.PdfFileReader(watermark)
pageObj.mergePage(watermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)

for page_num in range(1, pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page_num))

result_pdf = open('pdfs/watermarkedCover.pdf', 'wb')
pdfWriter.write(result_pdf)
pdfFile1.close()
watermark.close()
result_pdf.close()