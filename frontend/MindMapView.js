import React, { useState, useEffect } from 'react';
import { fetchMindMapData } from './apiService';

const API_URL = process.env.REACT_APP_API_URL;

const defaultNodes = [
  { id: 1, title: 'Root', position: { x: 250, y: 5 } },
];

function MindMapView() {
  const [nodes, setNodes] = useState(defaultNodes);
  const [connections, setConnections] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      try {
        const apiUrl = `${API_URL}/mindmaps`;
        const data = await fetchMindMapData(apiUrl);
        if (data) {
          setNodes(data.nodes);
          setConnections(data.connections);
        }
      } catch (error) {
        console.error("Failed to fetch mind map data:", error);
      }
    };

    loadData();
  }, []);

  const handleNodeClick = (nodeId) => {
    console.log(`Node ${nodeId} clicked`);
  };

  return (
    <div className="mindMapContainer" style={{ position: 'relative' }}>
      {nodes.map((node) => (
        <div
          key={node.id}
          className="node"
          style={{ position: 'absolute', left: node.position.x, top: node.position.y }}
          onClick={() => handleNodeClick(node.id)}
        >
          {node.title}
        </div>
      ))}
    </div>
  );
}

export default MindMapView;