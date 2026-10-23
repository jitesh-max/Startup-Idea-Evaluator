# evaluator.py
def evaluate_startup(idea):
    score = 0
    print("\nEvaluating your startup idea...")

    if len(idea['problem']) > 10:
        score += 2
    if len(idea['unique']) > 10:
        score += 2
    if len(idea['market']) > 10:
        score += 2
    if "none" in idea['competition'].lower():
        score += 2
    elif len(idea['competition']) > 10:
        score += 1
    if any(word in idea['monetization'].lower() for word in ['subscription', 'ads', 'sales', 'commission']):
        score += 2

    if score >= 8:
        result = "Strong Potential ✅"
    elif score >= 5:
        result = "Moderate Potential ⚠️"
    else:
        result = "Weak Potential ❌"

    return score, result
