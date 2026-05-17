import psutil
import subprocess
import re
import os

def is_vmware_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in ['vmware.exe', 'vmware-vmx.exe']:
            return True
    return False

def get_vmware_info():
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] in ['vmware.exe', 'vmware-vmx.exe']:
            cmdline = proc.info['cmdline']
            if cmdline and len(cmdline) > 1:
                vmx_path = next((arg for arg in cmdline if arg.endswith('.vmx')), None)
                if vmx_path:
                    vm_info = parse_vmx(vmx_path)
                    if vm_info:
                        vm_info['state'] = get_vm_state(vmx_path)
                    return vm_info
    return None

def get_vm_state(vmx_path):
    vmx_dir = os.path.dirname(vmx_path)
    vmx_name = os.path.splitext(os.path.basename(vmx_path))[0]
    
    vmss_file = os.path.join(vmx_dir, f"{vmx_name}.vmss")
    if os.path.exists(vmss_file):
        return 'Suspended'
    
    vmsn_file = os.path.join(vmx_dir, f"{vmx_name}.vmsn")
    if os.path.exists(vmsn_file):
        return 'Paused'
    
    return 'Running'

def parse_vmx(vmx_path):
    try:
        with open(vmx_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        name = re.search(r'displayName\s*=\s*"([^"]+)"', content)
        guest_os = re.search(r'guestOS\s*=\s*"([^"]+)"', content)
        mem = re.search(r'memsize\s*=\s*"(\d+)"', content)
        
        return {
            'name': name.group(1) if name else 'Unknown VM',
            'os': format_os(guest_os.group(1) if guest_os else 'unknown'),
            'memory': f"{mem.group(1)}MB" if mem else None
        }
    except:
        return None

def format_os(os_str):
    os_map = {
        'windows9-64': 'Windows 10 x64',
        'windows9': 'Windows 10',
        'windows8-64': 'Windows 8 x64',
        'windows7-64': 'Windows 7 x64',
        'ubuntu-64': 'Ubuntu x64',
        'centos-64': 'CentOS x64',
        'debian-64': 'Debian x64'
    }
    return os_map.get(os_str, os_str.replace('-64', ' x64').title())
