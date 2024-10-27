from django.shortcuts import render
import subprocess
from django.shortcuts import render, redirect
from django.http import HttpResponse

def start_hotspot(request):
    if request.method == 'POST':
        ssid = request.POST.get('ssid')
        key = request.POST.get('key')
        if len(key) < 8:
            return HttpResponse("Key must be at least 8 characters long.")
        
        try:
            subprocess.run(["netsh", "wlan", "set", "hostednetwork", "mode=allow", f"ssid={ssid}", f"key={key}"], check=True)
            subprocess.run(["netsh", "wlan", "start", "hostednetwork"], check=True)
            return HttpResponse("Hotspot started successfully.")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Failed to start hotspot: {e}")
    
    return render(request, 'hotspot/start_hotspot.html')

def stop_hotspot(request):
    try:
        subprocess.run(["netsh", "wlan", "stop", "hostednetwork"], check=True)
        return HttpResponse("Hotspot stopped successfully.")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Failed to stop hotspot: {e}")

def show_hotspot_status(request):
    try:
        result = subprocess.run(["netsh", "wlan", "show", "hostednetwork"], check=True, capture_output=True, text=True)
        return HttpResponse(f"<pre>{result.stdout}</pre>")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Failed to show hotspot status: {e}")

