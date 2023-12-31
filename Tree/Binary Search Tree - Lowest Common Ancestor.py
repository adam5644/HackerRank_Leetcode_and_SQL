def lca(root, v1, v2):
    while root.info > v1 and root.info > v2:
        root = root.left
    while root.info < v1 and root.info < v2:
         root = root.right
    return root