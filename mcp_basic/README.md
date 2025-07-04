### Overview

This is a toy example to show the basic implementation of MCP.

It impletments two mcp servers. 
1. Calculator --> use the transport 'stdio' and runs the server locally. it has four tools
2. Tavily_search --> use the transport 'streamable-http' and runs the server at local host and port 8000. it has one tool that uses tavily search api

It implements an application that uses these MCP servers to respond to the queries.


### How to run
1. Give you OPENAI_API_KEY and TAVILY_API_KEY in .env
2. Start the tavily search mcp server explicity --> this is needed as the transport used is 'streamable-http'
3. Run client.py. It will automatically start the local mcp server
