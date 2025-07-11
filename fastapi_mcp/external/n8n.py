from fastapi import APIRouter, Query
import httpx

router = APIRouter(prefix="/n8n", tags=["n8n"])

N8N_BASE_URL = "http://192.168.20.26:8220"  # n8n-workflows文档系统的地址

@router.get("/workflows")
async def search_workflows(q: str = None, trigger: str = None, complexity: str = None):
    params = {}
    if q: params["q"] = q
    if trigger: params["trigger"] = trigger
    if complexity: params["complexity"] = complexity
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{N8N_BASE_URL}/api/workflows", params=params)
        return resp.json()

@router.get("/workflows/category/{category}")
async def workflows_by_category(category: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{N8N_BASE_URL}/api/workflows/category/{category}")
        return resp.json()

@router.get("/stats")
async def get_stats():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{N8N_BASE_URL}/api/stats")
        return resp.json()

@router.get("/categories")
async def get_categories():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{N8N_BASE_URL}/api/categories")
        return resp.json() 