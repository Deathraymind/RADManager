# PowerShell script to start the Django project

# Define the project directory
$projectDir = "C:\Program Files\ADManager"

# Check if the project directory exists
if (-Not (Test-Path $projectDir)) {
    Write-Error "Project directory not found."
    exit
}

# Navigate to the project directory
Set-Location $projectDir

# Activate the virtual environment
& "$projectDir\env\Scripts\Activate"

# Start Django development server
python manage.py runserver

# Additional commands can be added here if necessary
