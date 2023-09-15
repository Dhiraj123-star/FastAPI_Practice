from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =FastAPI()

@app.get("/hello/")
async def hello():
        ret = '''
    <html>
    <body> 

    <h2> Hello FastAPI </h2>

    </body>
    </html>

    '''

        return HTMLResponse(ret)