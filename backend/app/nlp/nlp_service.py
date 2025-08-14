from pathlib import Path
import spacy
import logging

logger = logging.getLogger(__name__)

class NLPService:
    def __init__(self):
        # Path is relative to this file's location
        self.model_path = Path(__file__).parent / "spact_token2vec" / "hotel_tok2vec"
        try:
            self.nlp = spacy.load(self.model_path)
            logger.info(f"Successfully loaded spaCy model from {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to load spaCy model from {self.model_path}: {e}")
            raise

    def predict_department(self, text: str) -> str:
        """Predict the department based on the input text."""
        doc = self.nlp(text)
        # Assuming the model predicts categories like "Housekeeping", "Maintenance", etc.
        # Adjust based on your actual model's output format
        if doc.cats:
            return max(doc.cats.items(), key=lambda x: x[1])[0]
        return ""

# Create a singleton instance
nlp_service = NLPService()
