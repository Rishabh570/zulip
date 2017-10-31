from django.utils.translation import ugettext as _
from zerver.lib.actions import check_send_stream_message
from zerver.lib.response import json_success, json_error
from zerver.decorator import REQ, has_request_variables, api_key_only_webhook_view
from zerver.models import get_client, UserProfile
from django.http import HttpRequest, HttpResponse
from typing import Dict, Any, Iterable, Optional, Text


@api_key_only_webhook_view('Front')
@has_request_variables
def api_front_webhook(request, UserProfile,
                      payload=REQ(argument_type='body'),
                      stream=REQ(default='test'),
                      topic=REQ(default='Front')):

    # type: (HttpRequest, UserProfile, Dict[str, Any], str, str) -> HttpResponse

    catogery = payload["type"]
    message_id = payload["conversation"]["id"]
    state = payload["conversation"]["status"]
    conversation = "https://app.frontapp.com/open/{}"
    conversation_link = conversation.format(message_id)

    if catogery == "archive":
        Username = payload["source"]["data"]["username"]
        body = u"A [conversation]({}) is {} by {}"
        body = body.format(conversation_link, state, Username)

    if catogery == "assign":
        tn = payload["target"]["data"]["username"]
        Username = payload["source"]["data"]["username"]
        body = u"A [conversation]({}) is {} to {} by {}"
        body = body.format(conversation_link, state, tn, Username)

    if catogery == "unassign":
        Username = payload["source"]["data"]["username"]
        body = u"A [conversation]({}) is {} by {}"
        body = body.format(conversation_link, state, Username)

    if catogery == "tag":
        tt = payload["target"]["data"]["name"]
        Username = payload["source"]["data"]["username"]
        body = u"Tag {} was added by {} to a [conversation]({})"
        body = body.format(tt, Username, conversation_link)

    if catogery == "untag":
        tt = payload["target"]["data"]["name"]
        Username = payload["source"]["data"]["username"]
        body = u"Tag {} was removed by {} from a [conversation]({})"
        body = body.format(tt, Username, conversation_link)

    if catogery == "comment":
        Username = payload["source"]["data"]["username"]
        tm = payload["target"]["data"]["body"]
        body = u"{} added a comment to a [conversation]({}) :\n> {}"
        body = body.format(Username, conversation_link, tm)

    if catogery == "out_reply":
        fn = payload["conversation"]["last_message"]["author"]["username"]
        reply_message = payload["conversation"]["last_message"]["blurb"]
        body = u"{} replied to a [conversation]({}) :\n> {}"
        body = body.format(fn, conversation_link, reply_message)

    if catogery == "reopen":
        Username = payload["source"]["data"]["username"]
        body = u"{} reopened a [conversation]({})"
        body = body.format(Username, conversation_link)

    if catogery == "mention":
        Username = payload["source"]["data"]["username"]
        tp = payload["target"]["_meta"]["type"]
        tn = payload["target"]["data"]["author"]["username"]
        tm = payload["target"]["data"]["body"]
        body = u"{} mentioned {} in a {} :\n> {}"
        body = body.format(Username, tn, tp, tm)

    check_send_stream_message(UserProfile, request.client, stream, topic, body)
    return json_success()
