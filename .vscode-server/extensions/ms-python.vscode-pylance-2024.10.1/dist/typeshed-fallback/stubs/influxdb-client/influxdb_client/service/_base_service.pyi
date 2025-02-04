from _typeshed import Incomplete

class _BaseService:
    api_client: Incomplete
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def build_type(self) -> str: ...
    async def build_type_async(self) -> str: ...
    def response_header(self, response, header_name: str = "X-Influxdb-Version") -> str: ...
