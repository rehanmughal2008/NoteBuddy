from pypdf import PdfReader

def text_extractor(file):
    reader = PdfReader(file)  # Pass the file-like object directly
    #established variables
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text