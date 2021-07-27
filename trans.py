from translate import Translator

lang1=str(input("enter the language that script is given "))
lang2=str(input("Language you want to translate "))
t=Translator(from_lang = lang1.capitalize(), to_lang=lang2.capitalize())
str1=str(input("Give Some Text..   :"))
str2=t.translate(str1)

print("Translated script is...",str2)