"""Weak editable predictor: cumulative degree-product score."""

class LinkPredictor:
    def fit(self, n_nodes, old_edges, recent_edges):
        self.degree = [0] * n_nodes
        for u, v in old_edges + recent_edges:
            self.degree[u] += 1
            self.degree[v] += 1

    def score(self, u, v):
        return float(self.degree[u] * self.degree[v])
