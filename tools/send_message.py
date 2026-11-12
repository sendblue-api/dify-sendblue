from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from sendblue_client import SendblueClient

class SendMessageTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        client = SendblueClient(self.runtime.credentials.get("api_key", ""), self.runtime.credentials.get("api_secret", ""))
        result = client.send_message(number=tool_parameters.get("number", ""), content=tool_parameters.get("content", ""), from_number=tool_parameters.get("from_number", ""))
        yield self.create_json_message(result if isinstance(result, dict) else {"data": result})
