# Blockchain Voting
###### work in progress
Wouldn't it be cool if I could come up with a solid name?

Check out the YAMLs in `application/config` to see what 
type of things you have control over. It's pretty
simple:

`redis` handles the backend database for the master node, this is the only
"centralized" database, and it's really just to keep track
of nodes and facilitate voting/policies.

## 1) First things first -- you need a master node
### tl;dr?
run setup.sh
### more details on that
if you want to pioneer it yourself, you will need to run
the `application/setup.py` file by running 
`pip install -e application` from the content root.

Once you have that, you'll have access to the `Command Line Interface`
which holds many different functions (check them out by running
`blockchain --help`)

Now start your master node with `blockchain start-master-node` there are
optional arguments you can provide for a redis port and host, but 
the defaults are built in


## 2) You've built the master node! Nice!
When you're setting up a new voting machine (these are the nodes)
you will need to make sure that it's provided a handshake 