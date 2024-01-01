import subprocess

# Run pip freeze command to get installed packages
output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')

# Filter out only the Django-related packages
django_packages = [line.strip() for line in output.split('\n') if 'django' in line.lower()]

# Write the Django packages to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write('# Django Project README\n\n')
    readme_file.write('## Third-Party Apps\n\n')
    for package in django_packages:
        readme_file.write(f'- {package}\n')
    readme_file.write('\n## Run these commands as follows on the root directory of the project:\n\n')
    readme_file.write('```diff\n+ python manage.py makemigrations\n')
    readme_file.write('+ python manage.py migrate\n')
    readme_file.write('+ python manage.py runserver\n```')