# Firewall Configuration Script

This repository contains a script to configure the `ufw` firewall on a Ubuntu server to block all incoming traffic except for the following TCP ports:
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

## Files

- `0-block_all_incoming_traffic_but`: A bash script to configure the `ufw` firewall.

## Usage

1. **Connect to your server:**
    ```sh
    ssh ubuntu@your_server_ip
    ```

2. **Upload the script to your server.** You can use `scp` to transfer the script:
    ```sh
    scp 0-block_all_incoming_traffic_but ubuntu@your_server_ip:~
    ```

3. **Make the script executable:**
    ```sh
    chmod +x 0-block_all_incoming_traffic_but
    ```

4. **Run the script:**
    ```sh
    ./0-block_all_incoming_traffic_but
    ```

5. **Verify the UFW status to ensure the rules are applied correctly:**
    ```sh
    sudo ufw status verbose
    ```

## Notes

- The script will reset `ufw` to its default settings before applying the new rules.
- Make sure to run the script with sudo privileges to allow it to modify firewall settings.
