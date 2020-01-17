import fiona
import requests
import json
import zipfile
import io
import os
import xml.etree.ElementTree as ET
import pandas as pd


# Download en unzip bestand
def download_and_unzip(name, zip_url, folder):

    x = r'{}\depositie_gml'.format(folder)

    r = requests.get(zip_url)
    z = zipfile.ZipFile(io.BytesIO(r.content)) # read file to memory
    z.extract(z.namelist()[0], x)
    
    src = '{}\{}'.format(x, z.namelist()[0])
    dst = '{}\{}'.format(x, name)
    os.rename(src, dst)


# Schrijf OPS input bestand (.brn)
def write_brn(ft_dict, temp_path):
    header = r'snr   x(m)    y(m)   q(g/s)     hc(MW) h(m)    r(m)  ' \
             's(m)  dv    cat   area  ps  component     bronomschrijving'

    data = '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}'.format(
        ft_dict['ai_code'][-4:].ljust(6), ft_dict['x'].ljust(7), ft_dict['y'].ljust(7),
        ft_dict['q'].ljust(11), ft_dict['hc'].ljust(7), ft_dict['h'].ljust(8),
        ft_dict['r'].ljust(6), ft_dict['s'].ljust(6), ft_dict['dv'].ljust(2),
        ft_dict['cat'].ljust(7), ft_dict['area'].ljust(4), ft_dict['ps'].ljust(3),
        ft_dict['component'].ljust(14), ft_dict['bronomschrijving'])

    brn = header + '\n' + data

    '''
    path = r"{}\brn\{}.brn".format(temp_path, ft_dict['ai_code'])
    with open(path, 'w') as brnfile:
        brnfile.write(brn)
    '''
    
    # Return BRN string en de ai_code
    return brn


def calculate_job(api_key, gml, job_naam, year):
    endpoint = 'https://connect.aerius.nl/api/5/calculate'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {
        "apiKey": api_key,
        "options": {
            "calculationType": "NBWET",
            "year": year,
            "substances": ["NOX", "NH3"],
            "name": job_naam,
            "aggregate": True,
            "permitCalculationRadiusType": "NONE",
            "researchArea": False,
            "permitReportType": "DEMAND",
            "outputOptions": {
                "sectorOutput": False
            }
        },
        "calculateDataObjects": [
            {
                "contentType": "TEXT",
                "dataType": "GML",
                "data": gml,
                "researchArea": False
            }
        ],
        "strict": False
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    return response


def generate_api_key(email):
    endpoint = 'https://connect.aerius.nl/api/5/generateAPIKey'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {'email': email}
    print(endpoint, headers, data)
    return requests.post(endpoint, headers=headers, data=json.dumps(data))


def get_job_status(api_key):
    endpoint = 'https://connect.aerius.nl/api/5/status/jobs'
    headers = {'Accept': 'application/json'}
    params = {'apiKey': api_key}
    
    response = requests.get(endpoint, headers=headers, params=params)    
    return response

def convert_brn_to_gml(brn_in, substance):
    endpoint = 'https://connect.aerius.nl/api/5/convert'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {
        "dataObject":
            {
                "contentType": "TEXT",
                "dataType": "BRN",
                "data": brn_in,
                "substance": substance
            }        
    }

    return (requests.post(endpoint, headers=headers, data=json.dumps(data)))



def yield_receptor_data(gml):
    tree = ET.parse(gml)
    root = tree.getroot()    
    
    for i in root.findall('.//{http://imaer.aerius.nl/2.1}ReceptorPoint'):

        receptor_id = i.find('.//{http://imaer.aerius.nl/2.1}localId').text
        
        nox = i.find(".//{http://imaer.aerius.nl/2.1}Result[@substance='NOX']/{http://imaer.aerius.nl/2.1}value")
        nh3 = i.find(".//{http://imaer.aerius.nl/2.1}Result[@substance='NH3']/{http://imaer.aerius.nl/2.1}value")
        depositie = extractEmission(nox, nh3)
        
        coors = i.find(".//{http://www.opengis.net/gml/3.2}posList").text.split(' ')
        wkt = "POLYGON (({} {}, {} {}, {} {}, {} {}, {} {}, {} {}, {} {}))".format(*coors)
                  
        if depositie > 0:
            data = [receptor_id[3:], round(depositie,4), wkt]        
            yield(data)
    

def extractEmission(nox, nh3):
    try:
        nox = float(nox.text)
    except:
        nox = 0
    try:
        nh3 = float(nh3.text)
    except:
        nh3 = 0

    return(nox+nh3)


if __name__ == '__main__':
    pass

