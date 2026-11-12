# Sendblue for Dify

Official Sendblue tool plugin. Send one-to-one text messages, read message history, check delivery, and list sending lines.

## Requirements

Requires a Sendblue account, an active API key and secret, and outbound HTTPS access to api.sendblue.co. Supported in Dify 1.9 or later.

## Setup

Install the `.difypkg` release in Dify and configure the Sendblue API key and API secret from [your dashboard](https://app.sendblue.com/). Credentials are validated using a read-only line-state request. API calls go only to `https://api.sendblue.co`.

Free shared-line plans require a verified recipient and an explicit `from_number`. Confirm the recipient and exact content before calling `send_message`; use a human approval step when an LLM chooses writes. Sends are asynchronous. Save the returned handle and query `get_message_status`. A timeout may follow a successful send, so check history before retrying. `list_messages` returns a bounded page with optional phone filter and offset.

## Development

Python 3.12. `uv venv && uv pip install -r requirements.txt pytest` then `uv run pytest`. Tests use mock HTTP responses and never send messages. Package using the official Dify CLI: `dify plugin package .`.

[API docs](https://docs.sendblue.com/) · [Privacy](PRIVACY.md) · support@sendblue.com

Source repository: https://github.com/sendblue-api/dify-sendblue
