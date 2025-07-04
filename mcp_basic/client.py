from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

from dotenv import load_dotenv
import asyncio

load_dotenv()

async def run_agent():
    # Load remote and local MCP servers
    client = MultiServerMCPClient({
        "calculator": {
            "command": "python",
            "args": ["/servers/calculator_server.py"],      # you may have to give absolute path
            "transport": "stdio",
        },
        "tavily": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    })

    # Load tools from all servers
    tools = await client.get_tools()

    # Build the model and bind to the tools
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    llm_with_tools = llm.bind_tools(tools)

    # Node function
    def call_model(state: MessagesState):
        return {"messages":llm_with_tools.invoke(state["messages"])}

    # Build the graph
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", tools_condition)
    builder.add_edge("tools", "call_model")

    # Compile the graph
    agent = builder.compile()

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the difference between GDPs of India and USA"}]}
    )

    for m in response['messages']:
        m.pretty_print()

asyncio.run(run_agent())
        