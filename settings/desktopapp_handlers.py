from pydantic import Field, validator

from openpype.settings import BaseSettingsModel, ensure_unique_names

from .common import DictWithStrList


class ApplicationLaunchStatuses(BaseSettingsModel):
    """Application launch statuses

    Change task's status to left side if current task status is in list on right side
    """
    enabled: bool = True
    ignored_statuses: list[str] = Field(
        default_factory=list,
        title="Do not change status if current status is",
    )
    status_change: list[DictWithStrList] = Field(
        title="Status change",
        default_factory=list,
    )

    @validator("status_change")
    def ensure_unique_names(cls, value):
        """Ensure name fields within the lists have unique names."""

        ensure_unique_names(value)
        return value


class FtrackDesktopAppHandlers(BaseSettingsModel):
    """Settings for event handlers running in ftrack service."""

    application_launch_statuses: ApplicationLaunchStatuses = Field(
        title="Application - Status change on launch",
        default_factory=ApplicationLaunchStatuses,
    )


DEFAULT_DESKTOP_HANDLERS_SETTINGS = {
    "application_launch_statuses": {},
}