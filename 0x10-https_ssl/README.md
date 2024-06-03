# 0x10-https_ssl

## Description

This project contains two tasks related to setting up and managing HTTPS and SSL termination with HAProxy.

## Task 0: World Wide Web

### Objective

Configure your domain to point to specific subdomains and create a Bash script that retrieves DNS information for these subdomains.

### Requirements

1. Add the subdomains `www`, `lb-01`, `web-01`, and `web-02` to your domain, pointing them to their respective IPs.
2. Create a Bash script named `0-world_wide_web` that:
   - Accepts two arguments: `domain` (mandatory) and `subdomain` (optional).
   - Displays DNS information using `dig`.
   - Uses `awk` to parse and display the output.
   - Contains at least one Bash function.
   - Ignores `shellcheck` case `SC2086`.

### Usage

```bash
./0-world_wide_web domain_name [subdomain]
