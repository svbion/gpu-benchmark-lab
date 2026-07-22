# Publication Configuration

This repository keeps public-facing links and owner/repository values configurable in [_config.yml](../_config.yml).

## Variables

| Variable | Purpose |
| :--- | :--- |
| `repository_owner` | GitHub owner used in badges, release docs, and Pages references |
| `repository_name` | Repository name |
| `repository_slug` | `owner/repository` shorthand |
| `repository_url` | Public GitHub repository URL |
| `pages_url` | GitHub Pages URL |
| `license_name` | Public license label |
| `release_version` | Current public launch release |
| `profile.*` | Public biography/contact labels and URLs |

## Update Rule

Before publishing under a different account, update `_config.yml` first and then regenerate docs or Pages artifacts that depend on those values.

## Placeholder Policy

Docs should not contain raw placeholder links or phrases such as `Add URL here`. If a public link is not ready, refer to the relevant `_config.yml` variable by name.
