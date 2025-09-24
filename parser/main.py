from parser.constants import CLIENT_INFO
from parser.decorators import time_of_script
from parser.utils import initialize_components, run


@time_of_script
def main():
    """Основная логика скрипта."""
    for client_name, info in CLIENT_INFO.items():
        client_logins, client_m_id, client_am_id = info
        appmetrica, direct, metrica = initialize_components(
            client_logins,
            client_m_id,
            client_am_id
        )
        run(direct, metrica, appmetrica, client_name)


if __name__ == "__main__":
    main()
