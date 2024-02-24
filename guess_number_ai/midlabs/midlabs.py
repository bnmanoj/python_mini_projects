import random

def mad_libs():
    # Mad Libs template
    template = "Once upon a time, in a [adjective] [noun], there was a [adjective] [noun]. One day, it decided to [verb] [adverb]. The [noun] was very [adjective], and everyone in the [noun] was [emotion]."

    # List of parts of speech
    parts_of_speech = ['adjective', 'noun', 'verb', 'adverb', 'emotion']

    # Dictionary to store user inputs
    user_inputs = {}

    # Get user inputs
    for part_of_speech in parts_of_speech:
        user_input = input(f"Enter an {part_of_speech}: ")
        user_inputs[part_of_speech] = user_input

    # Fill in the blanks
    filled_story = template
    for part_of_speech, user_input in user_inputs.items():
        filled_story = filled_story.replace(f"[{part_of_speech}]", user_input)

    # Display the filled story
    print("\nYour Mad Libs Story:")
    print(filled_story)

# Run the Mad Libs game
mad_libs()
