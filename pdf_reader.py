import pdfplumber
import os

class ReadPDF:
	def __init__(self):
		self.filedir = 'data/pdf_examples/'

	def readinPDF(self):
		'''
		Reads in PDF and prints out print lines in the pdf
		'''
		files_list = os.listdir(self.filedir)
		for file_name in files_list:
			file_path = os.path.join(self.filedir, file_name)
			if file_path.lower().endswith('.pdf'):
				with pdfplumber.open(file_path) as pdf:
					for page_number in range(len(pdf.pages)):
						page = pdf.pages[page_number]
						text = page.extract_text()
						# Split the text into lines and process each line
						lines = text.split('\n')
						print(lines)

pdf_data = ReadPDF()
pdf_data.readinPDF()