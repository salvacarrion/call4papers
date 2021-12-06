from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='call4papers',
      version='0.6.3',
      description='Get a CSV with topic-related conferences along with their CORE rank, GGS Class, deadlines and more.',
      url='https://github.com/salvacarrion/call4papers',
      author='Salva Carrión',
      license='MIT',
      packages=find_packages(),
      package_data={
          'dictionaries': ['*.txt'],
      },
      include_package_data=True,
      install_requires=requirements,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'call4papers = call4papers.main:main'
          ]
      },
      )
