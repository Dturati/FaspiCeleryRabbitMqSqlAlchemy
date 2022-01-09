class PeopleService:
    def __init__(self) -> None:
        super().__init__()

    async def save(self, data: dict) -> dict:
        data['name'] = f"{data['name']} saved"
        return data