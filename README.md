
# Port Scanner

**Port Scanner** is a Python script designed to identify open ports on a specified host. It utilizes the `socket` library to attempt connections to a range of ports and reports which ones are open.

## Features

- **Range Scanning**: Scan a specified range of ports on a target host.
- **Customizable Timeouts**: Set connection timeout durations to balance between speed and accuracy.
- **Threaded Scanning**: Employs multithreading to expedite the scanning process.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhilov23/Port_Scanner.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Port_Scanner
   ```

## Usage

1. **Run the Script**:
   ```bash
   python port_scanner.py
   ```
2. **Provide Input When Prompted**:
   - **Target Host**: Enter the IP address or domain name of the host you wish to scan.
   - **Starting Port**: Enter the starting port number of the range you want to scan.
   - **Ending Port**: Enter the ending port number of the range you want to scan.

3. **Example**:
   ```plaintext
   Enter target host: example.com
   Enter starting port: 20
   Enter ending port: 80
   ```

   The script will then attempt to connect to each port in the specified range and display whether each port is open or closed.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

**Use this tool responsibly.** Unauthorized port scanning of systems without permission is illegal and unethical. Ensure you have explicit permission before scanning any network or host.

## Author

**Abhilov Gupta**  
- GitHub: [abhilov23](https://github.com/abhilov23)  
- Twitter: [@Abhilov_](https://twitter.com/Abhilov_)
