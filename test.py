from chain import blocks,nodes
from voters import voter

starting_chain = blocks.BlockModule()

node = nodes.Node(starting_chain)

my_chain = node.block()

v = voter.Voter()
r = voter.Rolls()

user = "blake"

r.register(user, "mypass")

v.login(user, "mypass")

vote_cast = "berniesanders"
if v.logged_in:
    my_chain.add_block(my_chain.create_block([v.username(), vote_cast]))
    node.verify()


print(starting_chain.winner(node.database().get_all_blocks()))

