from flask import Flask, request

app = Flask(__name__)

sre = [
    {
        "name": "SRE",
        "skills": [
            {
            "IaC": "Terraform",
            "level": 100
            }
        ]
        
    }
]


@app.get('/sre') # 'http://127.0.0.1:60000/sre'
def get_sre():
    return {"sre": sre}


## Run it locally (debug)
#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=60000)  # Keeps it running
