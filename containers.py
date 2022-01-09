import logging.config

from dependency_injector import containers, providers
from services.people import PeopleService
from repository.people import PeopleRepository

class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(modules=["endpoints"])
  config = providers.Configuration(yaml_files=["config.yml"])
  
  logging = providers.Resource(
      logging.config.fileConfig,
      fname="logging.ini",
  )

  people_repository = providers.Factory(
      PeopleRepository
  )

  people_service = providers.Factory(
    PeopleService,
    people_repository=people_repository
  )


