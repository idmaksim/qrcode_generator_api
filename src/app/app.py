from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.routers import main_api_router


app = FastAPI(include_in_schema=True)
app.include_router(main_api_router)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def redirect_to_docs():
    return '/docs'

