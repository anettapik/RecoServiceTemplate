from pydantic_settings import BaseSettings, SettingsConfigDict

TOKEN: str = "123"


class Config(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)


class LogConfig(Config):
    model_config = SettingsConfigDict(case_sensitive=False)
    level: str = "INFO"
    datetime_format: str = "%Y-%m-%d %H:%M:%S"


class ServiceConfig(Config):
    service_name: str = "reco_service"
    k_recs: int = 10

    log_config: LogConfig
    token: str = TOKEN


def get_config() -> ServiceConfig:
    return ServiceConfig(
        log_config=LogConfig(),
    )
