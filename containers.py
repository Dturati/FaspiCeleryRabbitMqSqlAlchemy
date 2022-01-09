import logging.config

from dependency_injector import containers, providers
from services.people import PeopleService

class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(modules=["endpoints"])
  config = providers.Configuration(yaml_files=["config.yml"])
  
  logging = providers.Resource(
      logging.config.fileConfig,
      fname="logging.ini",
  )

  people_service = providers.Factory(
    PeopleService
  )
