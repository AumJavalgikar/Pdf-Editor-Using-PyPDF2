import PyPDF2

pdfFile1 = open('pdfs/meetingminutes.pdf', 'rb')
pdfFile2 = open('pdfs/meetingminutes2.pdf', 'rb')

pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)
pdfWriter = PyPDF2.PdfFileWriter()

for page in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(page)
    pdfWriter.addPage(pageObj)

for page in range(pdfReader2.numPages):
    pageObj = pdfReader2.getPage(page)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('pdfs/combined_minutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile1.close()
pdfFile2.close()