from pypresence import Presence
import time

class DiscordRPC:
    def __init__(self, client_id='1234567890123456789'):
        self.client_id = client_id
        self.rpc = None
        
    def connect(self):
        try:
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            return True
        except:
            return False
    
    def update(self, vm_info):
        if not self.rpc:
            return
        
        details = f"{vm_info['state']} • {vm_info['os']}"
        state = f"VM: {vm_info['name']}"
        
        try:
            self.rpc.update(
                details=details,
                state=state,
                large_image='vmware',
                large_text='VMware Workstation Pro',
                small_image='running',
                small_text=vm_info['state']
            )
        except:
            pass
    
    def idle(self):
        if not self.rpc:
            return
        
        try:
            self.rpc.update(
                details='Idling',
                state='No VMs running',
                large_image='vmware',
                large_text='VMware Workstation Pro'
            )
        except:
            pass
    
    def clear(self):
        if self.rpc:
            try:
                self.rpc.clear()
            except:
                pass
    
    def close(self):
        if self.rpc:
            try:
                self.rpc.close()
            except:
                pass
