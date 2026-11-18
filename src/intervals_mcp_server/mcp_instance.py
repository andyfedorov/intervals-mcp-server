"""
Shared MCP instance module.

This module provides a shared FastMCP instance that can be imported by both
the server module and tool modules without creating cyclic imports.
"""

from mcp.server.fastmcp import FastMCP  # pylint: disable=import-error
from mcp.server.transport_security import TransportSecuritySettings

from intervals_mcp_server.api.client import setup_api_client


mcp: FastMCP = FastMCP(
    "intervals-icu",
    lifespan=setup_api_client,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "intervals-backend.onrender.com",
            "intervals-backend.onrender.com:*",
            "localhost:*",
            "127.0.0.1:*",
        ],
        allowed_origins=[
            "https://intervals-backend.onrender.com",
            "https://intervals-backend.onrender.com:*",
            "http://localhost:*",
            "http://127.0.0.1:*",
        ],
    ),
)  # pylint: disable=invalid-name
