import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="therapy_bot",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    frontend_packages=[
        "react-loading-icons",
    ],
)
