def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_counter = 0 
    oranges_counter = 0
    for apple in apples:
        apple_position = apple + a
        if apple_position >= s and apple_position <= t : 
            apples_counter += 1
    for orange in oranges:
        orange_position = orange + b
        if orange_position >= s and orange_position <= t:
            oranges_counter += 1
    print(f'{apples_counter}\n{oranges_counter}')
    