# wifi-password-extractor-python

Extract saved Wi-Fi profiles and passwords on Windows and export them to a CSV file using Python and netsh.

This Python script allows you to extract all saved Wi-Fi profiles and their passwords from a Windows machine using the netsh command-line tool. It retrieves the Wi-Fi names (SSIDs) along with their corresponding passwords (if available) and exports the data into a neatly formatted CSV file for backup or administrative use.

🔧Features:
Retrieves all saved Wi-Fi profiles using netsh
Extracts passwords (if stored)
Exports the results to a CSV file using pandas
User-friendly console output

💡Use Cases:
Backup your Wi-Fi credentials
Audit saved networks on your system
