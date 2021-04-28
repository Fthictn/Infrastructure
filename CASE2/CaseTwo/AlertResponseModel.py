from typing import List


class EmailServer(object):
    user: str
    email_server_pass: str
    host: str
    port: int
    encrypt: bool

    def __init__(self, user: str, email_server_pass: str, host: str, port: int, encrypt: bool) -> None:
        self.user = user
        self.email_server_pass = email_server_pass
        self.host = host
        self.port = port
        self.encrypt = encrypt


class AlertModel(object):
    recipients: List[str]
    sender: str
    enabled: bool
    email_server: EmailServer
    alerts: List[str]

    def __init(self, recipients: List[str], sender: str, enabled: bool, email_server: EmailServer, alerts: List[str]) -> None:
        self.recipients = recipients
        self.sender = sender
        self.enabled = enabled
        self.email_server = email_server
        self.alerts = alerts
