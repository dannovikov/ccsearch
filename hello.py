from flask import Flask, request, render_template
from ccsearch import getVideoID, getCC, find

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/form')
def hello():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def my_form_post():
    link = request.form['link']
    search_term = request.form['search_term']

    vid_id = getVideoID(link)
    cc = getCC(vid_id)
    find(search_term, vid_id, cc)

    return render_template('results.txt')



#Recieve link through above post method,
#If captions:
#   Return video
# else:
    # return sorry
#Ask for search term
#If found:
#   for each found:
    #'div with found info and link to timestamp