
## Tasks

### Task 0: Double the Number of Web Servers

**Objective:** Configure `web-02` to be identical to `web-01` and add a custom Nginx response header to both servers.

#### Requirements:
- Configure Nginx to include a custom HTTP header `X-Served-By` with the server's hostname as the value.
- Use a Bash script to automate the configuration.

#### Instructions:
1. **Create and execute the configuration script:**
    - The script `0-custom_http_response_header` installs Nginx and configures the custom header.
    - Run the script on `web-02`.

    ```bash
    # Transfer and execute the script on web-02
    scp 0-custom_http_response_header ubuntu@100.25.37.11:/home/ubuntu/
    ssh ubuntu@100.25.37.11 'bash /home/ubuntu/0-custom_http_response_header'
    ```

### Task 1: Install Your Load Balancer

**Objective:** Install and configure HAProxy on `lb-01` to distribute traffic between `web-01` and `web-02` using a round-robin algorithm.

#### Requirements:
- Configure HAProxy to send traffic to `web-01` and `web-02`.
- Use a Bash script to automate the configuration.

#### Instructions:
1. **Create and execute the load balancer script:**
    - The script `1-install_load_balancer` installs HAProxy and configures it to distribute traffic.

    ```bash
    # Transfer and execute the script on lb-01
    scp 1-install_load_balancer ubuntu@54.164.28.73:/home/ubuntu/
    ssh ubuntu@54.164.28.73 'bash /home/ubuntu/1-install_load_balancer'
    ```

### Task 2: Add a Custom HTTP Header with Puppet

**Objective:** Automate the addition of a custom HTTP header to Nginx responses using Puppet.

#### Requirements:
- Configure Nginx to include the custom HTTP header `X-Served-By` with the server's hostname.
- Use a Puppet manifest to automate the configuration.

#### Instructions:
1. **Create and apply the Puppet manifest:**
    - The Puppet manifest `2-puppet_custom_http_response_header.pp` configures Nginx to add the custom header.

    ```bash
    # Transfer and apply the Puppet manifest on web-01 and web-02
    scp 2-puppet_custom_http_response_header.pp ubuntu@18.209.179.77:/home/ubuntu/
    ssh ubuntu@18.209.179.77 'sudo puppet apply /home/ubuntu/2-puppet_custom_http_response_header.pp'

    scp 2-puppet_custom_http_response_header.pp ubuntu@100.25.37.11:/home/ubuntu/
    ssh ubuntu@100.25.37.11 'sudo puppet apply /home/ubuntu/2-puppet_custom_http_response_header.pp'
    ```

## Verification

To verify the setup, you can use `curl` to check the response headers:

```bash
curl -sI http://<lb-01-ip> | grep X-Served-By
