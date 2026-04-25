"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed."""
    capitalized = title.title()
    return capitalized

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present."""
    has_period = '.' in sentence
    return has_period

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence."""
    cleaned_sentence = sentence.strip()
    return cleaned_sentence

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one."""
    processed_sentence = sentence.replace(old_word, new_word)
    return processed_sentence