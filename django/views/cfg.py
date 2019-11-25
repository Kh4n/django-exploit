from pycfg.pycfg import PyCFG, CFGNode, slurp 

def traverse(cfgnode, funcs):
  #print("CHildren: ", cfgnode.children)
  #print(cfgnode.source())
  if hasattr(cfgnode, 'visited'):
    cfgnode.visited += 1
  else:
    cfgnode.visited = 1
  print(cfgnode)
  if len(cfgnode.calls) > 0:
    for call in cfgnode.calls:
      test = []
      try:
        test = funcs[call]
      except:
        # print("Built-in function ", call)
        pass
      for node in test:
        traverse(node, funcs)
  for child in cfgnode.children[::-1]:
    if not hasattr(child, 'visited') or child.visited < 5:
      traverse(child, funcs)
  #print("Calls: ", cfgnode.calls)
  #print("Regid: ", cfgnode.rid)
  #print("ast: ", cfgnode.ast_node.lineno)

cfg = PyCFG()
cfg.gen_cfg(slurp("/mnt/c/Users/dylan/programming/6332/lemme_in.py").strip())
cfg2 = PyCFG()
cfg2.gen_cfg(slurp("/mnt/c/Users/dylan/programming/6332/django/django/views/defaults.py").strip())
g = CFGNode.to_graph([])
print(cfg2.functions)
traverse(cfg2.functions['page_not_found'][0], cfg2.functions)

print("This is the graph: ", g)
print("It has %d nodes and %d edges" % (g.number_of_nodes(), g.number_of_edges()))
print("calls: ", cfg.founder.calls);


