from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from sendblue_client import SendblueClient

class ListMessagesTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        client = SendblueClient(self.runtime.credentials.get("api_key", ""), self.runtime.credentials.get("api_secret", ""))
        result = client.list_messages(limit=int(tool_parameters.get("limit") or 20), number=tool_parameters.get("number", ""), offset=int(tool_parameters.get("offset") or 0))
        yield self.create_json_message(result if isinstance(result, dict) else {"data": result})
