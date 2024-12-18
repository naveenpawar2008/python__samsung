import pdfkit

# Path to your HTML file
html_file = 'file1.html'

# Path where the PDF will be saved
pdf_file = 'file1.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file)

print(f"PDF saved as {pdf_file}")
