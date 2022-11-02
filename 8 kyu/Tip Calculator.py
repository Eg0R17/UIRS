import math
def calculate_tip(amount, rating):
    rating = rating.lower();
    recognizedRating = ["terrible", "poor", "good", "great", "excellent"]
    if rating not in recognizedRating:
        return "Rating not recognised"
    if rating in recognizedRating:
        if (rating == "terrible"):
            return (amount * 0);
        if (rating == "poor"):
            return math.ceil(amount * 0.05);
        if (rating == "good"):
            return math.ceil(amount * 0.1);
        if (rating == "great"):
            return math.ceil(amount * 0.15);
        else:
            return math.ceil(amount * 0.2);