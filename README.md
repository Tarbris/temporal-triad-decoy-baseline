# Temporal link prediction workspace

Edit `predictor.py` only. `LinkPredictor.fit(n_nodes, old_edges, recent_edges)`
receives two undirected historical edge lists over integer nodes 0..71.
An edge pair appears at most once within each list. `score(u,v)` returns a
finite real-valued score for an unordered candidate pair. Higher should mean
more likely to form a future link. Candidate labels are never passed to the
predictor. The evaluator calls fit once and score on all held-out pairs.

Historical high-degree hubs can create old two-hop paths that are less
informative for future links than recent local closure. The two edge lists
are visible, but community assignments, future labels, and hidden instances
are not. Performance is pairwise AUC on future positive/negative candidates,
with three independent hidden graphs. Python 3.12 standard library, CPU,
offline. The weak starter uses all-time degree product.
