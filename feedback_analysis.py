<<<<<<< HEAD
def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback_percentage(ratings)}%")
=======
def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {positive_feedback_percentage(ratings)}%")
>>>>>>> 4f033417f855d4a2df2714cf467ed7d9db94dfe7
