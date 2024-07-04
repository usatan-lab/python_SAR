from transformers import pipeline

import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)


if __name__ == "__main__":
    install_packages()
    # Below is the main code of main.py
    sentiment_analysis = pipeline("sentiment-analysis")
    texts = [
        "I love using Python for make game.",
        "This product didn't meet my expectations.",
        "I'm not sure how I feel about this.",
        "I hate this"
    ]

    results = sentiment_analysis(texts)

    for text, result in zip(texts, results):
        print(f"Text: {text}")
        print(f"sentiment: {result['label']},Score: {result['score']:.4f}")
        print("Packages installed successfully!")

