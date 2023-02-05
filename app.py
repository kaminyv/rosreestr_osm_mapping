from flask import Flask, render_template
from rosreestr2coord import Area

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-piece/<string:piece_id>')
def piece(piece_id: str = None):
    area = Area(piece_id, use_cache=False, with_proxy=True)
    response = area.to_geojson_poly()

    if response:
        return response

    return {'message': 'The object was not found.'}


if __name__ == '__main__':
    app.run()
