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
        input=input.replace('පිතිකරුවන්', 'පිතිකරු')
        input=input.replace('ක්‍රීඩකයන්', '')
        input=input.replace('ක්‍රීඩකයින්', '')
        input=input.replace('ශ්‍රී ලංකා', 'ශ්‍රී ලංකාව')
        input=input.replace('එංගලන්ත', 'එංගලන්තය')
        input=input.replace('පකිස්ථාන', 'පකිස්ථානය')
        input=input.replace('නවසීලන්ත', 'නවසීලන්තය')
        input=input.replace('ඕස්ට්‍රේලියානු', 'ඕස්ට්‍රේලියාව')
        input=input.replace('ඉන්දියානු', 'ඉන්දියාව')
        input=input.replace('දකුණු අප්රිකානු', 'දකුණු අප්රිකාව')
   
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
