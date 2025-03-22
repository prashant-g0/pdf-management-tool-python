from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
import pikepdf
from glob import glob

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Convert PDF to DOCX
@app.route('/convert-pdf-to-docx', methods=['POST'])
def convert_pdf_to_docx():
    file = request.files['file']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        docx_filename = filename.replace(".pdf", ".docx")
        obj = Converter(filename)
        obj.convert(docx_filename)
        obj.close()

        return send_file(docx_filename, as_attachment=True)

# Convert DOCX to PDF
@app.route('/convert-docx-to-pdf', methods=['POST'])
def convert_docx_to_pdf():
    file = request.files['file']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        pdf_filename = filename.replace(".docx", ".pdf")
        convert(filename, pdf_filename)

        return send_file(pdf_filename, as_attachment=True)

# Extract Images from PDF
@app.route('/extract-images', methods=['POST'])
def extract_images():
    file = request.files['file']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        images = convert_from_path(filename)
        image_paths = []
        for i, img in enumerate(images):
            image_path = filename.replace(".pdf", f"_page{i+1}.jpg")
            img.save(image_path, "JPEG")
            image_paths.append(image_path)

        return send_file(image_paths[0], as_attachment=True)  # Sending first image as an example

# Merge PDFs
@app.route('/merge-pdfs', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('files')
    if files:
        merged_pdf = pikepdf.Pdf.new()
        for file in files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            merged_pdf.pages.extend(pikepdf.Pdf.open(filename).pages)

        merged_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], "merged.pdf")
        merged_pdf.save(merged_pdf_path)

        return send_file(merged_pdf_path, as_attachment=True)

# Split PDF
@app.route('/split-pdf', methods=['POST'])
def split_pdf():
    file = request.files['file']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        old_pdf = pikepdf.Pdf.open(filename)
        split_files = []
        for n, page in enumerate(old_pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(page)
            split_filename = filename.replace(".pdf", f"_split{n+1}.pdf")
            new_pdf.save(split_filename)
            split_files.append(split_filename)

        return send_file(split_files[0], as_attachment=True)  # Sending first split file as an example

# Encrypt PDF
@app.route('/encrypt-pdf', methods=['POST'])
def encrypt_pdf():
    file = request.files['file']
    password = request.form['password']
    if file and password:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        protected_pdf = filename.replace(".pdf", "_protected.pdf")
        pdf = pikepdf.Pdf.open(filename)
        pdf.save(protected_pdf, encryption=pikepdf.Encryption(user=password, owner="admin"))

        return send_file(protected_pdf, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
