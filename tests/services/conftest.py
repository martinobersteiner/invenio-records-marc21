# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-Records-Marc21 is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""
from collections import namedtuple

import pytest
from flask_principal import Identity
from invenio_access import any_user
from invenio_app.factory import create_api

from invenio_records_marc21.proxies import current_records_marc21
from invenio_records_marc21.services import (
    Marc21RecordService,
    Marc21RecordServiceConfig,
)
from invenio_records_marc21.services.record import Marc21Metadata


@pytest.fixture(scope="module")
def create_app(instance_path):
    """Application factory fixture."""
    return create_api


RunningApp = namedtuple("RunningApp", ["app", "service", "identity_simple"])


@pytest.fixture(scope="module")
def running_app(app, service, identity_simple):
    """This fixture provides an app with the typically needed db data loaded.

    All of these fixtures are often needed together, so collecting them
    under a semantic umbrella makes sense.
    """
    return RunningApp(app, service, identity_simple)


@pytest.fixture(scope="module")
def identity_simple():
    """Simple identity fixture."""
    i = Identity(1)
    i.provides.add(any_user)
    return i


@pytest.fixture(scope="module")
def service(appctx):
    """Service instance."""
    return Marc21RecordService(config=Marc21RecordServiceConfig())


@pytest.fixture(scope="session")
def metadata():
    """Input data (as coming from the view layer)."""
    metadata = Marc21Metadata()
    metadata.xml = "<record><datafield tag='245' ind1='1' ind2='0'><subfield code=' '>laborum sunt ut nulla</subfield></datafield></record>"
    return metadata


@pytest.fixture(scope="session")
def metadata2():
    """Input data (as coming from the view layer)."""
    metadata = Marc21Metadata()
    metadata.xml = "<record><datafield tag='245' ind1='1' ind2='0'><subfield code=' '>nulla sunt laborum</subfield></datafield></record>"
    return metadata


@pytest.fixture()
def embargoedrecord(embargoed_record):
    """Embargoed record."""
    service = current_records_marc21.records_service

    draft = service.create(identity_simple, embargoed_record)
    record = service.publish(id_=draft.id, identity=identity_simple)
    return record


@pytest.fixture()
def full_metadata():
    """Metadata full record marc21 xml."""
    metadata = Marc21Metadata()
    metadata.xml = "<record><leader>00000nam a2200000zca4500</leader><datafield tag='035' ind1=' ' ind2=' '><subfield code='a'>AC08088803</subfield></datafield></record>"
    return metadata


@pytest.fixture()
def min_metadata():
    """Metadata empty record marc21 xml."""
    metadata = Marc21Metadata()
    metadata.xml = "<record></record>"
    return metadata
