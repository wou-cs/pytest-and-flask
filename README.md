# mongodb-test-client

A very simple Python client for MongoDB using mongoengine.

To use this client:

- Copy `sample.settings` to `dev.settings`
- Edit `dev.settings` with your connection information for MongoDB. If using a cloud server such as [MongoDB Atlas](https://cloud.mongodb.com), you'll see details there.
- You may need to [whitelist the IP address for your local machine](https://studio3t.com/knowledge-base/articles/mongodb-atlas-login-ip-whitelisting/).
- Run the script `rundev.sh` which will load your settings and run the tiny test client.
