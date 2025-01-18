import time
import random

candidates = ["Candidate A", "Candidate B", "Candidate C"]

vote_counts = {candidate: 0 for candidate in candidates}

def cast_vote():
    return random.choice(candidates)

try:
    print("Voting simulation started. Press Ctrl+C to stop.")
    while True:
        vote = cast_vote()
        vote_counts[vote] += 1

        print(f"Vote cast for: {vote}")
        print("Current vote counts:", vote_counts)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nVoting simulation stopped.")
    print("Final vote counts:", vote_counts)
