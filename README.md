# OCR Assessment - Sales Data Analysis

This repository contains the solution for the OCR Assessment on Sales Data Analysis. The task involves extracting sales data from a scanned PDF document, cleaning/transforming the data, performing data analysis to answer key business questions, and presenting the results.

## Author Information
- **Name:** Palak Sawle
- **Enrollment Number:** 0827CD231051
- **Email:** palaksawle230478@acropolis.in

---

## Project Overview

The workflow of the project is as follows:
1. **API Integration**: Send a GET request to retrieve the URL of the sales dataset PDF hosted on Google Drive.
2. **File Downloader**: Programmatically download the PDF file from Google Drive using python.
3. **Data Extraction**: Extract raw tabular data from the image-based PDF. Since the PDF is scanned/image-based and direct text extraction fails, the data was compiled using visual inspection (OCR) of the rendered page images.
4. **Data Cleaning & Transformation**: Load the extracted data into a Pandas DataFrame, clean and format data types (e.g., date conversion, numeric parsing), and engineer new columns (e.g., `total_sales = quantity * price_per_unit`).
5. **Data Analysis**: Write Python code to calculate key business metrics and answer the assessment questions.

---

## File Structure

- `Assessment_ocr.ipynb`: The main Jupyter Notebook containing the full implementation, documentation, code, and execution outputs.
- `extract.py`: A Python script for attempting direct table extraction.
- `requirements.txt`: Python package requirements.
- `sales_data.pdf`: The downloaded sales dataset.
- `page0.png` to `page4.png`: Rendered page images from the PDF.

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PalakSawle/ocr-assessment.git
   cd ocr-assessment
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Notebook**:
   Launch Jupyter Notebook or JupyterLab and open `Assessment_ocr.ipynb` to view or rerun the analysis.
   ```bash
   jupyter notebook Assessment_ocr.ipynb
   ```

---

## Summary of Analysis & Insights

The sales dataset consists of **49 transactions** spanning from January to July 2024. Here is a summary of the findings:

### Key Metrics
- **Total Orders**: 49
- **Total Revenue**: $2,143,900
- **Average Order Value (AOV)**: $43,753.06
- **Highest Single Order Value**: Order ID **1028** ($108,000)
- **Top Product**: **Laptop** (Generated highest total sales revenue: $582,000)
- **Top Customer**: **C001** (Spent a total of $235,500)
- **Cancelled Orders**: 6 (Total revenue lost: $329,500)

### Product Performance (Quantity Sold)
1. **Chair**: 21
2. **Tablet**: 20
3. **Headphones**: 19
4. **Monitor**: 14
5. **Laptop**: 11
6. **Desk**: 9
7. **Smartphone**: 9
8. **Smartwatch**: 7
9. **Sofa**: 7

### Regional Sales Breakdown
- **East**: $630,900
- **North**: $562,800
- **South**: $535,600
- **West**: $414,600

*The East region leads in revenue generation, followed by North and South, with West having the lowest total sales.*
