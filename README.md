# mongodb-test-client

A very simple Python Flask client for MongoDB using mongoengine, with a demonstration of how to use Pytest to test Flask routes.

To use this client:

- Copy `sample.settings` to `dev.settings`
- Do the same to create a `test.settings` file
- Edit `dev.settings` with your connection information for MongoDB. If using a cloud server such as [MongoDB Atlas](https://cloud.mongodb.com), you'll see details there.
- You may need to [whitelist the IP address for your local machine](https://studio3t.com/knowledge-base/articles/mongodb-atlas-login-ip-whitelisting/).
- Run the script `rundev.sh` which will load your settings and run the tiny test client.
- Run the script `runtests.sh` to run the Pytest tests
