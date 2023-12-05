from fastapi import FastAPI, HTTPException
from starlette import status
from sample_task_management import router as sample_task_management_router
from database import check_db_connected


app = FastAPI()
app.include_router(sample_task_management_router.router)


@app.on_event("startup")
async def app_startup():
    db = await check_db_connected()
    if db is not None:
        db.close()
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="can not connect to database")
