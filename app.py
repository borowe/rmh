from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/syncshit')
def sync_it():
    #do some awesome shit
    #talk to shopify
    #sync some booze
    bob_says = 'Hello edo!'
    return bob_says

@app.route('/anotherexample')
def example_html_render():
    bilbo = 'do' + ' some' + ' stuff, yahoo!'
    return render_template('example.html', name=bilbo)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host= '0.0.0.0', port='5000')

