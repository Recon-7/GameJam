def increase_difficulty(level):
    return max(1, 3 - level * 0.1)  # Decrease speed interval as level increases