def autocomplete_list(user_input, master_list):

    suggestions = [
        word
        for word in master_list
        if word.lower().startswith(user_input.lower())
    ]

    return suggestions
