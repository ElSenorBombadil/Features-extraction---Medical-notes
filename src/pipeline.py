import pandas as pd
from extractor import SpaCyExtractor, SciSpaCyExtractor
from merger import PredictionMerger


def process_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sentences = [line.strip() for line in f if line.strip()]

    spacy_extractor = SpaCyExtractor()
    scispacy_extractor = SciSpaCyExtractor()
    merger = PredictionMerger()

    results, confidences, sources = [], [], []

    for sentence in sentences:
        spacy_pred = spacy_extractor.extract(sentence)
        scispacy_pred = scispacy_extractor.extract(sentence)
        row, conf, src = merger.merge(spacy_pred, scispacy_pred, sentence)
        results.append(row)
        confidences.append(conf)
        sources.append(src)

    return pd.DataFrame(results), pd.DataFrame(confidences), pd.DataFrame(sources)
