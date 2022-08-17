import PyPDF2

PATH = r'/home/mervan.yalcindag@bik.ilan/Downloads/artvin haber kkr/'
pdfIn = open(PATH + '3.pdf', 'rb') # exchange the 'original.pdf' with a name of your file 
pdfReader = PyPDF2.PdfFileReader(pdfIn)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    page.rotateCounterClockwise(90)
    pdfWriter.addPage(page)

pdfOut = open(PATH + 'rotated.pdf', 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()