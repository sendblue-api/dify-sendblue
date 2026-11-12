from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from sendblue_client import SendblueClient

class GetMessageStatusTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        client = SendblueClient(self.runtime.credentials.get("api_key", ""), self.runtime.credentials.get("api_secret", ""))
        result = client.get_message_status(handle=tool_parameters.get("handle", ""))
        yield self.create_json_message(result if isinstance(result, dict) else {"data": result})
