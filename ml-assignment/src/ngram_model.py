import random
import re
from collections import defaultdict, Counter

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        # (w1, w2) -> Counter of next words
        self.trigrams = defaultdict(Counter)
        self.trained = False

    def fit(self, text):
        """
        Trains the trigram model on the given text.
        """
        # Handle empty string
        if not text or text.strip() == "":
            self.trained = False
            return

        # Clean text: lowercase + remove punctuation
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)

        # Tokenize
        words = text.split()
        if len(words) == 0:
            self.trained = False
            return

        # Pad with start and end tokens
        words = ["<s>", "<s>"] + words + ["</s>"]

        # Count trigrams
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i + 1], words[i + 2]
            self.trigrams[(w1, w2)][w3] += 1

        self.trained = True

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.
        """
        # If model was never trained or text was empty → return empty string
        if not self.trained:
            return ""

        w1, w2 = "<s>", "<s>"
        output_words = []

        for _ in range(max_length):
            next_candidates = self.trigrams.get((w1, w2))
            if not next_candidates:
                break

            # Choose next word based on trigram frequency
            next_word = random.choices(
                population=list(next_candidates.keys()),
                weights=list(next_candidates.values()),
            )[0]

            if next_word == "</s>":
                break

            output_words.append(next_word)
            w1, w2 = w2, next_word

        # Ensure return value is always a string
        return "" if not output_words else " ".join(output_words)
