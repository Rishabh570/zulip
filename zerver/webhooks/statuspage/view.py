from django.utils.translation import ugettext as _
from zerver.lib.actions import check_send_stream_message
from zerver.lib.response import json_success
from zerver.decorator import REQ, has_request_variables, api_key_only_webhook_view
from zerver.models import get_client, UserProfile
from django.http import HttpRequest, HttpResponse
from typing import Dict, Any, Iterable, Optional, Text


@api_key_only_webhook_view('Statuspage')
@has_request_variables
def api_statuspage_webhook(request, UserProfile,
                           payload=REQ(argument_type='body'),
                           stream=REQ(default='statuspage-test'),
                           topic=REQ(default='Statuspage')):

    # type: (HttpRequest, UserProfile, Dict[str, Any], str, str) -> HttpResponse

    status = payload["page"]["status_description"]

    if status == "All Systems Operational":
        name = payload["incident"]["name"]
        state = payload["incident"]["status"]
        content = payload["incident"]["incident_updates"][0]["body"]
        body = u"Incident Report :\n **{}** \n * State: **{}** \n * Description: {}"
        body = body.format(name, state, content)

    if status != "All Systems Operational":
        name = payload["component"]["name"]
        old_status = payload["component_update"]["old_status"]
        new_status = payload["component_update"]["new_status"]
        body = u"Component status changed :\n **{}** has changed status from **{}** to **{}**"
        body = body.format(name, old_status, new_status)

    check_send_stream_message(UserProfile, request.client, stream, topic, body)
    return json_success()
