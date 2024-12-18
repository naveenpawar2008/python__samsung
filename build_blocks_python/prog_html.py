import pdfkit

def html_to_pdf(input_html, output_pdf):
    # Convert HTML file to PDF
    pdfkit.from_file(input_html, output_pdf)
    print(f"PDF saved as {output_pdf}")

# Usage
input_html = "C:\learning\kleit_dec2024\certificate\certificate_bg.jpg.html"
output_pdf = "output.pdf"     # Replace with the desired output PDF path
html_to_pdf(input_html, output_pdf)
