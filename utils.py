def calculate_score(item_type, correct_bin):
    recyclable_items = ['plastic', 'paper', 'can']
    general_waste_items = ['food_scraps', 'wrappers', 'hazardous_materials']
    
    if correct_bin == 'recycling' and item_type in recyclable_items:
        return 10
    elif correct_bin == 'general' and item_type in general_waste_items:
        return 10
    else:
        return -5

def increase_difficulty(level):
    return max(1, 3 - level * 0.1)  # Decrease speed interval as level increases