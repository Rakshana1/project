from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import pandas as pd
from scipy import stats
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
# Load your data and precompute the cosine similarity matrix

df = pickle.load(open('model/df.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))



# Update the recommendation function to handle discrepancies in AI tool name formatting
# Update the recommendation function to handle discrepancies in AI tool name formatting
def recommend_ai_tools(aitool, df, similarity, top_n=5):
    # Standardize the AI tool names by stripping leading/trailing spaces and converting to lowercase
    standardized_aitool = aitool.strip().lower()
    # Find the standardized name in the dataset
    matches = df['aitool'].str.lower().str.strip() == standardized_aitool
    if not matches.any():
        return "AI tool not found in the dataset."
    
    # Get the index of the AI tool in the DataFrame
    idx = df[matches].index[0]

    # Get the pairwise similarity scores of all AI tools with that AI tool
    sim_scores = list(enumerate(similarity[idx]))

    # Sort the AI tools based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top-n most similar AI tools
    sim_scores = sim_scores[1:top_n+1]

    # Get the AI tool indices
    ai_tool_indices = [i[0] for i in sim_scores]
    
    # Return the top-n most similar AI tools
    return df['aitool'].iloc[ai_tool_indices].tolist()

# Let's try the recommendation function again with the corrected name

#flask app
app = Flask(__name__)



# Define route for the index page
@app.route('/')
def index():
    return render_template('home.html')

# Define route for the index page
@app.route('/tool')
def tool():
    return render_template('tool.html')

#productivity tools
@app.route('/website')
def website():
    return render_template('website-builders.html')

@app.route('/market')
def market():
    return render_template('marketing.html')

@app.route('/finance')
def finance():
    return render_template('finance.html')

@app.route('/project')
def project():
    return render_template('project-management.html')

@app.route('/social')
def social():
    return render_template('social-media.html')

@app.route('/product')
def product():
    return render_template('productivity.html')

#ai video generators

@app.route('/enhancer')
def enhancer():
    return render_template('video-enhancer.html')

@app.route('/edit')
def edit():
    return render_template('video-editing.html')

@app.route('/generators')
def generators():
    return render_template('video-generators.html')

@app.route('/text')
def text():
    return render_template('text-to-video.html')


@app.route('/gener')
def gener():
    return render_template('video-generators.html')

#ai text generators

@app.route('/prompt')
def prompt():
    return render_template('prompt-generators.html')

@app.route('/write')
def write():
    return render_template('writing-generators.html')

@app.route('/para')
def para():
    return render_template('paraphrasing.html')

@app.route('/story')
def story():
    return render_template('storyteller.html')

@app.route('/copy')
def copy():
    return render_template('copywriting-assistant.html')

@app.route('/textgen')
def textgen():
    return render_template('text-generators.html')

#ai image generators

@app.route('/design')
def design():
    return render_template('design-generators.html')

@app.route('/image')
def image():
    return render_template('image-generators.html')

@app.route('/imgedit')
def imgedit():
    return render_template('image-editing.html')

@app.route('/textimg')
def textimg():
    return render_template('text-to-image.html')

@app.route('/imggen')
def imggen():
    return render_template('image-generators.html')

#ai art generators

@app.route('/cartoon')
def cartoon():
    return render_template('cartoon-generators.html')

@app.route('/portrait')
def portrait():
    return render_template('portrait-generators.html')

@app.route('/imgimg')
def imgimg():
    return render_template('image-to-image.html')


@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/draw')
def draw():
    return render_template('drawing.html')

@app.route('/artgen')
def artgen():
    return render_template('art-generators.html')

#ai audio generators

@app.route('/audedit')
def audedit():
    return render_template('audio-editing.html')

@app.route('/ttospe')
def ttospe():
    return render_template('text-to-speech.html')

@app.route('/music')
def music():
    return render_template('music-generator.html')

@app.route('/trans')
def trans():
    return render_template('transcriber.html')

@app.route('/audgen')
def audgen():
    return render_template('audio-generators.html')

#ai misc tools

@app.route('/fit')
def fit():
    return render_template('fitness.html')

@app.route('/reli')
def reli():
    return render_template('religion.html')

@app.route('/free')
def free():
    return render_template('free.html')

@app.route('/gen')
def gen():
    return render_template('generative.html')

@app.route('/fashion')
def fashion():
    return render_template('fashion-assistant.html')

@app.route('/misc')
def misc():
    return render_template('misc-tools.html')

#ai code generators

@app.route('/code')
def code():
    return render_template('code-assistant.html')

@app.route('/nocode')
def nocode():
    return render_template('no-code.html')

@app.route('/sql')
def sql():
    return render_template('sql-assistant.html')

@app.route('/cogen')
def cogen():
    return render_template('code-generators.html')





































# Define route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Define route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define route for the recommendation page

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    tool_list = df['aitool'].values
    status = False
    if request.method == "POST":
        try:
            if request.form:
                aitool = request.form['df']
                print(aitool)
                recommended_tools_name = recommend_ai_tools(aitool,df,similarity,top_n=5)
                print(recommended_tools_name)
                status = True

                return render_template("recommendation.html", aitool = recommended_tools_name,  tool_list = tool_list, status = status)




        except Exception as e:
            error = {'error': e}
            return render_template("recommendation.html",error = error, tool_list = tool_list, status = status)

    else:
        return render_template("recommendation.html", tool_list = tool_list, status = status)
    
                

if __name__ == '__main__':
    app.debug = True
    app.run()
