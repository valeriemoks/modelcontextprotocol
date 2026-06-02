from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

#the transport is the protocol used to communicate with the MCP server.
#stdio is the default transport for local development.
#http is the transport for remote development.
#the transport ="stdio" tells the server to:
#use standard input/output(stdin and stdout) to receive and respond to tool function calls


if __name__ == "__main__":
    mcp.run(transport="stdio")