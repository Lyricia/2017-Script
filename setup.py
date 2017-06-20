from distutils.core import setup, Extension

files = ["bookmarkdata.txt",
         'data.txt',
         'list.txt',
         'rawdata.xml'
         'loadmod.pyd'
         'savemod.pyd'
         ]

setup(name='MyPyProj',
version='1.0',
packages=['MyPyProj'],
package_data = {'MyPyProj' : files },
)
