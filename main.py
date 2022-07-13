from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# using FastApi to upload pages
app = FastAPI()

# create the main function


@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <marquee width="525" behavior="alternate"><h1 style="color:red;font-family:Arial">Please Upload Your Scenes!</h1></marquee>
    """
    return content
