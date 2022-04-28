from cs50 import get_int

amount_of_scores = 0
score_list = []

# Asking for positive integer from user
while (amount_of_scores <= 0):
    amount_of_scores = get_int("How many scores? ")

# Asks for individual scores then adds them to a list
for i in range(amount_of_scores):
    score = get_int("Score: ")
    score_list.append(score)

# Result
high_score = max(score_list)

print(f"High score: {high_score}")