
import pymupdf

def liststorage(file: UploadFile):
    
    documents = []

    pdf = pymupdf.open(
        stream=file.file.read(),
        filetype="pdf"
    )

    for page_number, page in enumerate(pdf):
        print(page_number)
        text = page.get_text()

        documents.append({
            "text": text,
            "source": file.filename,
            "page": page_number + 1
        })

    pdf.close()
    return documents
