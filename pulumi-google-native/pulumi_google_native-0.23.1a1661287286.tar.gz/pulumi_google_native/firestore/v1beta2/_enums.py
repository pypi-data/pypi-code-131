# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'GoogleFirestoreAdminV1beta2IndexFieldArrayConfig',
    'GoogleFirestoreAdminV1beta2IndexFieldOrder',
    'IndexQueryScope',
]


class GoogleFirestoreAdminV1beta2IndexFieldArrayConfig(str, Enum):
    """
    Indicates that this field supports operations on `array_value`s.
    """
    ARRAY_CONFIG_UNSPECIFIED = "ARRAY_CONFIG_UNSPECIFIED"
    """
    The index does not support additional array queries.
    """
    CONTAINS = "CONTAINS"
    """
    The index supports array containment queries.
    """


class GoogleFirestoreAdminV1beta2IndexFieldOrder(str, Enum):
    """
    Indicates that this field supports ordering by the specified order or comparing using =, <, <=, >, >=.
    """
    ORDER_UNSPECIFIED = "ORDER_UNSPECIFIED"
    """
    The ordering is unspecified. Not a valid option.
    """
    ASCENDING = "ASCENDING"
    """
    The field is ordered by ascending field value.
    """
    DESCENDING = "DESCENDING"
    """
    The field is ordered by descending field value.
    """


class IndexQueryScope(str, Enum):
    """
    Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection id. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection id as this index.
    """
    QUERY_SCOPE_UNSPECIFIED = "QUERY_SCOPE_UNSPECIFIED"
    """
    The query scope is unspecified. Not a valid option.
    """
    COLLECTION = "COLLECTION"
    """
    Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the collection id specified by the index.
    """
    COLLECTION_GROUP = "COLLECTION_GROUP"
    """
    Indexes with a collection group query scope specified allow queries against all collections that has the collection id specified by the index.
    """
