from fastapi import FastAPI
import uvicorn

api = FastAPI()

@api.get('/')
def home():
    return "Api testing for credit risk model!"

@api.post('/predict')
def predict():
    return 'prediction'

if __name__ == "__main__":
    uvicorn.run("api:api", host="0.0.0.0", port=8000, reload=True)
