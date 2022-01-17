# ------------------------------------------------------------------------------
# CMSC 291 Lecture 10: Default Application configuration for Jupyter Lab
# ------------------------------------------------------------------------------


## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = "notebooks"

## Forces users to use a password for the Notebook server. This is useful in a
#  multi user environment, for instance when everybody in the LAN can access each
#  other's machine through ssh.
#
#  In such a case, serving the notebook server on localhost is not secure since
#  any user can connect to the notebook server via ssh. But not necessary here.
c.NotebookApp.password_required = False

## The port the notebook server will listen on (env: JUPYTER_PORT).
c.NotebookApp.port = 8888
