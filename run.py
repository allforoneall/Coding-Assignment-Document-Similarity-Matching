from src.invoice_matcher import InvoiceMatcher
import os

def main():
    matcher = InvoiceMatcher()

    # Add existing invoices to the database
    for filename in os.listdir('existing_invoices'):
        if filename.endswith('.pdf'):
            matcher.add_invoice(os.path.join('existing_invoices', filename))
    
    # Find similar invoice for a new input invoice
    input_invoice = 'input_invoices/new_invoice.pdf'
    similar_invoice, score = matcher.find_similar_invoice(input_invoice)
    
    print(f"Most similar invoice: {similar_invoice['path']}")
    print(f"Similarity score: {score}")

if __name__ == "__main__":
    main()