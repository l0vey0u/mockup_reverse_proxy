from fastapi import APIRouter, FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os, tempfile, shutil, base64
FLAG = 'FLAG{**REMOVED**}'
ENDPOINT = '/bubble'
config = {
	'docs_url': ENDPOINT+'/docs',
	'redoc_url': ENDPOINT+'/redoc',
	'openapi_url': ENDPOINT+'/openapi.json',
	'flag': f'{FLAG}'
}

log_path = tempfile.mkdtemp()
app = FastAPI(**config)
prefix_router = APIRouter(prefix=ENDPOINT)
app.mount(ENDPOINT+"/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory=["templates",log_path], autoescape=False, auto_reload=True)

filter_word = [
    "config",
    "class",
    "mro",
    "base",
    "subclasses",
    "main"
]


def filter(msg):
    if any(filtering in msg.lower() for filtering in filter_word):
        msg = "해킹은 나쁜거야!!"
    return msg


def echo(request, t):
    try:
    	return templates.TemplateResponse(f"{t}.html", {"request": request})
    except:
    	return HTMLResponse(content="머라 보낸거야 -- 못 따라하겠어 ㅜㅜ", status_code=200)


@prefix_router.get("/", response_class=HTMLResponse)
async def chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@prefix_router.post("/send")
async def send(request: Request, msg: str = Form()):
    try:
    	msg = base64.b64decode(msg).decode()
    	msg_raw = """%s""" % msg
    except:
        msg_raw = ""
    # LOG chats for ban cheat user
    t = int(datetime.now().timestamp())
    log_file = os.path.join(log_path, f"{t}.html")
    open(log_file, "w").write(msg_raw)
    return echo(request, t)

app.include_router(prefix_router)
