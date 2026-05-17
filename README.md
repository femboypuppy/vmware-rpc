
# ONLY WORKS IN VMWARE WORKSTATION PRO (It's free please don't use vmware player guys)


# VMware Discord Rich Presence

Shows your running VMware VM in Discord status.

## Setup

1. **Create Discord Application**
   - Go to https://discord.com/developers/applications
   - Click "New Application"
   - Copy the Application ID
   - Go to "Rich Presence" → "Art Assets"
   - Upload VMware logo and name it `vmware`
   - Replace `CLIENT_ID` in `main.py` with your Application ID

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run**
   ```bash
   python main.py
   ```

## Features

- Automatically detects running VMware VMs
- Shows VM name and OS in Discord status
- Updates every 5 seconds
- Clears status when no VM is running

## Example Status

```
Running • Windows 10 x64
VM: Development Machine
```
