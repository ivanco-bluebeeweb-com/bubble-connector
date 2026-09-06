"""Extension declaration, capabilities, health check for Bubble Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "bubble-connector",
    version="0.1.0",
    display_name="Bubble",
    icon="icon.svg",
    capabilities=["bubble:manage"],
    description="Official Imperal connector for Bubble (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("bubble_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Bubble connection(s) configured." if count else "Not connected yet."
    }
