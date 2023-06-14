from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="BeCloserApp")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

# GINO event routes
# from database.events_router import router as database_events
# app.include_router(
#     database_events
# )

# site routes
from routes import router as main_router
app.include_router(
    main_router,
    # prefix="/",
    tags=["main"]
)