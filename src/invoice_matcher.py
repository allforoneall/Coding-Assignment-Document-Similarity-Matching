import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InvoiceMatcher:
    def __init__(self):
        self.invoices = []
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def extract_text(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
            return ""

    def add_invoice(self, pdf_path):
        text = self.extract_text(pdf_path)
        self.invoices.append({'path': pdf_path, 'text': text})

    def find_similar_invoice(self, input_pdf):
        input_text = self.extract_text(input_pdf)
        all_texts = [invoice['text'] for invoice in self.invoices] + [input_text]
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)
        cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        
        most_similar_index = cosine_similarities.argmax()
        most_similar_score = cosine_similarities[0][most_similar_index]
        
        return self.invoices[most_similar_index], most_similar_score
