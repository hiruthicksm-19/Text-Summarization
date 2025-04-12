from rouge_score import rouge_scorer

def evaluate_summary(reference, summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, summary)
    return {
        key: {
            "precision": round(value.precision, 4),
            "recall": round(value.recall, 4),
            "f1": round(value.fmeasure, 4)
        } for key, value in scores.items()
    }
