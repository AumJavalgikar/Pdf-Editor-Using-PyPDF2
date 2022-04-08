import PyPDF2

pdfFile1 = open('pdfs/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile1)
pdfWriter = PyPDF2.PdfFileWriter()

for page in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page))

pdfWriter.encrypt('rosebud')
result_pdf = open('pdfs/encrypted_meeting.pdf', 'wb')
pdfWriter.write(result_pdf)

pdfFile1.close()
result_pdf.close()