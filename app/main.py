
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from . import auth, database, models, crud, schemas, email_utils
import httpx
from sqlalchemy.orm import Session



app = FastAPI()

# In-memory analytics example: simple hit counter
hit_counter = {"/analytics/hits": 0}

# Dependency for DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the General API!"}

# Auth endpoint
@app.post("/token", response_model=auth.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(auth.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected user endpoint
# Protected user endpoint
@app.get("/users/me", response_model=auth.User)
def read_users_me(current_user: auth.User = Depends(auth.get_current_active_user)):
    return current_user

# User registration endpoint
@app.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user.email, user.password, user.full_name)


# Email test endpoint
@app.post("/send-test-email")
def send_test_email(to_email: str, current_user: auth.User = Depends(auth.get_current_active_user)):
    """Send a test email to the specified address (must be authenticated)."""
    try:
        email_utils.send_email(
            to_email=to_email,
            subject="Test Email",
            body="This is a test email from your FastAPI project."
        )
        return {"message": f"Test email sent to {to_email}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")


# Third-party API integration example: Get a random joke
# Third-party API integration example: Get a random joke
@app.get("/external/joke")
async def get_random_joke():
    """Fetch a random joke from the official joke API (https://official-joke-api.appspot.com/random_joke)."""
    url = "https://official-joke-api.appspot.com/random_joke"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            return resp.json()
        raise HTTPException(status_code=502, detail="Failed to fetch joke from external API.")


# Example analytics endpoint: hit counter
@app.get("/analytics/hits")
def get_hit_count():
    hit_counter["/analytics/hits"] += 1
    return {"hits": hit_counter["/analytics/hits"]}


# Example file upload endpoint
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # For demo: just return file info, not saving
    return {"filename": file.filename, "size": len(content)}
