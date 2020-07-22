# Pipeline Linter Buildkite Plugin

An [Buildkite plugin](https://buildkite.com/docs/agent/v3/plugins) to validate all pipelines in a repository.

## Example

```yml
steps:
  - label: ':buildkite: lint pipelines'
    plugins:
      - xiaket/pipeline-linter:
          pipelines:
            - .buildkite/*.yml
```

This tool is also available as a docker image, you can run it as:

```
docker run -v /path/to/your/repo/.buildkite/:/pipelines/ \
  xiaket/buildkite-pipeline-linter \
  /pipelines/pipeline.yml
```

## License

MIT (see [LICENSE](LICENSE))
