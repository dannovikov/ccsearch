from flask import Flask, request, render_template
from ccsearch import getVideoID, getCC, find
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    link = request.form['link']
    search_term = request.form['search_term'].lower()

    vid_id = getVideoID(link)
    cc = getCC(vid_id)
    results = find(search_term, vid_id, cc)
    if results[0] == 'NC':
        return render_template('nocaptions.html')
    elif results[0] == 'NF':
        return render_template('notfound.html')
    else:
        return render_template('results.html',
                                results = results,
                                search_term = search_term,
                                link = link)



#Recieve link through above post method,
#If captions:
#   Return video
# else:
    # return sorry
#Ask for search term
#If found:
#   for each found:
    #'div with found info and link to timestamp
