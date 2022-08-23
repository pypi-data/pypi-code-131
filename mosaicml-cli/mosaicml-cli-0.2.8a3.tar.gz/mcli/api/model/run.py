""" GraphQL representation of MCLIJob"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Tuple

from mcli.api.engine.utils import dedent_indent
from mcli.api.exceptions import MAPIException
from mcli.api.schema.generic_model import DeserializableModel, convert_datetime
from mcli.models.run_config import FinalRunConfig
from mcli.utils.utils_run_status import RunStatus


@dataclass
class Run(DeserializableModel):
    """The GraphQL Serializable and Deserializable representation of a Run
    """

    run_uid: str
    name: str
    status: RunStatus
    created_at: datetime
    updated_at: datetime
    config: FinalRunConfig
    job_config: dict

    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    _required_properties: Tuple[str] = tuple(
        ['runUid', 'runName', 'runStatus', 'createdAt', 'updatedAt', 'runInput', 'jobConfig'])

    @classmethod
    def from_mapi_response(cls, response: Dict[str, Any]) -> Run:
        missing = set(cls._required_properties) - set(response)
        if missing:
            raise MAPIException(
                status=HTTPStatus.BAD_REQUEST,
                message=f'Missing required key(s) in response to deserialize Run object: {", ".join(missing)}',
            )

        return cls(run_uid=response['runUid'],
                   name=response['runName'],
                   created_at=convert_datetime(response['createdAt']),
                   updated_at=convert_datetime(response['updatedAt']),
                   status=RunStatus[response['runStatus']],
                   config=FinalRunConfig.from_mapi_response(response['runInput']),
                   job_config=response['jobConfig'])


def get_run_schema(indentation: int = 2):
    """ Get the GraphQL schema for a :type RunModel:
    Args:
        indentation (int): Optional[int] for the indentation of the block
    Returns:
        Returns a GraphQL string with all the fields needed to initialize a
        :type RunModel:
    """
    return dedent_indent("""
runUid
runName
runInput
runStatus
createdAt
updatedAt
jobConfig
        """, indentation)
