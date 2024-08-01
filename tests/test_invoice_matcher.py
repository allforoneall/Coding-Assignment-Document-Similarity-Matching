import unittest
from src.invoice_matcher import InvoiceMatcher
import os

class TestInvoiceMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = InvoiceMatcher()
        # Add a couple of sample invoices for testing
        self.matcher.add_invoice('existing_invoices/invoice1.pdf')
        self.matcher.add_invoice('existing_invoices/invoice2.pdf')

    def test_text_extraction(self):
        text = self.matcher.extract_text('existing_invoices/invoice1.pdf')
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)

    def test_similarity_matching(self):
        similar_invoice, score = self.matcher.find_similar_invoice('input_invoices/new_invoice.pdf')
        self.assertIsNotNone(similar_invoice)
        self.assertTrue(score > 0)

if __name__ == '__main__':
    unittest.main()
