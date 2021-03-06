# Copyright 2017 FiberHome Telecommunication Technologies CO.,LTD
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib.services.volume.v3 import volumes_client
from tempest.tests.lib import fake_auth_provider
from tempest.tests.lib.services import base


class TestVolumesClient(base.BaseServiceTest):

    FAKE_VOLUME_SUMMARY = {
        "volume-summary": {
            "total_size": 20,
            "total_count": 5
        }
    }

    def setUp(self):
        super(TestVolumesClient, self).setUp()
        fake_auth = fake_auth_provider.FakeAuthProvider()
        self.client = volumes_client.VolumesClient(fake_auth,
                                                   'volume',
                                                   'regionOne')

    def _test_show_volume_summary(self, bytes_body=False):
        self.check_service_client_function(
            self.client.show_volume_summary,
            'tempest.lib.common.rest_client.RestClient.get',
            self.FAKE_VOLUME_SUMMARY,
            bytes_body)

    def test_show_volume_summary_with_str_body(self):
        self._test_show_volume_summary()

    def test_show_volume_summary_with_bytes_body(self):
        self._test_show_volume_summary(bytes_body=True)
