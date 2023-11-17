from django.shortcuts import render
from ldap3 import Server, Connection, ALL
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import subprocess
from settingsapp.models import AppSettings


@login_required
def get_ad_users(request):
    settings = AppSettings.objects.first()
    if not settings:
        print("App settings not found.")
        return []

    # Use the correct field name based on your model
    domain = settings.domain
    user_dn = settings.user_dn
    password = settings.password
    search_base = settings.search_base

    try:
        server = Server(domain, get_info=ALL)
        conn = Connection(server, user_dn, password, auto_bind=True)
        conn.search(search_base, '(objectclass=person)', attributes=['cn', 'givenName', 'sn', 'mail'])

        users = []
        for entry in conn.entries:
            users.append({
                'cn': entry.cn.value if 'cn' in entry else 'N/A',
                'givenName': entry.givenName.value if 'givenName' in entry else 'N/A',
                'sn': entry.sn.value if 'sn' in entry else 'N/A',
                'mail': entry.mail.value if 'mail' in entry else 'N/A'
            })
        return users
    except Exception as e:
        print("Error connecting to AD:", e)
        return []

    
@login_required
def list_users(request):
    users = get_ad_users(request)
    return render(request, 'list_users.html', {'users': users})

@login_required
def reset_password(request, username):
    settings = AppSettings.objects.first()
    if not settings:
        return HttpResponse("App settings not found.")

    try:
        new_password = settings.default_password

        ps_script = f"""
        $username = '{username}'
        $new_password = '{new_password}'

        Set-ADAccountPassword -Identity $username -NewPassword (ConvertTo-SecureString -AsPlainText $new_password -Force)
        Set-ADUser -Identity $username -ChangePasswordAtLogon $true
        """

        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_script], capture_output=True)

        return HttpResponse("Password reset successfully. User must change password at next logon.")
    except Exception as e:
        print("Error resetting password:", e)
        return HttpResponse("Error resetting password.")
