# Copyright (c) 2016 Hewlett-Packard Enterprise Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from tempest.lib.services.volume.v3.backups_client import BackupsClient
from tempest.lib.services.volume.v3.base_client import BaseClient
from tempest.lib.services.volume.v3.group_snapshots_client import \
    GroupSnapshotsClient
from tempest.lib.services.volume.v3.group_types_client import GroupTypesClient
from tempest.lib.services.volume.v3.groups_client import GroupsClient
from tempest.lib.services.volume.v3.messages_client import MessagesClient
from tempest.lib.services.volume.v3.snapshots_client import SnapshotsClient
from tempest.lib.services.volume.v3.versions_client import VersionsClient
from tempest.lib.services.volume.v3.volumes_client import VolumesClient

__all__ = ['BackupsClient', 'BaseClient', 'GroupsClient',
           'GroupSnapshotsClient', 'GroupTypesClient',
           'MessagesClient', 'SnapshotsClient', 'VersionsClient',
           'VolumesClient']