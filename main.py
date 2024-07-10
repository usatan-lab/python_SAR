from transformers import pipeline
import subprocess
import sys


def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def split_text_into_sentence(text):
    sentences = text.split('.')
    return [sentence.strip() for sentence in sentences if sentence.strip()]


if __name__ == "__main__":
    install_packages()
    sentiment_analysis = pipeline('sentiment-analysis')

    file_path = "long_text.txt"
    text = read_text_file(file_path)
    sentences = split_text_into_sentence(text)

    # Filter out invalid input
    valid_sentences = [sentence for sentence in sentences if len(sentence) > 0]

    if not valid_sentences:
        print("No valid sentences found for analysis.")
        sys.exit(1)

    results = sentiment_analysis(valid_sentences)

    positive_count = 0
    negative_count = 0

    for sentence, result in zip(valid_sentences, results):
        print(f"Text: {sentence}")
        print(f"Sentiment: {result['label']}, Score: {result['score']:.4f}")
        print()

    print("Packages installed successfully!")

    if positive_count > negative_count:
        print('POSITIVE STORY')
    else:
        print('NEGATIVE STORY')