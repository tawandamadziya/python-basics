def get_text(sline):
    capitalized=sline.capitalize()
    if sline.startswith(("is","where","are","how","when","who")):   #sline.startswith(("is","where","are","how","when","who")) in brackets is a tuple
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)    

text_s=input("Say something: ")
print(get_text(text_s))



#Same code, different methode
def get_text(sline):
    tuple_text=("is","where","are","how","when","who")
    capitalized=sline.capitalize()
    if sline.startswith(tuple_text):  
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)    

text_s=input("Say something: ")
print(get_text(text_s))