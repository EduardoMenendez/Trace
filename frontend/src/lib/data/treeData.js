export const treeData = {
    node_id: "https://example.com",
    name: "example.com",
    severity: "Low",
    children: [
      {
        node_id: "https://example.com/api",
        name: "api",
        severity: "Medium",
        children: [
          {
            node_id: "https://example.com/api/v1",
            name: "v1",
            severity: "High",
            children: []
          }
        ]
      },
      {
        node_id: "https://example.com/docs",
        name: "docs",
        severity: "Low",
        children: []
      }
    ]
    
  };
  