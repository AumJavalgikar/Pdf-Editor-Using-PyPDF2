import PyPDF2

# Open file, store file object in pdfFile
pdfFile = open('pdfs/encrypted.pdf', 'rb')

# Get pdfFileReaderObject and store it in pdfReader, all pdf operations will be performed on this object
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# Decrypt pdf
pdfReader.decrypt('rosebud')

# Print the total number of pages
print(pdfReader.numPages)

# Create a page object for 1st page, i.e index 0
pageObj = pdfReader.getPage(0)

# Extract all the text from page object and print output
print(pageObj.extractText())

# Close pdfFile
pdfFile.close()