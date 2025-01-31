..
    Copyright (C) 2021 Graz University of Technology.

    Invenio-Records-Marc21 is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

Changes
=======

Version v0.17.3 (release 2024-01-11)

- fix: indexer needs queue name


Version v0.17.2 (release 2024-01-07)

- setup: add support for python3.10 and 3.11
- fix: controlfield not correct build for marcxml
- fix: ind1 could be undefined
- ui: move react-records-marc21 code here
- fix: rebuild-index not working
- fix: missing special for AVE
- bugfix: add schema to record


Version v0.17.1 (release 2023-12-01)

- alembic: add missing deletion_status


Version v0.17.0 (release 2023-11-09)

- ui: change dependency to invenio_rdm_records
- bugfix: files links list
- bugfix: add missing permissions
- CI: disable python 3.10
- tests: remove sqlalchemy NoResultFound
- tests: modification to testset and codestyle
- modification: permission policy records and files
- modification: create marc21 v2 schema and mappings
- global: change path to publications
- tests: add parameters to run-tests
- ui: redesign edit button
- records: add deletion_status
- services: make components customizable
- cli: change parameters
- resources: add dublin core serializer
- build:  limit draft resource version
- testset: modification files in record
- modification: import structure
- modification: unit of work
- modification: parent schema
- tests: fix test
- modification: records service config
- modifcation: use invenio-i18n translations module
- modification: create demo records
- modification: serializer structure
- build: bump version
- modification: marc21 v1 mapping
- modification: result item on dashboard
- modification: search mapping
- modification: user dashboard translations
- modification: translations in config module
- modification: empty search result
- translations: resource type translations
- modification: resource type translate
- modification: code style
- modification: gitignore
- translations: i18next update
- modification: result item translations
- modification: dashboard layout
- modification: user dashboard search
- fix: subfield may not exist
- landing-page: add additional titles
- translations: update
- modification: user dashboard search application
- modification: search components
- modification: configuration search application
- modification: api search options
- modification: clean code


Version v0.16.1 (release 2023-09-14)

- fix: doi modal


Version v0.16.0 (release 2023-09-14)

- landing_page: conditional wrap show doi
- modification: translations
- translation: update
- refactoring: variable naming
- landing_page: increase space above title
- landing-page: change created at to published
- landing_page: use improved export
- bugfix: import landing page


Version v0.15.0 (release 2023-09-12)

- fix: create_record dangling draft
- modification: gitignore
- modification: translations update
- modification: templates structured
- modification: add comments
- modifications: marc21 service permissions


Version v0.14.2 (release 2023-06-16)

- fix: namespace handling was wrong


Version v0.14.1 (release 2023-06-07)

- fix: remove whitespace and close div tag


Version v0.14.0 (release 2023-06-07)

- modification: alembic scripts
- modification: remove prefix in configuration variables


Version v0.13.2 (release 2023-06-05)

- bugfix: draft get file content


Version v0.13.1 (release 2023-06-01)

- bugfix: load default roles needed


Version v0.13.0 (release 2023-05-25)

- setup: remove compatibility check with python3.8
- metadata: add methods to get fields and values


Version v0.12.7 (release 2023-05-12)

- metadata: subfs, character before numbers


Version v0.12.6 (release 2023-05-11)

- pids: remove 2 subfields


Version v0.12.5 (release 2023-05-11)

- fix: metadata export needs a space


Version v0.12.4 (release 2023-05-10)

- doi: apply marc21 request changes
- tests: cleaned tests, remove unused statements
- metadata: add 856 field after doi creation
- modification: templates load from roles


Version v0.12.3 (release 2023-04-28)

- fix: distinguish between str and list


Version v0.12.2 (release 2023-04-25)

- bugfix: previewer allow to access files


Version v0.12.1 (release 2023-04-20)




Version v0.11.0 (release 2023-03-06)

- permissions: re-add SystemProcess to can_manage
- fix: to keep flask-babelex
- permissions: enlarge permission system
- modification: update marc21 record permissions
- modification: remove duplicate code
- modification: add pids to new version
- bugfix: create new version
- modification: dashboard records edit


Version v0.10.0 (release 2023-02-13)

- fix: category could be AVA
- modification: add fix me in the future
- modification: create dashboard entry for marc21


Version v0.9.2 (release 2023-02-09)

- fix: sort xml subfields generation
- fix: the value in subfs is a list
- fix: unify order of et.Element attributes


Version v0.9.1 (release 2023-01-23)

- fix: wrong alias for drafts and records
- modification: record status in deposit


Version v0.9.0 (release 2023-01-11)

- metadata: use id property instead
- fixes:
- global: pass through exports
- modification: add multiple files to record
- metadata: add param do_publish
- metadata: add exists method
- ui: update react-records-marc21
- services: add exception for common search
- services: add types
- codestyle: deposit form
- modification: deposit form style
- tests: testset update
- modification: put doi into the metadata
- modification: create identifier with draft
- bugfix: files enabled
- fix: correct CHANGES.rst


Version v0.8.4 (release 2022-11-17)

- fix:
- api: add duplicate check function
- fix
- metadata: implement convert_json_to_marc21xml
- metadata: add default values to selector
- api: add two functions moved from invenio-alma
- improve: add subfs parameter to emplace_datafield
- modification: add access_status field
- modification: use jast jsonschema
- codestyle: variable on top of the function definition.
- modification: service file config
- modification: api register services
- modification: create draft with errors
- modification: deposit structure
- modification: deposit application


Version v0.8.3 (release 2022-11-02)

- fix
- metadata: implement convert_json_to_marc21xml
- metadata: add default values to selector
- api: add two functions moved from invenio-alma
- improve: add subfs parameter to emplace_datafield
- fix: remove import of semantic css


Version v0.8.2 (release 2022-10-14)

- fix: pypi-publish inherit secrets


Version v0.8.1 (release 2022-10-14)

- global: migrate publish to reusable workflows
- setup: fix classifier


Version v0.8.0 (release 2022-10-14)

- tests: move to resuable workflows
- tests: remove CACHE and MQ
- setup: sort imports, remove doublets
- global: migrate to opensearch2


Version v0.7.5 (release 2022-09-27)

- fix: javascript dependencies


Version v0.7.4 (release 2022-09-27)

- fix: ConfigurationMixin changed location
- global: increase version of invenio-search


Version v0.7.3 (release 2022-08-10)

- fix use 009[7:11] for publication year


Version v0.7.2 (release 2022-08-10)

- modification: datacite schema\n\n changing the field numbers
- tests: modification datacite testset
- bugfix: pids components from rdm records


Version v0.7.1 (release 2022-08-09)

- fix: the missing mappings causes an error with the empty search feature


Version v0.7.0 (release 2022-08-04)

- improve (WIP) landing page and search results


Version v0.6.0 (release 2022-08-01)

- make the jsonschema less restrictive


Version v0.5.2 (release 2022-07-29)

- use search react components provided by invenio-app-rdm
- update the search initial query state


Version v0.5.1 (release 2022-07-07)




Version 0.0.1 (released TBD)

- Initial public release.
