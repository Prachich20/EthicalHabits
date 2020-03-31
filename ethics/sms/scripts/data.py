import spacy
nlp = spacy.load('en_core_web_sm')


def extract():
    sentence = "woolworths is located in uk"
    doc = nlp(sentence.title())
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            print(ent.text)



if __name__ == '__main__':
    extract()