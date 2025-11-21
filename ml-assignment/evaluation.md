Evaluation Summary
This document explains the thinking behind how the TrigramModel was built and the practical decisions
made along the way. The goal was simple: create a clean, reliable trigram-based text generator that
behaves predictably and passes the provided tests, while also keeping the implementation easy to
understand and extend.

1. Design Choices
1.1 Why a Trigram Model?
A trigram model strikes a good balance. It uses the previous two words as context, which is usually enough
to form reasonable predictions without making the model too sparse or complicated. It’s more expressive
than unigrams and bigrams, and less fragile than higher-order n-grams.

1.2 Data Structures That Make Life Easier
I used a defaultdict(Counter) to store trigram counts. This structure lets the model: - Record counts
quickly while training - Retrieve candidate next words instantly - Use frequencies naturally during
probabilistic generation
Basically, it gives us fast lookups and simple integration with random.choices().

1.3 Text Cleaning and Token Handling
Preprocessing ensures consistency across different texts. The steps include: - Converting text to lowercase
so the model treats "The" and "the" the same - Removing punctuation so words aren’t split incorrectly -
Splitting into tokens - Adding <s> and </s> to mark sentence boundaries
These choices help the model learn clean and stable trigrams.

1.4 Making Sure Edge Cases Don’t Break Anything
The tests expect the model to behave sensibly even when the input text is empty or extremely short. To
support that: - Empty input makes the model “untrained,” and generation returns an empty string - Short
input still gets padded so the model can form at least one trigram - generate() always returns a string,
never None
This makes the model predictable and fully test-compliant.

1.5 How Words Are Chosen During Generation
Instead of always picking the most frequent next word, the model samples based on the actual trigram
distribution. This keeps the output varied and more natural.

2. How to Test the Model
2.1 Install Dependencies
Run this in the project root:

pip install -r requirements.txt

2.2 Check the Project Structure
Make sure your folders look like this:

ml-assignment/
├── src/
│ ├── __init__.py
│ └── ngram_model.py
├── tests/
│ └── test_ngram.py
└── requirements.txt

2.3 Fix Import Path (Windows)
Before running tests, set the Python path:

set PYTHONPATH=%cd%

2.4 Run All Tests

pytest
You should see all tests passing.



3. Final Thoughts

The model was built to be simple, readable, and reliable. Every design choice—from preprocessing to how
trigrams are stored—was made to ensure clean behavior and easy testing. This makes the implementation
stable while keeping the door open for future improvements like smoothing or higher-order models.