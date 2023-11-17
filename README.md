RADManager - Rad Active Directory Manager

Description:

RADManager is a simple web-based user management tool built on the Django framework. It offers a set of basic features and is designed for small-scale use cases. Please note that it is not intended for use in critical network environments. Its primary purpose is for use in small lab setups.

Features Include:

    LDAP Reader: Allows you to read LDAP (Lightweight Directory Access Protocol) information.

    LDAP Settings Page: Provides a page for configuring LDAP settings.

    User List: Displays a list of users.

    Reset Passwords: Allows you to reset user passwords.

    Add Users: Provides functionality to add new users.

    Default Password Parameters: Includes default password parameters for user management.

Security Considerations:

    The application is designed with minimal security features and is best suited for small-scale labs.
    Critical pages are user and password protected using Django's built-in user management system.
    We do not recommend port forwarding unless the application is placed behind an SSL/TLS-protected proxy with appropriate Access Control Lists (ACLs) in place.

Please use this tool responsibly and consider the security implications, especially when handling user accounts and LDAP settings.

![image](https://github.com/Deathraymind/RADManager/assets/116578035/1c78cb71-6deb-48a8-aab6-35b29d073c3f)
![image](https://github.com/Deathraymind/RADManager/assets/116578035/14534842-2708-4f8f-ac5f-dd2bd9748d14)
![image](https://github.com/Deathraymind/RADManager/assets/116578035/d047251b-9b4f-49de-9d80-4d4184407cad)

Installation Instructions

Step 1: Download and Extract

    Download the application and place it on your domain controller's administrator user account. For example, you can put it in the Documents folder.

    Extract the contents of the downloaded archive.

Step 2: Setup and Dependency Installation

    Navigate to the extracted directory.

    Run the install.ps1 script, which will set up a virtual environment and install all required dependencies.

Step 3: Running the Application

    Execute the run.ps1 script to start the application.

Step 4: Accessing the Web Interface

    Open your web browser and type in the following URL: http://localhost:8000/main. This will take you to the main menu of the application.

Step 5: Initial Configuration (Recommended)

    It's recommended to perform some initial configuration:

    a. Navigate to RADManager > env > scripts.

    b. Open a terminal in this directory and run ./activate. This activates the Python virtual environment.

    c. Run the command python manage.py createsuperuser to create a new user and set a password.

    d. Execute the run.ps1 script again. This step ensures that the newly created user can access pages that require root login.

These revised instructions are presented in a clear and organized manner to help users with the 
