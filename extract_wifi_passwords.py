import subprocess
import pandas as pd

# Initialize a list to hold the Wi-Fi profiles and passwords
wifi_data = []


#Get All WIFI User Profilies
data = subprocess.check_output(['netsh','wlan','show','profile'], encoding='utf-8', errors='ignore')
# print("ALL WIFI PROFILIES",data)

profiles = []

for i in data.split('\n'):
    if "All User Profile" in i:
      parts = i.split(":")
      if len(parts) > 1:
        profiles.append(parts[1].strip())  
# print("PROFILES", profiles)


# Open the file for writing and store the Wi-Fi profiles and passwords
print("{:<30} {:<}".format("Wifi Name","Password")) # Print header with columns for Wi-Fi name and password
print("-" * 50 + "\n")

# Retrieve the Wi-Fi name and password and store in a list
for profile in profiles:
    try:
        #Get the key content (password) for each profile
        result = subprocess.check_output(['netsh','wlan','show','profile',profile,'key=clear'], encoding='utf-8', errors='ignore')
        # print("RESULTS", result) #Profile Information
            

        password_lines=[] #Password Lines
        for line in result.split('\n'):
            if "Key Content" in line:
                password_lines.append(line)
        # print("PASSWORD LINES", password_lines)
                    
            
        if password_lines:
            password = password_lines[0].split(":")[1].strip()
        else:
            password = ""

        # Append the profile name and password to the list
        wifi_data.append([profile, password])
    
    except subprocess.CalledProcessError:

        # In case of error, append 'Error Retrieving' as the password
        wifi_data.append([profile, "Error Retrieving"])


# Create a DataFrame from the list of data
df = pd.DataFrame(wifi_data, columns=["Wi-Fi Name", "Password"])

# Store the DataFrame in a CSV file   * Set The File Path Correctly*
df.to_csv("D:/Besant Technologies/OCT_NOV_DEC(Python Batch I)/code source/wifi_passwords.csv", index=False)

# Print the DataFrame for confirmation
print(df)
