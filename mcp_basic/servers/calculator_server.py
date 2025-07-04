from fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Returns the difference between a and b."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divides a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#  Ensure the MCP server only runs when the script is called directly
if __name__ == "__main__":
    mcp.run(transport="stdio")