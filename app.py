from flask import Flask, request, jsonify
from nltk.stem import WordNetLemmatizer
app = Flask(__name__)


@app.route('/')
def hello_world():
    data = request.json
    print(data)
    result_string = ""
    lemmatizer = WordNetLemmatizer()
    lemma_list = []
    lemma_list.append( lemmatizer.lemmatize("rocks"))
    lemma_list.append(lemmatizer.lemmatize("corpora"))
    
    # a denotes adjective in "pos"
    lemma_list.append( lemmatizer.lemmatize("better", pos ="a"))
    print(lemma_list)
    for lemma in lemma_list:
        result_string += '{} '.format(lemma)

    print(result_string)
    return result_string