#!/usr/bin/env python3
import json
import sys
import urllib

import jsonschema
import yaml


def get_latest_schema():
    url = (
        "https://raw.githubusercontent.com"
        "/buildkite/pipeline-schema/master/schema.json"
    )
    response = urllib.request.urlopen(url)
    return json.loads(response.read().decode('utf-8'))


def main():
    schema = get_latest_schema()
    with open(sys.argv[1]) as fobj:
        pipeline = yaml.load(fobj, Loader=yaml.SafeLoader)

    jsonschema.validate(instance=pipeline, schema=schema)

if __name__ == '__main__':
    main()
