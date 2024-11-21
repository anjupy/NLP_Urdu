import pandas as pd
from nltk.util import ngrams
from nltk import ConditionalFreqDist
import random

# Step 1: Load the Data
data = pd.read_csv('urdu_stories.csv', header=None, encoding='utf-8')  
data.columns = ['Transliterated', 'Urdu']

# Extract the necessary columns (Urdu written in Urdu script)
urdu_text = data['Urdu']  

# Step 2: Tokenization Using UTF-8
# Tokenize manually by splitting on spaces and keeping UTF-8 compatibility
def utf8_tokenizer(text):
    return text.split()  # Split by spaces to extract words

# Tokenize all Urdu paragraphs (written in Urdu script)
urdu_tokens = urdu_text.apply(utf8_tokenizer)

# Combine all tokenized sentences into a single list of words
all_tokens = [word for sentence in urdu_tokens for word in sentence]

# Step 3: Build N-Gram Models
# Function to create n-grams from tokens
def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

# Function to build a Conditional Frequency Distribution (CFD)
def build_cfd(tokens, n):
    ngrams_list = generate_ngrams(tokens, n)
    return ConditionalFreqDist((ngram[:-1], ngram[-1]) for ngram in ngrams_list)

# Create unigram, bigram, trigram, and four-gram CFDs
unigram_cfd = build_cfd(all_tokens, 1)
bigram_cfd = build_cfd(all_tokens, 2)
trigram_cfd = build_cfd(all_tokens, 3)
fourgram_cfd = build_cfd(all_tokens, 4)

# Step 4: Story Generation
# Function to generate a sentence using an n-gram model
def generate_sentence(cfd, n, max_length=15):
    sentence = []
    # Start with a random word or n-gram
    starting_words = list(cfd.keys())
    current = random.choice(starting_words)
    sentence.extend(current)

    for _ in range(max_length - n + 1):
        if current not in cfd or len(cfd[current]) == 0:
            break
        next_word = random.choices(list(cfd[current].keys()), weights=cfd[current].values())[0]
        sentence.append(next_word)
        current = tuple(sentence[-n + 1:])  # Update the context

    return ' '.join(sentence)

# Function to generate a story with paragraphs
def generate_story(paragraphs=3, sentences_per_paragraph=(5, 10), n=3):
    story = []
    for _ in range(paragraphs):
        paragraph = []
        num_sentences = random.randint(*sentences_per_paragraph)
        for _ in range(num_sentences):
            sentence = generate_sentence(trigram_cfd if n == 3 else fourgram_cfd, n=n)
            paragraph.append(sentence)
        story.append('\n'.join(paragraph))
    return '\n\n'.join(story)


# Step 5: Generate the Story with n=2, n=3 or n=4
# Uncomment to use n=2 for four-grams
#print("Generated Story with n=2 (Trigrams):")
#print(generate_story(n=2))  

# Uncomment to use n=3 for four-grams
#print("Generated Story with n=3 (Trigrams):")
#print(generate_story(n=3))  # Use n=3 for trigrams

# Uncomment to use n=4 for four-grams
print("Generated Story with n=4 (Trigrams):")
print(generate_story(n=4))  
##this is giving the best result among above two n grams