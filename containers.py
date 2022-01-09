import logging.config

from dependency_injector import containers, providers
from services.people_service import PeopleService
from repository.people import PeopleRepository
from database import SessionLocal, engine
from models import People

from fastapi import Depends


class Container(containers.DeclarativeContainer):
    # Dependency
    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    People.Base.metadata.create_all(bind=engine)

    wiring_config = containers.WiringConfiguration(modules=["endpoints"])
    config = providers.Configuration(yaml_files=["config.yml"])

    logging = providers.Resource(
       logging.config.fileConfig,
       fname="logging.ini",
    )

    people_repository = providers.Factory(
      PeopleRepository
    )

    db = providers.Factory(
        SessionLocal
    )

    people_service = providers.Factory(
      PeopleService,
      people_repository=people_repository,
      db=db,
    )


