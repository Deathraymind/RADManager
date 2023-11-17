from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
import subprocess
@login_required
def add_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Call the function to execute PowerShell script here
            create_ad_user(username, password)
            # You might want to add some context or redirect after the operation
    else:
        form = CreateUserForm()

    return render(request, 'add_user.html', {'form': form})

def create_ad_user(username, password):
    # Convert the password to a secure string in PowerShell
    ps_script = f"""
    $secureString = ConvertTo-SecureString '{password}' -AsPlainText -Force
    New-ADUser -Name '{username}' -AccountPassword $secureString -Enabled $true -CannotChangePassword $false -ChangePasswordAtLogon $true -PasswordNeverExpires $false
    """
    subprocess.run(["powershell", "-Command", ps_script], capture_output=True)
