from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get('query')
    
    # TODO: Extract the query term from url using request.args.get() √

    query = request.args.get('query')

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    # 'params' is defining the parameter values for each variable
    params = {
        
        "s": search,

        "apikey" = "LIVDSRZULELA",  # test value

        "lmt" = 10,   
    }




    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search", params = params)


    # use '.json()' function to get the JSON of the return function
    if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(r.content)
        #print(top_10gifs)
        top_9gifs = top_9gifs["results"]
    else:
        top_10gifs = None


    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs = top_10gifs)

@app.route("/search-result")
def search_results():
    query = request.args.get('search')
    # set the apikey and limit
    search = {
        "s": search,

        "apikey" = "LIVDSRZULELA",  # test value

        "lmt" = 10,
    }

    # get the top 8 GIFs for the search term
    r = requests.get("https://api.tenor.com/v1/search", params = search)
    #("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s(search_term, apikey, lmt))"

    if r.status_code == 200:
        searchResult = json.loads(r.content)
        searchResult = searchResult["results"]
    else:
        searchResult = None
    
    return render_template("index.html", gifs = searchResult)


if __name__ == '__main__':
    app.run(debug=True)
    
