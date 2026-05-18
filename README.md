> **Note:** Only works with VMware Workstation Pro (it's free — don't use VMware Player)

# VMware Discord Rich Presence

Shows your currently running VMware VM in your Discord status, including the VM name and OS. Updates every 5 seconds and clears when no VM is running.

![Discord Status Example](https://i.imgur.com/placeholder.png)

---

## Requirements

- Python 3.8+
- [VMware Workstation Pro](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion) (free)
- Discord desktop app running

---

## Setup

### 1. Create a Discord Application

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Copy the **Application ID** — you'll need it in the next step
4. Go to **Rich Presence → Art Assets**
5. Upload your VMware logo and name the asset exactly `vmware`

### 2. Set Your Client ID

Open `main.py` and replace the `CLIENT_ID` with your Application ID:

```python
CLIENT_ID = 'YOUR_APPLICATION_ID_HERE'
```

The current default ID (`1505562752083562617`) is the author's own app — replace it with yours if you want your own application name shown in Discord.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python main.py
```

---

## Features

- Detects running VMware VMs automatically via process scanning
- Shows VM name and guest OS in Discord status
- Updates every 5 seconds
- Shows an idle state when VMware is open but no VM is running
- Clears status when VMware is closed

---

## Example Status

```
Running • Windows 10 x64
VM: Development Machine
```

---

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| `pypresence` | 4.3.0 | Discord RPC connection |
| `psutil` | 5.9.8 | VMware process detection |

---

## License

See [LICENSE](LICENSE).
