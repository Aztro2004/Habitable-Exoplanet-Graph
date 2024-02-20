import requests

base_url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"

params = {
    'table': 'cumulative',
    'where': "koi_disposition like 'CANDIDATE' and koi_period>300 and koi_prad<2",
    'order': 'koi_period',
    'format': 'ascii'
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
