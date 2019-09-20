from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    search = request.args.get('search')

    print(search)


    # TODO: Extract the query term from url using request.args.get() √



    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'





    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation

# set the apikey and limit
    apikey = "LIVDSRZULELA"  # test value
    lmt = 10

    # our test search
    search_term = search

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(r.content)
        print(top_10gifs)
    else:
        top_10gifs = None


# continue a similar pattern until the user makes a selection or starts a new search.


    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object




    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    gif_list = top_10gifs["results"]




    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'





    return render_template("index.html",
    gif_list = gif_list)


if __name__ == '__main__':
    app.run(debug=True)
