#!/usr/bin/python3
"""
    Validates visibility of my web server in Datadog.
    Get all hosts for your organization returns "OK" response
    Run in bash:
     DD_SITE="us5.datadoghq.com" DD_API_KEY="xxx" DD_APP_KEY="xxx" python3 validate_server.py
"""
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi


configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        include_hosts_metadata=True,
        # filter="env:ci",
    )

    print(response)
