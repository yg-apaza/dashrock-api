import uvicorn
from app.settings import PORT, RELOAD

if __name__ == "__main__":
    uvicorn.run(
        "app.api.main:app", host="0.0.0.0", port=PORT, reload=RELOAD
    )
