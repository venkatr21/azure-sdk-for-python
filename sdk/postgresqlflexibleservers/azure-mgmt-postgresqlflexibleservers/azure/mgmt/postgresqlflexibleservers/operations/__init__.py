# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._administrators_operations import AdministratorsOperations
from ._backups_operations import BackupsOperations
from ._location_based_capabilities_operations import LocationBasedCapabilitiesOperations
from ._server_capabilities_operations import ServerCapabilitiesOperations
from ._check_name_availability_operations import CheckNameAvailabilityOperations
from ._check_name_availability_with_location_operations import CheckNameAvailabilityWithLocationOperations
from ._configurations_operations import ConfigurationsOperations
from ._databases_operations import DatabasesOperations
from ._firewall_rules_operations import FirewallRulesOperations
from ._servers_operations import ServersOperations
from ._flexible_server_operations import FlexibleServerOperations
from ._ltr_backup_operations_operations import LtrBackupOperationsOperations
from ._migrations_operations import MigrationsOperations
from ._postgre_sql_management_client_operations import PostgreSQLManagementClientOperationsMixin
from ._operations import Operations
from ._get_private_dns_zone_suffix_operations import GetPrivateDnsZoneSuffixOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_endpoint_connection_operations import PrivateEndpointConnectionOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._quota_usages_operations import QuotaUsagesOperations
from ._replicas_operations import ReplicasOperations
from ._log_files_operations import LogFilesOperations
from ._server_threat_protection_settings_operations import ServerThreatProtectionSettingsOperations
from ._tuning_options_operations import TuningOptionsOperations
from ._virtual_endpoints_operations import VirtualEndpointsOperations
from ._virtual_network_subnet_usage_operations import VirtualNetworkSubnetUsageOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdministratorsOperations",
    "BackupsOperations",
    "LocationBasedCapabilitiesOperations",
    "ServerCapabilitiesOperations",
    "CheckNameAvailabilityOperations",
    "CheckNameAvailabilityWithLocationOperations",
    "ConfigurationsOperations",
    "DatabasesOperations",
    "FirewallRulesOperations",
    "ServersOperations",
    "FlexibleServerOperations",
    "LtrBackupOperationsOperations",
    "MigrationsOperations",
    "PostgreSQLManagementClientOperationsMixin",
    "Operations",
    "GetPrivateDnsZoneSuffixOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateEndpointConnectionOperations",
    "PrivateLinkResourcesOperations",
    "QuotaUsagesOperations",
    "ReplicasOperations",
    "LogFilesOperations",
    "ServerThreatProtectionSettingsOperations",
    "TuningOptionsOperations",
    "VirtualEndpointsOperations",
    "VirtualNetworkSubnetUsageOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
