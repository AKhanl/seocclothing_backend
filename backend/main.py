from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend JS calls (safe for local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Demo products (later replace with Teespring API) ---
PRODUCTS = [
    {"id":"p1","title":"Essential Crew Tee","price":49,"image":"/static/images/p1.jpeg","colors":["#111111","#d9d9d9","#ffffff"]},
    {"id":"p2","title":"Classic Black Tee","price":49,"image":"/static/images/p2.jpeg","colors":["#111111","#cfcfcf","#ffffff"]},
    {"id":"p3","title":"Navy Minimal Tee","price":55,"image":"/static/images/p3.jpeg","colors":["#0b2a4a","#111111","#ffffff"]},
]



class SubscribePayload(BaseModel):
    email: str

@app.get("/api/products")
def get_products():
    return {"ok": True, "products": PRODUCTS}

@app.post("/api/subscribe")
def subscribe(payload: SubscribePayload):
    email = payload.email.strip().lower()

    if "@" not in email or "." not in email:
        return JSONResponse({"ok": False, "error": "Enter a valid email."}, status_code=400)

    # Later: save to DB / Mailchimp / Brevo etc.
    return {"ok": True}

# Serve static files

# Homepage
@app.get("/")
def home():
    return FileResponse("static/index.html")

