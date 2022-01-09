from repository.people import PeopleRepository

class PeopleService:
    def __init__(self, people_repository: PeopleRepository) -> None:
        self._repository: PeopleRepository = people_repository

    async def save(self, data: dict) -> dict:
        data['name'] = f"{data['name']} saved"
        self._repository.save(data)
        return data