import time
import json

from TempHumidity import piTemp
from flask import *

# create flask app and pi temp and humidity
app = Flask(__name__)
pi_temp = piTemp()


@app.route("/")
def index():
    # Get the temperature and pass it to index.html
    celsius = pi_temp.read_temperature()
    fahrenheit = 9.0 / 5.0 * celsius + 32
    humid = pi_temp.read_humidity()
    fahrenheit1 = 9.0 / 5.0 * celsius + 32
    humid1 = pi_temp.read_humidity()
    fahrenheit2 = 9.0 / 5.0 * celsius + 32
    humid2 = pi_temp.read_humidity()
    return render_template('index.html', fahrenheit=fahrenheit, humid=humid,
                           fahrenheit1=fahrenheit1, humid1=humid1,
                           fahrenheit2=fahrenheit2, humid2=humid2)


@app.route("/temphumi")
def temphumi():
    def get_enviro_values():
        while True:
            celsius = pi_temp.read_temperature()
            fahrenheit = 9.0 / 5.0 * celsius + 32
            fahrenheit1 = pi_temp.read_temperature1()
            fahrenheit2 = pi_temp.read_temperature2()
            humidity1 = pi_temp.read_humidity1()
            humidity2 = pi_temp.read_humidity2()
            temphumi_state = {
                'fahrenheit': fahrenheit,
                'humidity': pi_temp.read_humidity(),
                'fahrenheit1': fahrenheit1,
                'humidity1': humidity1,
                'fahrenheit2': fahrenheit2,
                'humidity2': humidity2
            }
            yield ('data: {0}\n\n'.format(json.dumps(temphumi_state)))

            time.sleep(10.0)

    return Response(get_enviro_values(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
