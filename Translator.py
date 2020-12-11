from tkinter import *
from tkinter import ttk
from textblob import TextBlob

# ===|root|===
root = Tk()
root.geometry('550x500')
root.title('Translator')
root.resizable(False, False)
root.configure(bg='#cfe4ff')
root.iconbitmap('img/main_ico.ico')

# ===|utils|===
# --language-dictionary--
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
             'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
             'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
             'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co',
             'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
             'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
             'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu',
             'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn',
             'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
             'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
             'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
             'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
             'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
             'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
             'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
             'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
             'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
             'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
             'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
             'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

lang_dict_rev = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
                 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
                 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
                 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
                 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
                 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician',
                 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
                 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
                 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
                 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
                 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
                 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay',
                 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
                 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
                 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
                 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
                 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
                 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
                 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur',
                 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba',
                 'zu': 'zulu'}

# --font--
base_font = ('arial', 13)
text_font = ('arial', 11)
button_font = ('calibri', 13, 'bold')

# --colors--
label_bgcolor = '#b8d7ff'
button_bgcolor = '#267ded'
button_fgcolor = '#ffffff'
button_hover_color = '#4e94ed'
active_button_bgcolor = '#82b9ff'
active_button_fgcolor = '#ffffff'
frame_color = '#b8d7ff'

# --sizes--
label_width = 10
text_width = 44
text_height = 7
button_width = 25
frame_width = 540


# ===|functions|===
# --hover-effects--
def button_translate_enter(x):
    button_translate['bg'] = button_hover_color


def button_translate_exit(x):
    button_translate['bg'] = button_bgcolor


def button_detect_enter(x):
    button_detect['bg'] = button_hover_color


def button_detect_exit(x):
    button_detect['bg'] = button_bgcolor


# --main-functions--
def detect():
    word = TextBlob(text_in.get('1.0', 'end'))
    if len(word) > 2:
        label_detected_lang.configure(text=lang_dict_rev[word.detect_language()].upper())
    else:
        label_detected_lang.configure(text='')


def translate():
    text_out.delete('1.0', 'end')
    word = TextBlob(text_in.get('1.0', 'end'))
    if len(word) > 2:
        in_lang = word.detect_language()
        out_lang = lang_dict[language.get()]
        label_detected_lang.configure(text=lang_dict_rev[in_lang].upper())
        if in_lang == out_lang:
            text_out.insert('1.0', word)
        else:
            try:
                word_trans = word.translate(from_lang=in_lang, to=out_lang)
                text_out.insert('1.0', word_trans)
            except:
                print('exception raised')
                text_out.insert('1.0', word)

    else:
        text_out.insert('1.0', word)


# ===|layout|===
# --frames--
frame_in_block = Frame(root, bg=frame_color, width=frame_width, height=200)
frame_in_block.place(x=5, y=5)

frame_out_block = Frame(root, bg=frame_color, width=frame_width, height=200)
frame_out_block.place(x=5, y=210)

frame_button = Frame(root, bg=frame_color, width=frame_width, height=50)
frame_button.place(x=5, y=415)

frame_footer = Frame(root, bg=frame_color, width=frame_width, height=25)
frame_footer.place(x=5, y=470)

# --labels--
label_in = Label(frame_in_block, text='Enter text:', width=label_width, bg=label_bgcolor, font=base_font, anchor=E)
label_in.place(x=10, y=10)

label_lang_detect = Label(frame_in_block, text='Detected Language:', bg=label_bgcolor, width=label_width + 6,
                          font=base_font,
                          anchor=W)
label_lang_detect.place(x=10, y=160)

label_detected_lang = Label(frame_in_block, text='', bg=label_bgcolor, width=label_width + 10, font=base_font, anchor=W)
label_detected_lang.place(x=180, y=160)

label_out = Label(frame_out_block, text='Translated:', width=label_width, bg=label_bgcolor, font=base_font, anchor=E)
label_out.place(x=10, y=50)

label_choose = Label(frame_out_block, text='Translate to:', bg=label_bgcolor, width=label_width, font=base_font,
                     anchor=W)
label_choose.place(x=10, y=10)

# --texts--
text_in = Text(frame_in_block, width=text_width, height=text_height, font=text_font)
text_in.place(x=125, y=10)

text_out = Text(frame_out_block, width=text_width, height=text_height, font=text_font)
text_out.place(x=125, y=50)

# --combo-box--
language = StringVar()
combobox_lang = ttk.Combobox(frame_out_block, textvariable=language, width=30, state='readonly')
combobox_lang['values'] = [i for i in lang_dict.keys()]
combobox_lang.current(21)
combobox_lang.place(x=125, y=10)

# --buttons--
button_detect = Button(frame_button, text='DETECT LANGUAGE', width=button_width, font=button_font,
                       fg=button_fgcolor, bg=button_bgcolor,
                       activebackground=active_button_bgcolor, activeforeground=active_button_fgcolor,
                       command=detect)
button_detect.place(x=17, y=7)
button_detect.bind('<Enter>', button_detect_enter)  # hover effects
button_detect.bind('<Leave>', button_detect_exit)  # hover effects

button_translate = Button(frame_button, text='TRANSLATE', width=button_width, font=button_font,
                          fg=button_fgcolor, bg=button_bgcolor,
                          activebackground=active_button_bgcolor, activeforeground=active_button_fgcolor,
                          command=translate)
button_translate.place(x=287, y=7)
button_translate.bind('<Enter>', button_translate_enter)  # hover effects
button_translate.bind('<Leave>', button_translate_exit)  # hover effects

# --footer--
label_version = Label(frame_footer, text='Version: 1.0', bg=label_bgcolor)
label_version.place(x=470, y=2)

# ===|mainloop|===
root.mainloop()
