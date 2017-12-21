from typing import Text

from zerver.lib.test_classes import WebhookTestCase

class FrontHookTests(WebhookTestCase):
    STREAM_NAME = 'test'
    URL_TEMPLATE = u"/api/v1/external/front?api_key={api_key}"

    def test_front_archive(self) -> None:
        expected_subject = u"Front"
        expected_message = u"A [conversation](https://app.frontapp.com/open/cnv_a73yqx) is archived by www_rrawat555"
        self.send_and_test_stream_message('archive', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_assign(self) -> None:
        expected_subject = u"Front"
        expected_message = u"A [conversation](https://app.frontapp.com/open/cnv_a73yu9) is assigned to www_rrawat555 by www_rrawat555"
        self.send_and_test_stream_message('assign', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_comment(self) -> None:
        expected_subject = u"Front"
        expected_message = u"www_rrawat555 added a comment to a [conversation](https://app.frontapp.com/open/cnv_a73yq9) :\n> Hmmm...i know these automated replies...:sweat_smile:"

        self.send_and_test_stream_message('comment', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_mention(self) -> None:
        expected_subject = u"Front"
        expected_message = u"www_rrawat555 mentioned www_rrawat555 in a comment :\n> @www_rrawat555 Hii...This is a comment and i'm testing mention part of front application"
        self.send_and_test_stream_message('mention', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_outreply(self) -> None:
        expected_subject = u"Front"
        expected_message = u"www_rrawat555 replied to a [conversation](https://app.frontapp.com/open/cnv_a73yq9) :\n> hiii...."
        self.send_and_test_stream_message('outreply', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_reopen(self) -> None:
        expected_subject = u"Front"
        expected_message = u"www_rrawat555 reopened a [conversation](https://app.frontapp.com/open/cnv_a73yq9)"
        self.send_and_test_stream_message('reopen', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_tag(self) -> None:
        expected_subject = u"Front"
        expected_message = u"Tag Urgent was added by www_rrawat555 to a [conversation](https://app.frontapp.com/open/cnv_a73yu9)"
        self.send_and_test_stream_message('tag', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_untag(self) -> None:
        expected_subject = u"Front"
        expected_message = u"Tag Urgent was removed by www_rrawat555 from a [conversation](https://app.frontapp.com/open/cnv_a73yu9)"
        self.send_and_test_stream_message('untag', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def test_front_unassign(self) -> None:
        expected_subject = u"Front"
        expected_message = u"A [conversation](https://app.frontapp.com/open/cnv_a73yu9) is unassigned by www_rrawat555"
        self.send_and_test_stream_message('unassign', expected_subject, expected_message, content_type="application/x-www-form-urlencoded")

    def get_body(self, fixture_name: Text) -> Text:
        return self.fixture_data("front", fixture_name, file_type="json")
