from examples.shared.apps.items import app # The FastAPI app
from examples.shared.setup import setup_logging

from fastapi_mcp import FastApiMCP
from fastapi_mcp.external import n8n

setup_logging()

# 注册n8n router
app.include_router(n8n.router)

# 只暴露n8n相关API为MCP工具
mcp = FastApiMCP(app, include_tags=["n8n"])
mcp.mount()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
