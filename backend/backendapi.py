from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Willkommen zur FastAPI-Anwendung! - 3"}

def get_git_commit_info():
    try:
        commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        commit_date = subprocess.check_output(["git", "log", "-1", "--format=%cd"]).decode().strip()
        commit_message = subprocess.check_output(["git", "log", "-1", "--format=%B"]).decode().strip()
        return commit_hash, commit_date, commit_message
    except Exception as e:
        return str(e), None, None

@app.get("/git-info")
def git_info():
    commit_hash, commit_date, commit_message = get_git_commit_info()
    return {"commit_hash": commit_hash, "commit_date": commit_date, "commit_message": commit_message}