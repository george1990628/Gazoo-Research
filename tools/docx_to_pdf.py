from fpdf import FPDF
from docx import Document

def convert_docx_to_pdf(docx_file, pdf_file):
    """
    Converts a Word document (.docx) to PDF.

    Parameters:
    - docx_file (str): Path to the input DOCX file.
    - pdf_file (str): Path to save the output PDF file.
    """
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Open the DOCX file
    doc = Document(docx_file)

    # Loop through all paragraphs in the DOCX file
    for para in doc.paragraphs:
        # Ensure the text is encoded in utf-8
        text = para.text.encode('latin-1', 'replace').decode('latin-1')

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.ln()

    # Save the PDF file
    pdf.output(pdf_file)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Basic paragraph-only DOCX-to-PDF utility.')
    parser.add_argument('input_docx')
    parser.add_argument('output_pdf')
    args = parser.parse_args()
    convert_docx_to_pdf(args.input_docx, args.output_pdf)
