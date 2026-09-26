from fastmcp import FastMCP
import requests

mcp = FastMCP("Doors ERP")

@mcp.tool
def get_measurements():
    """Get all measurements"""
    
    r = requests.get(
        "https://YOUR-RAILWAY-DOMAIN/measurements"
    )

    return r.json()

if __name__ == "__main__":
    mcp.run()
