from config import FEATURE_WEIGHTS


class PredictionMerger:
    def __init__(self):
        self.feature_weights = FEATURE_WEIGHTS

    def merge(self, spacy_pred, scispacy_pred, text):
        final_row = {}
        confidence_row = {}
        source_row = {}

        for feature in self.feature_weights:
            spa_val = spacy_pred.get(feature)
            sci_val = scispacy_pred.get(feature)
            spa_weight = self.feature_weights[feature]["spacy"]
            sci_weight = self.feature_weights[feature]["scispacy"]

            if spa_val == sci_val and spa_val is not None:
                final_row[feature] = spa_val
                confidence_row[feature] = 3
                source_row[feature] = "both"
            elif spa_val and not sci_val:
                final_row[feature] = spa_val
                confidence_row[feature] = spa_weight
                source_row[feature] = "spacy"
            elif sci_val and not spa_val:
                final_row[feature] = sci_val
                confidence_row[feature] = sci_weight
                source_row[feature] = "scispacy"
            elif spa_val and sci_val and spa_val != sci_val:
                if spa_weight > sci_weight:
                    final_row[feature] = spa_val
                    confidence_row[feature] = 1
                    source_row[feature] = "spacy"
                else:
                    final_row[feature] = sci_val
                    confidence_row[feature] = 1
                    source_row[feature] = "scispacy"
            else:
                final_row[feature] = None
                confidence_row[feature] = 0
                source_row[feature] = None

        final_row["text"] = text
        confidence_row["text"] = text
        source_row["text"] = text
        return final_row, confidence_row, source_row
