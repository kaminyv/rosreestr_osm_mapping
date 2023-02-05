from flask import Flask, render_template
from rosreestr2coord import Area

poly = {"type": "Feature",
        "properties": {"kvartal": "38:6:144003", "sale_price": None, "sale_cnt": None, "sale_date": None,
                       "area_unit": "055", "cad_cost": 271540.0, "cc_date_approval": None, "rifr_dep": None,
                       "sale_doc_num": None, "parcel_type": "parcel", "cn": "38:06:144003:4723", "parcel_tour": False,
                       "kvartal_cn": "38:06:144003", "sale_doc_type": None, "parcel_build": False, "sale": None,
                       "rifr": None, "is_big": False,
                       "util_by_doc": "\u0434\u043b\u044f \u0434\u0430\u0447\u043d\u043e\u0433\u043e \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430",
                       "rifr_cnt": None, "cad_unit": "383", "area_type": "009", "id": "38:6:144003:4723",
                       "parcel_tour_attrs": None, "category_type": "003001000000", "rifr_dep_info": None,
                       "children": None, "statecd": "06", "date_cost": "01.01.2022", "cc_date_entering": "21.01.2023",
                       "sale_dep": None, "fp": 100, "sale_doc_date": None, "parcel_build_attrs": None,
                       "sale_dep_uo": None, "area_value": 1000.0,
                       "address": "\u0418\u0440\u043a\u0443\u0442\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c, \u0418\u0440\u043a\u0443\u0442\u0441\u043a\u0438\u0439 \u0440\u0430\u0439\u043e\u043d, 19 \u043a\u043c \u0413\u043e\u043b\u043e\u0443\u0441\u0442\u043d\u0435\u043d\u0441\u043a\u043e\u0433\u043e \u0442\u0440\u0430\u043a\u0442\u0430, \u0434\u0430\u0447\u043d\u043e\u0435 \u043d\u0435\u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u043e\u0435 \u0442\u043e\u0432\u0430\u0440\u0438\u0449\u0435\u0441\u0442\u0432\u043e \"\u042f\u0441\u043d\u043e\u0435\", \u0443\u043b. \u0411\u0435\u0440\u0435\u0433\u043e\u0432\u0430\u044f, \u0443\u0447\u0430\u0441\u0442\u043e\u043a \u2116 136",
                       "application_date": "01.01.2023", "center": {"x": 104.63489884158952, "y": 52.266512291557405}},
        "geometry": {"type": "MultiPolygon", "coordinates": [[[[104.63460124177388, 52.26667269308686],
                                                               [104.63450422372321, 52.266502883687544],
                                                               [104.63519499224408, 52.26635326088061],
                                                               [104.63529006993375, 52.26652307085298],
                                                               [104.63460124177388, 52.26667269308686]]]]},
        "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}}

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )


@app.route('/')
def index():  # put application's code here
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
