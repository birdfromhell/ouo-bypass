from fastapi import FastAPI
from pydantic import BaseModel
from bypass import ouo_bypass

app = FastAPI()


class Url(BaseModel):
    url: str


@app.get('/')
def root():
    return {'message': 'This is ouo.io Bypass'}


@app.post('/bypass/')
def bypass(url: Url):
    result = ouo_bypass(url.url)

    return result
