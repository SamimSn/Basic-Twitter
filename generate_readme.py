import subprocess

# Run pip freeze command to get installed packages
output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')

# Filter out only the Django-related packages
django_packages = [line.strip() for line in output.split('\n') if 'django' in line.lower()]

# Write the Django packages to README.md
with open('requirements.txt', 'w') as readme_file:    
    for package in django_packages:
        readme_file.write(f'{package}\n')    