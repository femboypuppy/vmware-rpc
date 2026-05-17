import time
from vmware_detector import get_vmware_info, is_vmware_running
from discord_rpc import DiscordRPC

CLIENT_ID = '1505562752083562617'  # Replace with your Discord App Client ID

def main():
    print("VMware Discord RPC Starting...")
    
    rpc = DiscordRPC(CLIENT_ID)
    if not rpc.connect():
        print("Failed to connect to Discord. Make sure Discord is running.")
        return
    
    print("Connected to Discord!")
    print("Monitoring VMware...")
    
    last_vm = None
    vmware_was_running = False
    
    try:
        while True:
            vmware_running = is_vmware_running()
            vm_info = get_vmware_info()
            
            if not vmware_running:
                if vmware_was_running:
                    print("\nVMware closed")
                    rpc.clear()
                    last_vm = None
                    vmware_was_running = False
            elif vm_info:
                if vm_info != last_vm:
                    print(f"\nVM Detected: {vm_info['name']}")
                    print(f"OS: {vm_info['os']}")
                    rpc.update(vm_info)
                    last_vm = vm_info
                    vmware_was_running = True
            else:
                if last_vm or not vmware_was_running:
                    print("\nVMware open - Idling")
                    rpc.idle()
                    last_vm = None
                    vmware_was_running = True
            
            time.sleep(5)
    
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        rpc.close()

if __name__ == '__main__':
    main()
