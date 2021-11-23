from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import os
import search

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    # input = request.args.get("input")
    input = request.form.get("input")
    if input is not None:
        # print(len(input.split(" ")))
        if "*" in input:
            fields = ['nameEn', 'nameSi', 'country', "dateOfBirth","playingRole","bowlingStyle","battingStyle"]
            input=input.split("*")
            term1=input[0]
            term2=input[1]
            result = search.es_wildcard_query(fields,term1,term2)
            return render_template('search.html', input=input, cricketers=result)
        else:
            fields = ['nameEn', 'nameSi', 'country', "dateOfBirth","playingRole","bowlingStyle","battingStyle"]
            result = search.search_text_multi_match_query(input, fields)
            return render_template('search.html', input=input, cricketers=result)

        

    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
