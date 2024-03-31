# Load Balancer Project

## Overview
This project aims to set up a load balancer using HAproxy and configure two web servers (web-01 and web-02) behind it. The web servers are configured with Nginx to include a custom HTTP response header for tracking purposes.

## Tasks
1. **Task 0: Double the number of webservers**
   - Configure Nginx on web-02 to include a custom HTTP response header.
   - Write a script (`0-custom_http_response_header`) to automate this configuration.

2. **Task 1: Install your load balancer**
   - Install and configure HAproxy on lb-01.
   - Distribute traffic to web-01 and web-02 using a round-robin algorithm.
   - Write a script (`1-install_load_balancer`) to automate this installation and configuration.

## Requirements
- All files should end with a new line.
- All Bash scripts must be executable.
- Bash scripts must pass Shellcheck (version 0.3.7) without any errors.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- A README.md file is mandatory.
- Hostnames for servers should be properly configured as `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.

## Usage
1. Clone this repository.
2. Navigate to the appropriate directory.
3. Run the provided Bash scripts to configure the servers accordingly.

## Author
Rasaq olamilekan
