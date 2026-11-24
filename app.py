from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()
#loads all data from the json
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

#endpoint view
@app.get('/view')
def view():
    data = load_data()

    return data

#endpoint for specific pateint id 1 path parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient', example='P00X where X = 0 to N')):
    #load data of all patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        #return {'error' : 'patient not found'}
        raise HTTPException(status_code = 404, detail = 'Patient not found.')

#endpoint for specific pateint id 2 using query parameter
@app.get('/sort')
def sort_patient(sort_by : str = Query(..., description='Sort on the basis if weight, height and or bmi'), order: str = Query('asc', ) ):
    valid_field = ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail='Invalid field selected from {valid_field}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, detail='Invalid field selected from asc or desc')

    data = load_data()

    sorted_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sorted_order)

    return sorted_data