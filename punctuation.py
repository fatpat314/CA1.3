# def remove_punctuation(text):
#     punctuation = ["!","?","."," "]
#     text = list(text)
#
#     for i in text:
#         if i in punctuation:
#             print(i)
#             print(text)
#             text.remove(i)
#     print(text)
#
# remove_punctuation("taco? cat.")


def punctuation(text):
    text = text.replace(" ", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("-", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("\'", "")
    return text

# print(punctuation("taco? cat."))

def test(text):
    text = punctuation(text)
    print (text)
test("does, this, work?")
