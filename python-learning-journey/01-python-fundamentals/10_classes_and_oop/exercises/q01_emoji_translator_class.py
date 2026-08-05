"""
Question:
Build a Translator class with an emoji dictionary stored as an instance
attribute, and a method translate(sentence) that replaces matching words
(like ":)") with their emoji before returning the sentence.

"""


class Translator:
    def __init__(self):
        self.emojis = {
            ":)": "😄",
            ":(": "😢",
            ":love:": "❤️",
            ":thumbsup:": "👍",
        }

    def translate(self, sentence):
        words = sentence.split()
        result = []
        for word in words:
            result.append(self.emojis.get(word, word))
        return " ".join(result)


if __name__ == "__main__":
    translator = Translator()
    print(translator.translate("I am happy :) and I :love: pizza"))
    print(translator.translate("Feeling :( today"))