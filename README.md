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

## License

MIT (see [LICENSE](LICENSE))
