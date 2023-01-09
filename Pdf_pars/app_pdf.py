import PyPDF2

f_test = 'Test.pdf'
pdf_list = []
res_params = 'Test'


def pdf_pars():
    reader = PyPDF2.PdfReader(f_test)
    pdf_list.append(reader.pages[0].extract_text())
    for f_params in pdf_list:
        if res_params in f_params:
            print(True)
        else:
            print(False)


pdf_pars()
