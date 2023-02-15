from fastapi import APIRouter, FastAPI

ENDPOINT = '/fastapi'

app = FastAPI(docs_url=f'{ENDPOINT}/docs', redoc_url=f'{ENDPOINT}/redoc', openapi_url=f'{ENDPOINT}/openapi.json')
prefix_router = APIRouter(prefix=ENDPOINT)
@prefix_router.get("/")
def root():
	return {"hello, this is fastapi"}

@prefix_router.get("/flag")
def world():
	return {"FLAG{hello_world}"}

app.include_router(prefix_router)
