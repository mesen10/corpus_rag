import os
import re
import requests

# Dictionary containing book metadata and Project Gutenberg URLs
BOOKS = {
    "The Odyssey": {
        "id": 1727,
        "author": "Homer",
        "filename": "the_odyssey.txt",
        "url": "https://www.gutenberg.org/files/1727/1727-0.txt",
    },
    "Alice in Wonderland": {
        "id": 11,
        "author": "Lewis Carroll",
        "filename": "alice_in_wonderland.txt",
        "url": "https://www.gutenberg.org/files/11/11-0.txt",
    },
    "Romeo and Juliet": {
        "id": 1513,
        "author": "William Shakespeare",
        "filename": "romeo_and_juliet.txt",
        "url": "https://www.gutenberg.org/files/1513/1513-0.txt",
    },
    "Crime and Punishment": {
        "id": 2554,
        "author": "Fyodor Dostoevsky",
        "filename": "crime_and_punishment.txt",
        "url": "https://www.gutenberg.org/files/2554/2554-0.txt",
    },
}

DOWNLOAD_DIR = "./books"


def clean_gutenberg_text(raw_text: str) -> str:
    """Removes standard Project Gutenberg header and footer boilerplates."""
    # Find start marker
    start_match = re.search(
        r"\*\*\*\s*START OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*",
        raw_text,
        re.IGNORECASE,
    )
    # Find end marker
    end_match = re.search(
        r"\*\*\*\s*END OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*",
        raw_text,
        re.IGNORECASE,
    )

    start_idx = start_match.end() if start_match else 0
    end_idx = end_match.start() if end_match else len(raw_text)

    # Return only the book content inside the markers
    return raw_text[start_idx:end_idx].strip()


def download_books():
    """Downloads all books in the dictionary and saves them locally."""
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RAG-Demo-App/1.0"
    }

    print(f"Starting download to '{DOWNLOAD_DIR}/'...\n")

    for title, info in BOOKS.items():
        file_path = os.path.join(DOWNLOAD_DIR, info["filename"])

        if os.path.exists(file_path):
            print(f"✓ '{title}' already exists locally. Skipping download.")
            continue

        print(f"Downloading '{title}' (Gutenberg ID: {info['id']})...")
        try:
            response = requests.get(info["url"], headers=headers, timeout=15)
            response.raise_for_status()

            # Clean header and footer
            cleaned_text = clean_gutenberg_text(response.text)

            # Save clean text file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"✓ Saved to {file_path}\n")

        except requests.RequestException as e:
            print(f"✗ Failed to download '{title}': {e}\n")


if __name__ == "__main__":
    download_books()