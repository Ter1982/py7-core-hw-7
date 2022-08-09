from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Very useful code',
      author='Mykhailo Ter-Gukasian',
      author_email='mter1982@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
      )
