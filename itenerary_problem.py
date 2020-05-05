def get_itinerary(tickets):
    order = []
    from_to_dictionary = {}
    # build dictionary
    for item in tickets:
        from_island = item[0]
        to_island = item[1]
        from_to_dictionary[from_island] = to_island
    # find the start
    start_island = ""
    for from_island in from_to_dictionary.keys():
        if from_island not in from_to_dictionary.values():
            start_island = from_island
            break
    print(start_island)
    current_island = start_island
    order.append(current_island)
    for i in range(len(tickets)):
        # order.append(current_island)
        current_island = from_to_dictionary[current_island]
        order.append(current_island)



    return order





tickets = [("Noodle", "Jungalow"), ("Korok","Bunpun"), ("Bunpun", "Noodle"), ("Jungalow", "Astra Nova")]


print(get_itinerary(tickets))
