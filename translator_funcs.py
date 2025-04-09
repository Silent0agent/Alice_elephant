from deep_translator import GoogleTranslator


def translate_word(word):
    translated = GoogleTranslator(source='auto', target='en').translate(word)
    return translated
