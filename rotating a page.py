import PyPDF2

pdfFile = open('pdfs/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pageOBj = pdfReader.getPage(0)
pageOBj.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageOBj)

resultantPdf = open('pdfs/rotatedPdf.pdf', 'wb')
pdfWriter.write(resultantPdf)
resultantPdf.close()
pdfFile.close()