from typing import Any
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from sendblue_client import SendblueClient

class SendblueProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            SendblueClient(credentials.get("api_key", ""), credentials.get("api_secret", "")).list_lines()
        except Exception:
            raise ToolProviderCredentialValidationError("Cannot authenticate with Sendblue. Check your API key and API secret.") from None
