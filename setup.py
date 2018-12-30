from distutils.core import setup
setup(
  name = 'ltspice',         # How you named your package folder (MyLib)
  packages = ['ltspice'],   # Chose the same as "name"
  version = '0.2.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'DESC',   # Give a short description about your library
  author = 'DonghoonPark',                   # Type in your name
  author_email = 'donghun94@snu.ac.kr',      # Type in your E-Mail
  keywords = ['ltspice', 'multi point simulation'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
      ],
  classifiers=[
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)