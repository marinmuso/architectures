
from architectures.providers import _Azure


class _Integration(_Azure):
    _service_type = "integration"
    _icon_dir = "icons/azure/integration"


class APIForFhir(_Integration):
    _icon = "api-for-fhir.png"


class APIManagement(_Integration):
    _icon = "api-management.png"


class AppConfiguration(_Integration):
    _icon = "app-configuration.png"


class DataCatalog(_Integration):
    _icon = "data-catalog.png"


class DataFactory(_Integration):
    _icon = "data-factory.png"


class EventGridDomains(_Integration):
    _icon = "event-grid-domains.png"


class EventGridSubscriptions(_Integration):
    _icon = "event-grid-subscriptions.png"


class EventGridTopics(_Integration):
    _icon = "event-grid-topics.png"


class IntegrationAccounts(_Integration):
    _icon = "integration-accounts.png"


class IntegrationServiceEnvironments(_Integration):
    _icon = "integration-service-environments.png"


class LogicAppsCustomConnector(_Integration):
    _icon = "logic-apps-custom-connector.png"


class LogicApps(_Integration):
    _icon = "logic-apps.png"


class SendgridAccounts(_Integration):
    _icon = "sendgrid-accounts.png"


class ServiceBusRelays(_Integration):
    _icon = "service-bus-relays.png"


class ServiceBus(_Integration):
    _icon = "service-bus.png"


class ServiceCatalogManagedApplicationDefinitions(_Integration):
    _icon = "service-catalog-managed-application-definitions.png"


class SoftwareAsAService(_Integration):
    _icon = "software-as-a-service.png"


class StorsimpleDeviceManagers(_Integration):
    _icon = "storsimple-device-managers.png"


# Aliases
