
from translate import Translator

lang_shortcut = "ja" 

translator = Translator(to_lang="{}".format(lang_shortcut))

try:
    with open('./text.txt', mode='r') as my_file:

        text = my_file.read()
        translation = translator.translate(text)

        with open('./text_{}.txt'.format(lang_shortcut), mode='w') as translated_file:

            translated_file.write(translation)    

except FileNotFoundError as err:

    print('Check file path and try again')



