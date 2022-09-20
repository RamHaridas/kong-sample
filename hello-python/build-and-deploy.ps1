faas-cli login --username admin --password X1E81lQrU3G24zans6A7aR18Y
faas-cli build -f ./hello-python.yml
faas-cli push -f ./hello-python.yml
faas-cli deploy -f ./hello-python.yml