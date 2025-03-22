# 📄 PDF Management Tool

## 🚀 Overview
The **PDF Management Tool** is a Python-based web application designed to help users efficiently manage their PDF documents. It provides an easy-to-use interface for various operations, including:
- **Converting PDF to DOCX** and **DOCX to PDF**
- **Extracting images from PDFs**
- **Merging multiple PDFs**
- **Splitting PDFs into separate files**
- **Encrypting PDFs with a password**

This tool simplifies PDF handling and enhances document accessibility.

---

## 🛠 Prerequisites
Ensure you have Python installed. To install all dependencies, run:

```sh
pip install -r requirements.txt
```

### 🔹 Poppler Installation (Required for Image Extraction)
Poppler is necessary for processing PDF images.

#### **Windows Users:**
1. Download [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases).
2. Extract the downloaded files.
3. Set the `poppler_path` in the code:
   ```python
   poppler_path = r"C:\path\to\poppler\bin"
   ```

#### **Linux/macOS Users:**
Install Poppler using the following commands:
```sh
sudo apt install poppler-utils  # Ubuntu/Debian
brew install poppler  # macOS
```

---

## 📂 Project Directory Structure
```
pdf_management_tool/
│── static/                 # Static assets (CSS, JS)
│── templates/              # HTML templates
│   ├── index.html
│── uploads/                # Temporary storage for uploaded files
│── app.py                  # Flask backend logic
│── requirements.txt        # Dependencies list
│── README.md               # Project documentation
```
---

## 🚀 How to Run the Project
Follow these steps to set up and run the web application:

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/pdf-management-tool.git
cd pdf-management-tool
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Web Application**
```sh
python app.py
```

### **4️⃣ Open in Browser**
Once the server starts, open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## 👨‍💻 Author
Developed by **Prashant Gupta**
