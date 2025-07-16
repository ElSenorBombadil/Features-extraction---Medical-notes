from src.pipeline import process_corpus
from evaluation.true_labels import df_true
from evaluation.evaluate import evaluate_extraction

if __name__ == "__main__":
    df_results, df_confidence, df_sources = process_corpus("data/corpus.txt")

    df_results.to_csv("output/df_results.csv", index=False)
    df_confidence.to_csv("output/df_confidence.csv", index=False)
    df_sources.to_csv("output/df_sources.csv", index=False)

    print("Process completed. Results saved in /output.")

# Overview of the extraction results
evaluate_extraction(df_true, df_results)
