from translate import Translator
def translate_to_french(text):
    translator = Translator(to_lang="fr")
    translation = translator.translate(text)
    return translation

print("English to French Translator")
english_text = input("Enter the English text you want to translate: ")
translated_text = translate_to_french(english_text)
print("Translated text in French:", translated_text)







