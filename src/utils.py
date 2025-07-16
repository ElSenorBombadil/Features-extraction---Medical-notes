def load_corpus(file_path):
    """Loads a corpus from a text file, returning a list of sentences."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
