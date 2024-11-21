# Urdu Story Generator

This project is an **Urdu Story Generator** that uses N-gram models to generate meaningful sentences and stories in the Urdu language. The model is trained using the dataset from `urdu_stories.csv`, which contains Urdu stories. The primary goal is to build a system that generates new, random Urdu sentences and stories based on existing patterns observed in the dataset.

## Project Structure

- **urdu-story-generator/**: Main project folder
    - **venv/**: Virtual environment for project dependencies.
    - **requirements.txt**: A file that lists all the necessary libraries and dependencies required for the project.
    - **story_generator.py**: Python script containing the story generation logic.
    - **urdu_stories.csv**: Dataset containing the corpus of Urdu stories, used to train the N-gram model.

### Prerequisites

- Python 3.6+

### Steps to Set Up

1. **Clone the Repository**:
   Clone this repository to your local machine or GitHub Codespace.

   ```bash
   git clone https://github.com/<anjupy>>/urdu-story-generator.git
   cd urdu-story-generator
2. Create a Virtual Environment: Optional

Create and activate the virtual environment.
--> python -m venv venv
--> source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install Dependencies:

Install the required dependencies listed in requirements.txt.
--> pip install -r requirements.txt


4. Run the Story Generator:

After setting up the environment, you can run the story generator using the following command:
--> python story_generator.py
 This will generate random Urdu sentences and stories based on the trained N-gram model
 You can work further on this project to generate good urdu stories by adding more data to training and can add more best approaches.

## How It Works
The program first loads a CSV file (urdu_stories.csv) containing Urdu stories.
It tokenizes the text into words and builds N-gram models (bigram, trigram, or four-gram) to capture relationships between words.
The Conditional Frequency Distribution (CFD) is used to generate the next word in a sentence based on the previous words.
The story generation function starts with a random word from the model and continues generating sentences until the maximum length is reached.
## Model Details
Unigrams, Bigrams, Trigrams: The model can be customized to use 2-grams (bigrams), 3-grams (trigrams), or even 4-grams.
The more words in the model (higher n-grams), the more accurate the generated sentences become, but the model becomes more complex as well.
